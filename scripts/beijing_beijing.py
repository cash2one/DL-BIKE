# coding=utf-8

'''
:author pyx0622@gmail.com
:date 2016.08.13
:desc 北京公共自行车租赁点抓取脚本

    列表页地址：http://bjggzxc.btic.org.cn/Bicycle/views/wdStatus.html

    分城区列表页地址：wdList.html?areaid=0102

'''

from tornado import gen
from tornado.ioloop import IOLoop
from tornado.util import ObjectDict

import conf.common as const
import conf.headers as const_headers
from scripts.parser import Parser
from util.tool.http_tool import http_get

AREA_LIST = 'http://bjggzxc.btic.org.cn/Bicycle/views/wdStatus.html'
STATIONS_LIST = 'http://bjggzxc.btic.org.cn/Bicycle/BicycleServlet?action=GetBicycleStatus'


class BeijingParser(Parser):
    """
    北京租赁点抓取
    """

    @gen.coroutine
    def parse_html(self):
        source = yield http_get(route=AREA_LIST,
                                res_json=False,
                                headers=const_headers.BEIJING_HTML_HEADERS,
                                timeout=20)
        source = self.replace_white_within_span(str(source))
        source = self.remove_white_character(source)
        html = self.nbsp2space(source)

        beijing_list = self.parse_list(html)
        stations = yield self.parse_html_stations(beijing_list)
        print (stations)
        ret = yield self.update_station(stations)

        raise gen.Return(beijing_list)

    def parse_list(self, html):

        """
        解析 html 列表页
        :param html:
        :return:
        """
        area = ObjectDict()
        stations_list = self.get_all_value_from_html(
            r'<li><ahref=\"wdList\.html\?areaid=(.*?)\"title=\"(.*?)\"><div>.*?</div></a></li>', html)
        for item in stations_list:
            area[item[1]] = item[0]
        return area

    @gen.coroutine
    def parse_html_stations(self, area):

        """
        解析二级页面，获得每个租赁点
        :param area:
        :return:
        """
        stations = []

        for k, v in area.items():
            currentPage = 1
            length = 1
            while length > 0:
                data = {
                    "pageSize": 20,
                    "currentPage": currentPage,
                    "currentAreaid": v
                }
                stations_list = yield http_get(route=STATIONS_LIST,
                                               res_json=True,
                                               jdata=data,
                                               headers=const_headers.BEIJING_JSON_HEADERS,
                                               timeout=15)
                if not stations_list:
                    break

                for item in stations_list:
                    station = ObjectDict()
                    station['district'] = k
                    station['code'] = str(item.get('stationCode'))
                    station['type'] = item['type']
                    station['status'] = const.STATUS_INUSE if item['status'] == 2 else const.STATUS_UNUSE
                    station['total'] = item['bikesNum']
                    station['name'] = item['name']
                    station['address'] = item['adress']
                    station['district_id'] = item['countyCode']
                    station['longitude'] = item['bdLongitude']
                    station['latitude'] = item['bdLatitude']
                    station['telephone'] = item['name']
                    station['service_time'] = item['name']
                    stations.append(station)

                currentPage += 1
                length = len(stations_list)

            break

        raise gen.Return(stations)

    @gen.coroutine
    def update_station(self, stations):

        """
        增加或更新数据库中租赁点信息
        :param stations:
        :return:
        """
        for item in stations:
            station = yield self.station_ps.get_station({"code": item.get("code")})
            print (station)
            if station:
                # 存在，则更新
                print (1)
                pass

            else:
                # 不存在，则增加
                print (2)
                fields = ObjectDict({
                    "city_id":'',
                    "code": item.get("code", station.get("code"))
                })
                ret = yield self.station_ps.add_station(fields=fields)
                print (ret)

    def close(self):
        IOLoop.instance().stop()

    @gen.coroutine
    def runner(self):
        yield self.parse_html()
        self.close()


if __name__ == "__main__":
    jp = BeijingParser()
    jp.runner()
    IOLoop.instance().start()
