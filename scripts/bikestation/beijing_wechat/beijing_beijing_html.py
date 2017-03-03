# coding=utf-8

'''
:author pyx0622@gmail.com
:date 2016.08.13
:desc 北京公共自行车租赁点抓取脚本

    列表页地址：http://bjggzxc.btic.org.cn/Bicycle/views/wdStatus.html

    分城区列表页地址：wdList.html?areaid=0102

'''
import random
import time
import traceback

from tornado import gen
from tornado.ioloop import IOLoop
from tornado.util import ObjectDict

import conf.headers as const_headers
from scripts.parser import Parser
from util.tool.http_tool import http_get
from util.tool.str_tool import to_str

AREA_LIST = 'http://bjggzxc.btic.org.cn/Bicycle/views/wdStatus.html'
STATIONS_LIST = 'http://bjggzxc.btic.org.cn/Bicycle/BicycleServlet?action=GetBicycleStatus'
# 北京
CITY_ID = 1
SID = 2


class BeijingParser(Parser):
    """
    北京租赁点抓取
    """

    @gen.coroutine
    def parse_html(self):
        try:
            source = yield http_get(route=AREA_LIST,
                                    res_json=False,
                                    headers=const_headers.DATA_SOURCE.beijing_wechat.header_html,
                                    timeout=20)
            source = self.replace_white_within_span(to_str(source))
            source = self.remove_white_character(source)
            html = self.nbsp2space(source)

            beijing_list = self.parse_list(to_str(html))
            print (beijing_list)
            yield self.parse_html_stations(beijing_list)
        except Exception as e:
            self.logger.error(traceback.format_exc())
            # 增加抓取记录 log
            yield self.scraplog_ps.add_scrap_log(fields={
                "cid": CITY_ID,
                "status": self.const.STATUS_UNUSE,
            })

    @gen.coroutine
    def get_regions(self, rname):
        regions = yield self.region_ps.get_regions(conds={
            "cid": CITY_ID,
            "rname": rname,
        })
        raise gen.Return(regions)


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
                                               headers=const_headers.DATA_SOURCE.beijing_wechat.header_json,
                                               timeout=40)
                region = yield self.get_regions(k)

                if stations_list:
                    for item in stations_list:
                        if not isinstance(item, dict):
                            break
                        station = ObjectDict()
                        station['code'] = str(item.get('stationCode'))
                        station['status'] = self.const.STATUS_INUSE if item['status'] == 2 else self.const.STATUS_UNUSE
                        # station['type'] = item['type']  暂时不清楚含义
                        station['total'] = int(item['bikesNum'])
                        station['name'] = item['name']
                        station['address'] = item['adress']
                        station['district'] = region.rname,
                        station['district_id'] = region.rid,
                        station['longitude'] = item['bdLongitude']
                        station['latitude'] = item['bdLatitude']
                        # station['service_time'] = ""
                        # station['is_24'] = ""
                        # station['is_duty'] = ""
                        print (station)
                        yield self.update_station(station)

                currentPage += 1
                length = len(stations_list) if stations_list is not None else 0
                x = int(random.random() * 10)
                print (x)
                yield self.async_sleep(x)

        raise gen.Return(True)

    @gen.coroutine
    def update_station(self, item):

        """
        增加或更新数据库中租赁点信息
        :param stations:
        :return:
        """
        station = yield self.station_ps.get_station({
            "code": item.code,
            "cid": CITY_ID,
            "sid": SID,
        })
        if station:
            # 存在，则更新
            self.station_ps.update_station(
                conds={
                    "id": station.id
                },
                fields={
                    "status": item.status,
                    "total": item.total,
                    "name": item.name,
                    "address": item.address,
                    "district": item.district,
                    "district_id": item.district_id,
                    "longitude": item.longitude,
                    "latitude": item.latitude
                }
            )
        else:
            # 不存在，则增加
            yield self.station_ps.add_station(fields={
                "cid": CITY_ID,
                "sid": SID,
                "code": item.code,
                "status": item.status,
                "total": item.total,
                "name": item.name,
                "address": item.address,
                "district": item.district,
                "district_id": item.district_id,
                "longitude": item.longitude,
                "latitude": item.latitude
            })

    @gen.coroutine
    def async_sleep(self, timeout):
        # Sleep without blocking the IOLoop
        yield gen.Task(IOLoop.instance().add_timeout, time.time() + timeout)

    def close(self):
        IOLoop.instance().stop()
        # 增加抓取记录 log
        yield self.scraplog_ps.add_scrap_log(fields={
            "cid": CITY_ID,
            "status": self.const.STATUS_INUSE,
        })

    @gen.coroutine
    def runner(self):
        yield self.parse_html()
        self.close()


if __name__ == "__main__":
    jp = BeijingParser()
    jp.runner()
    IOLoop.instance().start()
