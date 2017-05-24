# coding=utf-8

import ujson
from tornado import gen

import conf.path as path
import conf.headers as headers
from setting import settings
from service.data.base import DataService
from cache.ipproxy import IpproxyCache
from util.common import ObjectDict
from util.tool.date_tool import curr_now
from util.tool.str_tool import md5Encode
from util.tool.http_tool import http_get, http_fetch


class InfraDataService(DataService):

    ipproxy = IpproxyCache()

    """对接网络请求服务"""

    @gen.coroutine
    def get_city_poi(self, q, region, tag, page_num, coord_type=3, page_size=10):
        """Place API 是一类简单的接口，用于返回查询某个区域的某类POI数据
        referer: http://lbsyun.baidu.com/index.php?title=webapi/guide/webservice-placeapi
        demo: http://api.map.baidu.com/place/v2/search?q=美食&region=杭州&output=json&ak=lSbGt6Z31wK9Pwi2GLUCx6ywLeflbjHf

        :param q: 检索关键字，周边检索和矩形区域内检索支持多个关键字并集检索，不同关键字间以$符号分隔，最多支持10个关键字检索。如:”银行$酒店”。
        :param region: 检索区域（市级以上行政区域），如果取值为“全国”或某省份，则返回指定区域的POI及数量
        :param tag: 关键词，可以使用城区，扩大 poi 搜索结果
        :param coord_type: 坐标类型，1（wgs84ll即GPS经纬度），2（gcj02ll即国测局经纬度坐标,火星坐标，高德地图坐标），3（bd09ll即百度经纬度坐标），4（bd09mc即百度米制坐标）
        :param page_num: 分页页码，默认为0,0代表第一页，1代表第二页，以此类推。
        :param page_size: 范围记录数量，默认为10条记录，最大返回20条。多关键字检索时，返回的记录数为关键字个数*page_size。
        :return json
        """
        params = ObjectDict({
            "region": region,
            "q": q,
            "tag": tag,
            "output": "json",
            "ak": settings['baidu_ak'],
            "coord_type": coord_type,
            "page_num": page_num,
            "page_size": page_size,
        })

        ret = yield http_get(route=path.BAIDU_WEBAPI_PLACE_POI_LIST,
                             jdata=params,
                             timeout=40)
        if ret:
            raise gen.Return(ret)
        else:
            raise gen.Return(ObjectDict())

    @gen.coroutine
    def get_dingda_nearby(self, longitude, latitude):

        """
        叮嗒出行，获得附近租赁点列表
        demo: http://bike-a.api.dingdatech.com/service/bicycle/stations?longitude=120.1457386954022&latitude=30.31722703827297
        :param longitude:
        :param latitude:
        :return:
        """

        try:
            params = ObjectDict({
                "longitude": longitude,
                "latitude": latitude,
            })

            host, port = yield self.get_ip_proxy()

            ret = yield http_get(path.DINGDA_NEARBY_LIST,
                                 params,
                                 headers=headers.DATA_SOURCE.dingda_app.header,
                                 timeout=30,
                                 proxy_host=host,
                                 proxy_port=port)

            if not ret:
                yield self.del_ip_proxy(host, port)
                raise gen.Return(ObjectDict())
            raise gen.Return(ret)
        except:
            yield self.del_ip_proxy(host, port)
            raise gen.Return(ObjectDict())

    @gen.coroutine
    def get_beijing_nearby(self, longitude, latitude):

        """
        北京公共自行车，获得附近租赁点列表
        demo:
        payload = "language=0&localLatitude=39.962947&localLongitude=116.416305&md5=uzpXelxfRBb4DyoCPhX4gg==&scale=1000&time=2017-02-07%2022%3A07%3A54"

        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'cookie': "JSESSIONID=1F1E59738AD63B96CAB53317DD732787",
            'user-agent': "mobileapp/1.0.4 (iPhone; iOS 10.2.1; Scale/2.00)clientVersion/iOS-1.0.4;clientType/bjbike_app",
            }

        conn.request("POST", "/bj_bicycleLease/query/queryStation.do", payload, headers)
        :param longitude:
        :param latitude:
        :return:
        """
        try:
            params = ObjectDict({
                "language": 0,
                "localLongitude": longitude,
                "localLatitude": latitude,
                "md5": md5Encode(str(latitude)),
                "scale": 1000,
                "time": curr_now()
            })

            host, port = yield self.get_ip_proxy()

            ret = yield http_fetch(path.BEIJING_NEARBY_LIST,
                                   params,
                                   headers=headers.DATA_SOURCE.beijing_app.header,
                                   timeout=30,
                                   proxy_host=host,
                                   proxy_port=port)
            if not ret:
                yield self.del_ip_proxy(host, port)
                raise gen.Return(ObjectDict())
            raise gen.Return(ret)
        except:
            yield self.del_ip_proxy(host, port)
            raise gen.Return(ObjectDict())

    @gen.coroutine
    def get_xian_nearby(self, longitude, latitude):

        """
        西安公共自行车，获得附近租赁点列表
        demo:
        payload = "longitude=108.91684&latitude=34.258907"

        headers = {
            'host': "bike.phioc.cn",
            'content-type': "application/x-www-form-urlencoded",
            'cookie': "PHPSESSID=abtgvitarmb8cgs85a1jcm1c63",
            'user-agent': "2.0.0 (iPhone; iOS 10.2.1; zh_CN)",
            'accept-encoding': "gzip",
            'cache-control': "no-cache",
            'postman-token': "487d8d8b-8946-40d4-5d38-12db68eb19c8"
            }

        conn.request("POST", "/api/get_around", payload, headers)
        :param longitude:
        :param latitude:
        :return:
        """
        try:
            params = ObjectDict({
                "longitude": longitude,
                "latitude": latitude,
            })

            host, port = yield self.get_ip_proxy()

            ret = yield http_fetch(path.XIAN_NEARBY_LIST,
                                   params,
                                   headers=headers.DATA_SOURCE.xian_app.header,
                                   timeout=30,
                                   proxy_host=host,
                                   proxy_port=port)
            if not ret:
                yield self.del_ip_proxy(host, port)
                raise gen.Return(ObjectDict())
            raise gen.Return(ret)
        except:
            yield self.del_ip_proxy(host, port)
            raise gen.Return(ObjectDict())

    @gen.coroutine
    def get_nanjing_list(self):

        """
        南京公共自行车，获得所有租赁点列表
        demo:
        conn = http.client.HTTPConnection("www.njlrsoft.cn")

        headers = {
            'cache-control': "no-cache",
            'postman-token': "f1780baa-95a0-91d8-6ce3-8d84bcd50a53"
            }

        conn.request("GET", "/bicycle/assets/js/site.json", headers=headers)
        :return:
        """

        ret = yield http_get(path.NANJING_LIST,
                             headers=headers.DATA_SOURCE.nanjing_wechat.header,
                             res_json=False,
                             timeout=30)
        ret = ret.decode('utf-8-sig') # 去除 dom 头
        if not ret:
            raise gen.Return(ObjectDict())
        else:
            raise gen.Return(ujson.decode(ret))