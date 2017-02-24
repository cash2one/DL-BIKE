# coding=utf-8

import random
import ujson
from tornado import gen

import conf.path as path
import conf.headers as headers
from setting import settings
from service.data.base import DataService
from util.common import ObjectDict
from util.common.decorator import cache
from util.tool.date_tool import curr_now
from util.tool.str_tool import md5Encode, to_str
from util.tool.http_tool import http_get, http_post, http_put, http_delete, http_patch, http_fetch


class InfraDataService(DataService):

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
            "ak": settings.baidu_ak,
            "coord_type": coord_type,
            "page_num": page_num,
            "page_size": page_size,
        })

        ret = yield http_get(path.BAIDU_WEBAPI_PLACE_POI_LIST, params)
        raise gen.Return(ret)

    @gen.coroutine
    def get_dingda_nearby(self, longitude, latitude):

        """
        叮嗒出行，获得附近租赁点列表
        demo: http://bike-a.api.dingdatech.com/service/bicycle/stations?longitude=120.1457386954022&latitude=30.31722703827297
        :param longitude:
        :param latitude:
        :return:
        """

        params = ObjectDict({
            "longitude": longitude,
            "latitude": latitude,
        })

        ip_proxys = yield self.get_ip_proxy()
        ip_proxy = ip_proxys[random.randint(0,19)]
        print (ip_proxy)

        ret = yield http_get(path.DINGDA_NEARBY_LIST, params, headers=headers.DINGDA_NEARBY_HEADERS, timeout=30,
                             proxy_host=ip_proxy.get("host"), proxy_port=ip_proxy.get("port"))

        if not ret:
            yield self.del_ip_proxy(ip_proxy.get("host"))
            raise gen.Return(ObjectDict())

        raise gen.Return(ret)

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

        params = ObjectDict({
            "language": 0,
            "localLongitude": longitude,
            "localLatitude": latitude,
            "md5": md5Encode(str(latitude)),
            "scale": 1000,
            "time": curr_now()
        })

        ip_proxys = yield self.get_ip_proxy()
        ip_proxy = ip_proxys[random.randint(0,19)]
        print (ip_proxy)

        ret = yield http_fetch(path.BEIJING_NEARBY_LIST, params, headers=headers.BEIJING_NEARBY_HEADERS, timeout=30,
                               proxy_host=ip_proxy.get("host"), proxy_port=ip_proxy.get("port"))
        if not ret:
            yield self.del_ip_proxy(ip_proxy.get("host"))
            raise gen.Return(ObjectDict())

        raise gen.Return(ret)

    @cache(ttl=600, key="get_ip_proxy", hash=False)
    @gen.coroutine
    def get_ip_proxy(self, count=20, types=0, protocol=1, country='国内'):
        """
        获得代理 IP
        referer: https://github.com/qiyeboy/IPProxyPool
        http://127.0.0.1:8000/?types=0&protocol=1&count=10&country=国内
        :param count: 数量
        :param types: 0: 高匿,1:匿名,2 透明
        :param protocol: 0: http, 1 https, 2 http/https
        :param country: 取值为国内, 国外
        :return:
        """

        params = ObjectDict({
            "types": types,
            "protocol": protocol,
            "count": count,
            "country": country
        })

        ret = yield http_get(path.IP_PROXY_GET, params, res_json=False)
        res_list = list()
        ret = ujson.decode(to_str(ret))

        for item in ret:
            ip_dict = ObjectDict({
                "host": item[0],
                "port": item[1],
                "score": item[2]
            })
            res_list.append(ip_dict)

        raise gen.Return(res_list)

    @gen.coroutine
    def del_ip_proxy(self, ip):
        """
        删除代理 IP
        referer: https://github.com/qiyeboy/IPProxyPool
        http://127.0.0.1:8000/delete?ip=111.40.84.73
        :param ip: 类似192.168.1.1
        :return:
        """

        params = ObjectDict({
            "ip": ip,
        })

        print ("!!!!!!!!!!del_ip_proxy!!!!!!!!!!!!!!!!")
        ret = yield http_get(path.IP_PROXY_DELETE, params, res_json=False)
        print (ret)
        res = self.redis.delete("DLBike_infra:get_ip_proxy:get_ip_proxy", prefix=False)
        print (res)
        raise gen.Return(ret)