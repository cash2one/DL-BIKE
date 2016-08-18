# coding=utf-8

'''
:author pyx0622@gmail.com
:date 2016.08.13
:desc 北京公共自行车租赁点抓取脚本

    列表页地址：http://bjggzxc.btic.org.cn/Bicycle/views/wdStatus.html

    分城区列表页地址：wdList.html?areaid=0102


'''
import ujson
from tornado.util import ObjectDict
from tornado.ioloop import IOLoop
from tornado import gen
import conf.common as const
from utils.tool.http_tool import http_get
from utils.parse.parser import Parser

AREA_LIST = 'http://bjggzxc.btic.org.cn/Bicycle/views/wdStatus.html'
STATIONS_LIST = 'http://bjggzxc.btic.org.cn/Bicycle/BicycleServlet?action=GetBicycleStatus'

class BeijingParser(Parser):

    """
    北京租赁点抓取
    """


    # def get_li_h4_value_from_section(self, html, h=''):
    #     re_li = h+r'<li><h4>(.*?)</h4>'
    #     return self.get_value_from_html(re_li, html)
    #
    # def get_section_value(self, k, html):
    #     re_section = r'<section><h3><span>' + k + r'(.*?)</section>'
    #     return self.get_value_from_html(re_section, html)
    #
    #
    #
    # def get_time_time_str_title(self, html):
    #     html = self.get_li_h4_value_from_section(html)
    #     re_t = r"([0-9.\w]*)[^\s]?\s*([^\s]*)\s*(.*)"
    #     return self.get_value_from_html(re_t, html, default=('', '', ''))
    #
    # def get_str_time_time_title(self, html):
    #     html = self.get_li_h4_value_from_section(html)
    #     re_t = r"([^\s]*)\s*([0-9.\w]*)(.*)"
    #     return self.get_value_from_html(re_t, html, default=('', '', ''))
    #
    # def get_sub_content(self, html):
    #     re_t = r'(^</li><li><h4>.*?</li><li><h4>|</li><li><h4>.*?</li><li>)'
    #     return self.get_all_value_from_html(re_t, html)
    #
    # def get_remark(self, k, html):
    #     re_remark = k + "</span></h3><divclass=\"preview-content\">(.*?)</div>"
    #     return self.get_value_from_html(re_remark, html, default='')

    @gen.coroutine
    def parse_html(self):
        source = yield http_get(route=AREA_LIST, headers=const.BEIJING_HTML_HEADERS)
        source = self.replace_white_within_span(source)
        source = self.remove_white_character(source)
        html = self.nbsp2space(source)

        beijing_list = self.parse_list(html)
        print (beijing_list)
        stations = yield self.parse_stations(beijing_list)

        raise gen.Return(beijing_list)

    def parse_list(self, html):
        area = ObjectDict()
        stations_list = self.get_all_value_from_html(r'<li><ahref=\"wdList\.html\?areaid=(.*?)\"title=\"(.*?)\"><div>.*?</div></a></li>', html)
        for item in stations_list:
            area[item[1]] = item[0]
        return area

    @gen.coroutine
    def parse_stations(self, area):
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
                print (data)
                stations_list = yield http_get(route=STATIONS_LIST, jdata=data, headers=const.BEIJING_JSON_HEADERS)
                stations_list = ujson.decode(stations_list)
                if not stations_list:
                    break

                print (stations_list)

                for item in stations_list:
                    print (item)
                    station = ObjectDict()
                    station['district'] = k
                    station['code'] = item.get('stationCode')
                    station['type'] = item['type']
                    station['status'] = const.STATUS_ONUSE if item['status'] == 2 else const.STATUS_UNUSE
                    station['total'] = item['bikesNum']
                    station['name'] = item['name']
                    station['address'] = item['adress']
                    station['district_id'] = item['countyCode']
                    station['longitude'] = item['bdLongitude']
                    station['latitude'] = item['bdLatitude']
                    station['telephone'] = item['name']
                    station['service_time'] = item['name']
                    stations.append(station)

                currentPage = currentPage + 1
                length = len(stations_list)



        raise gen.Return(stations)

    def close(self):
        IOLoop.instance().stop()
        # self.db.close()

    @gen.coroutine
    def runner(self):
        yield self.parse_html()
        self.close()

if __name__ == "__main__":

    jp = BeijingParser()
    jp.runner()
    IOLoop.instance().start()



