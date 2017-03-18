# coding=utf-8

# @Time    : 3/12/17 15:56
# @Author  : panda (panyuxin@moseeker.com)
# @File    : hztrip.py
# @DES     :

from tornado import gen

import conf.path as path
import conf.headers as headers
from setting import settings
from service.data.base import DataService
from cache.hztrip import HztripCache
from util.common import ObjectDict
from util.tool.str_tool import md5Encode
from util.tool.http_tool import http_get, http_post, http_fetch
from util.common.decorator import cache


class HztripDataService(DataService):

    hztrip = HztripCache()

    """对接网络请求服务"""

    @gen.coroutine
    def get_lnglat_by_baidu(self, q, city=None):
        """根据地址，查找经纬度信息
        demo: http://api.map.baidu.com/geocoder/v2/?output=json&ak=lSbGt6Z31wK9Pwi2GLUCx6ywLeflbjHf&city=杭州&address=玉泉校区

        :param q: 检索关键字
        :param city: 检索区域（市级以上行政区域）
        :return json
        """
        if city is None:
            city = "杭州"

        params = ObjectDict({
            "city": city,
            "address": q,
            "output": "json",
            "ak": settings['baidu_ak'],
        })

        ret = yield http_get(route=path.BAIDU_WEBAPI_PLACE_LNGLAT, jdata=params, timeout=40)
        if ret:
            raise gen.Return(ret)
        else:
            raise gen.Return(ObjectDict())

    @gen.coroutine
    def get_bd_lnglat(self, lng, lat):
        """根据微信经纬度为火星坐标，转换为百度地图经纬度
        refer: http://lbsyun.baidu.com/index.php?title=webapi/guide/changeposition
        demo: http://api.map.baidu.com/geoconv/v1/?from=3&to=5&ak=hS3TTOY2PEFFyTZsrmETWNlZ&coords=120.12,32.12

        :param lng: 经度
        :param lat: 纬度
        :return json
        """

        params = ObjectDict({
            "from": 3,
            "to": 5,
            "coords": "{},{}".format(lng, lat),
            "output": "json",
            "ak": settings['baidu_ak'],
        })

        ret = yield http_get(route=path.BAIDU_GEOCONV_LNGLAT, jdata=params, timeout=40)
        if ret:
            raise gen.Return(ret)
        else:
            raise gen.Return(ObjectDict())

    @cache(ttl=60)
    @gen.coroutine
    def get_stop(self, params=None):

        """
        根据经纬度，获得停车位信息
        demo: http://api.busditu.com/hangzhou/parking/nearby/
        :param params:
        :return:
        """

        params = params or {}
        params.update({
            "application": "busdituandroid",
            "code": "iVA7eOUG64aI0zHQ4L0LrvTtRhlyhJos",
            "count": 5,
            "redius": 10000,
        })

        # host, port = yield self.get_ip_proxy()

        # ret = yield http_get(path.HZTRIP_STOP, params, headers=headers.COMMON_HEADER, timeout=30,
        #                      proxy_host=host, proxy_port=port)

        ret = yield http_get(path.HZTRIP_STOP, params, headers=headers.COMMON_HEADER, timeout=30)

        if not ret:
            # yield self.del_ip_proxy(host)
            raise gen.Return(ObjectDict())
        raise gen.Return(ret)

    @gen.coroutine
    def get_yaohao(self, params=None):

        """
        根据用户名或编号，获得摇号结果
        demo: https://sp0.baidu.com/9_Q4sjW91Qh3otqbppnN2DJv/pae/common/api/yaohao
        :param params:
        :return:
        """

        params = params or {}
        params.update({
            "city": "杭州",
            "format": "json",
            "resource_id": 4003,
        })

        # host, port = yield self.get_ip_proxy()

        # ret = yield http_get(path.HZTRIP_YAOHAO, params, headers=headers.COMMON_HEADER, timeout=30,
        #                      proxy_host=host, proxy_port=port)
        ret = yield http_get(path.HZTRIP_YAOHAO, params, headers=headers.COMMON_HEADER, timeout=30)

        if not ret:
            # yield self.del_ip_proxy(host)
            raise gen.Return(ObjectDict())
        raise gen.Return(ret)

    @cache(ttl=120)
    @gen.coroutine
    def get_bikes(self, params=None):

        """
        根据经纬度，查找杭州公共自行车租赁点实时数据
        demo: http://c.ggzxc.com.cn/wz/np_getBikes.do?lng=120.17095&lat=30.246405&len=800
        :param params:
        :return:
        """
        params = params or {}
        params.update({
            "len": 800
        })

        # host, port = yield self.get_ip_proxy()

        header = headers.DATA_SOURCE.ggzxc_app.header
        openid = md5Encode(str(params.get("lng")))
        cookie = "JSESSIONID=6C274EA3774D097085A5846C44F64A84; openid={}".format(openid)
        header.update({
            "cookie": cookie
        })

        # ret = yield http_get(path.HZTRIP_BIKE, params, headers=header, timeout=30,
        #                      proxy_host=host, proxy_port=port)

        ret = yield http_get(path.HZTRIP_BIKE, params, headers=header, timeout=30)

        if not ret:
            # yield self.del_ip_proxy(host)
            raise gen.Return(ObjectDict())
        raise gen.Return(ret)

    @gen.coroutine
    def get_bus_lines(self, params=None):

        """
        根据线路名，模糊查询公交线路
        demo: https://publictransit.dtdream.com/v1/bus/findRouteByName?token=&city=%E6%9D%AD%E5%B7%9E&routeName=b
        :param params:
        :return:
        """
        params = params or {}
        params.update({
            "city": "杭州",
            "token": "",
        })

        # host, port = yield self.get_ip_proxy()

        header = headers.COMMON_HEADER

        # ret = yield http_get(path.HZTRIP_BIKE, params, headers=header, timeout=30,
        #                      proxy_host=host, proxy_port=port)

        ret = yield http_get(path.HZTRIP_BUS.format("findRouteByName"), params, headers=header, timeout=30)

        if ret.result == 0 and ret.total:
            for v in ret.get("items"):
                self.hztrip.set_bus_lines(v.get("name"), v)

        if not ret:
            # yield self.del_ip_proxy(host)
            raise gen.Return(ObjectDict())
        raise gen.Return(ret)

    @gen.coroutine
    def get_bus_info(self, params=None):

        """
        根据线路名，查询公交线路
        demo: https://publictransit.dtdream.com/v1/bus/getBusPositionByRouteId?routeId=712
        :param params:
        :return:
        """
        params = params or {}

        # host, port = yield self.get_ip_proxy()

        header = headers.COMMON_HEADER

        # ret = yield http_get(path.HZTRIP_BIKE, params, headers=header, timeout=30,
        #                      proxy_host=host, proxy_port=port)

        ret = yield http_get(path.HZTRIP_BUS.format("getBusPositionByRouteId"), params, headers=header, timeout=30)

        if not ret:
            # yield self.del_ip_proxy(host)
            raise gen.Return(ObjectDict())
        raise gen.Return(ret)

    @gen.coroutine
    def get_bus_realtime_route(self, params=None):

        """
        根据线路名, 查询公交线路实时轨迹
        demo: https://publictransit.dtdream.com/v1/bus/getNextBusByRouteStopId?routeId=712&stopId=22628
        :param params:
        :return:
        """
        params = params or {}

        # host, port = yield self.get_ip_proxy()

        header = headers.COMMON_HEADER

        # ret = yield http_get(path.HZTRIP_BIKE, params, headers=header, timeout=30,
        #                      proxy_host=host, proxy_port=port)

        ret = yield http_get(path.HZTRIP_BUS.format("getNextBusByRouteStopId"), params, headers=header, timeout=30)

        if not ret:
            # yield self.del_ip_proxy(host)
            raise gen.Return(ObjectDict())
        raise gen.Return(ret)

    @gen.coroutine
    def get_bus_stops(self, params=None):

        """
        根据车站名，查询公交车站
        demo: https://publictransit.dtdream.com/v1/bus/findStopByName?city=%E6%9D%AD%E5%B7%9E&stopName=%E5%B0%8F
        :param params:
        :return:
        """
        params = params or {}
        params.update({
            "city": "杭州",
        })

        # host, port = yield self.get_ip_proxy()

        header = headers.COMMON_HEADER

        # ret = yield http_get(path.HZTRIP_BIKE, params, headers=header, timeout=30,
        #                      proxy_host=host, proxy_port=port)

        ret = yield http_get(path.HZTRIP_BUS.format("findStopByName"), params, headers=header, timeout=30)

        if ret.result == 0 and ret.total:
            for v in ret.get("items"):
                self.hztrip.set_bus_stops(v.get("name"), v)

        if not ret:
            # yield self.del_ip_proxy(host)
            raise gen.Return(ObjectDict())
        raise gen.Return(ret)