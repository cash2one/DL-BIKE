# coding=utf-8

# @Time    : 3/12/17 15:56
# @Author  : panda (panyuxin@moseeker.com)
# @File    : hztrip.py
# @DES     :

import time
from tornado import gen

import conf.path as path
import conf.headers as headers
from setting import settings
from service.data.base import DataService
from cache.hztrip import HztripCache
from util.common import ObjectDict
from util.tool.http_tool import http_get, http_post, http_fetch
from util.common.decorator import cache


class HztripDataService(DataService):

    hztrip = HztripCache()

    """对接网络请求服务"""

    @cache(300)
    @gen.coroutine
    def get_lnglat_by_baidu(self, q, city=None):
        """根据地址，查找Baidu经纬度信息
        demo: http://api.map.baidu.com/geocoder/v2/?output=json&ak=lSbGt6Z31wK9Pwi2GLUCx6ywLeflbjHf&city=杭州&address=玉泉校区

        :param q: 检索关键字
        :param city: 检索区域（市级以上行政区域）
        :return json
        """
        if city is None:
            city = "杭州"

        params = ObjectDict({
            "region": city,
            "query": q,
            "page_size": 1,
            "page_num": 0,
            "scope": 1,
            "output": "json",
            "ak": settings['baidu_ak'],
        })

        ret = yield http_get(route=path.BAIDU_WEBAPI_PLACE_POI_LIST, jdata=params, timeout=5)
        if ret:
            raise gen.Return(ret)
        else:
            raise gen.Return(ObjectDict())

    @cache(300)
    @gen.coroutine
    def get_lnglat_by_soso(self, q, city=None):
        """根据地址，查找soso经纬度信息
        http://lbs.qq.com/webservice_v1/guide-geocoder.html
        demo: http://apis.map.qq.com/ws/geocoder/v1/?address=北京市海淀区彩和坊路海淀西大街74号&key=OB4BZ-D4W3U-B7VVO-4PJWW-6TKDJ-WPB77

        :param q: 检索关键字
        :param city: 检索区域（市级以上行政区域）
        :return json
        """
        if city is None:
            city = "浙江杭州"

        params = ObjectDict({
            "address": "{}{}".format(city, q),
            "output": "json",
            "key": settings['soso_ak'],
        })

        ret = yield http_get(route=path.QQ_WEBAPI_PLACE_POI_LIST, jdata=params, timeout=5)
        if ret:
            raise gen.Return(ret)
        else:
            raise gen.Return(ObjectDict())

    @cache(300)
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

        ret = yield http_get(route=path.BAIDU_WEBAPI_GEOCONV_LNGLAT, jdata=params, timeout=5)
        if ret:
            raise gen.Return(ret)
        else:
            raise gen.Return(ObjectDict())

    @cache(300)
    @gen.coroutine
    def get_soso_lnglat(self, lng, lat):
        """根据百度地图经纬度，转换为微信经纬度为火星坐标
        refer: http://lbs.qq.com/webservice_v1/guide-convert.html
        demo: http://apis.map.qq.com/ws/coord/v1/translate?locations=39.12,116.83;30.21,115.43&type=3&key=OB4BZ-D4W3U-B7VVO-4PJWW-6TKDJ-WPB77

        :param lng: 经度
        :param lat: 纬度
        :return json
        """

        params = ObjectDict({
            "type": 3,
            "locations": "{},{}".format(lat, lng),
            "output": "json",
            "key": settings['soso_ak'],
        })

        ret = yield http_get(route=path.QQ_WEBAPI_GEOCONV_LNGLAT, jdata=params, timeout=5)
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

        ret = yield http_get(path.HZTRIP_STOP, params, headers=headers.COMMON_HEADER, timeout=5)

        if not ret:
            # yield self.del_ip_proxy(host)
            raise gen.Return(ObjectDict())
        raise gen.Return(ret)

    @cache(ttl=60)
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
        ret = yield http_get(path.HZTRIP_YAOHAO, params, headers=headers.COMMON_HEADER, timeout=5)

        if not ret:
            # yield self.del_ip_proxy(host)
            raise gen.Return(ObjectDict())
        raise gen.Return(ret)

    @cache(ttl=60)
    @gen.coroutine
    def get_bikes(self, openid, params=None):

        """
        根据经纬度，查找杭州公共自行车租赁点实时数据
        demo: http://c.ggzxc.com.cn/wz/np_getBikesByWeiXin.do?lng=121.377&lat=31.324736&len=800&_=1491833445547
        :param params:
        :return:
        """
        params = params or {}
        params.update({
            "len": 800,
            "_": int(round(time.time() * 1000))
        })

        # host, port = yield self.get_ip_proxy()

        header = headers.DATA_SOURCE.ggzxc_app.header
        cookie = "JSESSIONID=6C274EA3774D097085A5846C44F64A84; openid={}".format(openid)
        header.update({
            "cookie": cookie
        })

        # ret = yield http_get(path.HZTRIP_BIKE, params, headers=header, timeout=30,
        #                      proxy_host=host, proxy_port=port)

        ret = yield http_get(path.HZTRIP_BIKE, params, headers=header, timeout=5)

        if not ret:
            # yield self.del_ip_proxy(host)
            raise gen.Return(ObjectDict())
        raise gen.Return(ret)

    @cache(ttl=60)
    @gen.coroutine
    def get_bike_stations(self, openid, params=None):

        """
        根据租赁点编号，查询租赁点信息
        demo: http://c.ggzxc.com.cn/wz/np_getNPByNum.do?bean.number=1001&len=800
        :param params:
        :return:
        """
        params = params or {}
        params.update({
            "len": 800
        })

        # host, port = yield self.get_ip_proxy()

        header = headers.DATA_SOURCE.ggzxc_app.header
        cookie = "JSESSIONID=6C274EA3774D097085A5846C44F64A84; openid={}".format(openid)
        header.update({
            "cookie": cookie
        })

        # ret = yield http_get(path.HZTRIP_BIKE, params, headers=header, timeout=30,
        #                      proxy_host=host, proxy_port=port)

        ret = yield http_get(path.HZTRIP_BIKE_NO, params, headers=header, timeout=5)

        if not ret:
            # yield self.del_ip_proxy(host)
            raise gen.Return(ObjectDict())
        raise gen.Return(ret)

    @cache(ttl=300)
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

        ret = yield http_get(path.HZTRIP_BUS.format("findRouteByName"), params, headers=header, timeout=5)

        if ret.result == 0 and ret.total:
            for v in ret.get("items"):
                new_line_name = v.get("name").replace("(", "").replace(")", "")
                self.hztrip.set_bus_lines(new_line_name, v)

        if not ret:
            # yield self.del_ip_proxy(host)
            raise gen.Return(ObjectDict())
        raise gen.Return(ret)

    @cache(ttl=20)
    @gen.coroutine
    def get_bus_info(self, params=None):

        """
        根据线路名，查询公交实时到站
        demo: https://publictransit.dtdream.com/v1/bus/getBusPositionByRouteId?routeId=712
        :param params:
        :return:
        """
        params = params or {}

        # host, port = yield self.get_ip_proxy()

        header = headers.COMMON_HEADER

        # ret = yield http_get(path.HZTRIP_BIKE, params, headers=header, timeout=30,
        #                      proxy_host=host, proxy_port=port)

        ret = yield http_get(path.HZTRIP_BUS.format("getBusPositionByRouteId"), params, headers=header, timeout=5)

        if not ret:
            # yield self.del_ip_proxy(host)
            raise gen.Return(ObjectDict())
        raise gen.Return(ret)

    @cache(ttl=300)
    @gen.coroutine
    def get_bus_stops(self, params=None):

        """
        根据车站名，模糊查询公交车站
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

        ret = yield http_get(path.HZTRIP_BUS.format("findStopByName"), params, headers=header, timeout=5)

        if ret.result == 0 and ret.total:
            for v in ret.get("items"):
                self.hztrip.set_bus_stops(v.get("name"), v)

        if not ret:
            # yield self.del_ip_proxy(host)
            raise gen.Return(ObjectDict())
        raise gen.Return(ret)

    @cache(ttl=10)
    @gen.coroutine
    def get_stop_info(self, params=None):

        """
        根据车站名，查询电子站牌
        demo: https://publictransit.dtdream.com/v1/bus/getNextBusByStopId?amapStopId=BV10420834
        :param params:
        :return:
        """
        params = params or {}

        # host, port = yield self.get_ip_proxy()

        header = headers.COMMON_HEADER

        # ret = yield http_get(path.HZTRIP_BIKE, params, headers=header, timeout=30,
        #                      proxy_host=host, proxy_port=port)

        ret = yield http_get(path.HZTRIP_BUS.format("getNextBusByStopId"), params, headers=header, timeout=5)

        if not ret:
            # yield self.del_ip_proxy(host)
            raise gen.Return(ObjectDict())
        raise gen.Return(ret)

    @cache(ttl=20)
    @gen.coroutine
    def get_around_bus_stop(self, params=None):

        """
        根据经纬度，查找车站，线路
        demo: https://publictransit.dtdream.com/v1/bus/findNearbyStop?lng=120.169144&lat=30.262842&city=330100&token=&radius=1000
        :param params:
        :return:
        """
        params = params or {}
        params.update({
            "city": 330100,
            "token": "",
            "radius": 1000,
        })

        # host, port = yield self.get_ip_proxy()

        header = headers.COMMON_HEADER

        # ret = yield http_get(path.HZTRIP_BIKE, params, headers=header, timeout=30,
        #                      proxy_host=host, proxy_port=port)

        ret = yield http_get(path.HZTRIP_BUS.format("findNearbyStop"), params, headers=header, timeout=5)

        if not ret:
            # yield self.del_ip_proxy(host)
            raise gen.Return(ObjectDict())
        raise gen.Return(ret)

    @cache(ttl=300)
    @gen.coroutine
    def get_bd_transfer(self, params=None):
        """根据百度 api，查询换成方案
        refer: http://lbsyun.baidu.com/index.php?title=webapi/guide/changeposition
        demo: http://api.map.baidu.com/direction/v1?mode=transit&region=%E6%9D%AD%E5%B7%9E&output=json&ak=hS3TTOY2PEFFyTZsrmETWNlZ&origin=

        :param params:
        :return json
        """
        params = params or {}
        params.update({
            "mode": "transit",
            "region": "杭州",
            "output": "json",
            "ak": settings['baidu_ak'],
        })

        ret = yield http_get(route=path.BAIDU_WEBAPI_DIRECTION, jdata=params, timeout=5)
        if ret:
            raise gen.Return(ret)
        else:
            raise gen.Return(ObjectDict())