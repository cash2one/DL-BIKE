# coding=utf-8

import re
from app import logger
import conf.common as const
from service.page.wechat.city import CityPageService
from service.page.wechat.scrap_log import ScrapLogPageService
from service.page.wechat.station import StationPageService
from service.page.wechat.user import UserPageService
from service.page.wechat.infra import InfraPageService
from service.page.wechat.region import RegionPageService

class Parser():

    def __init__(self):
        self.city_ps = CityPageService()
        self.scraplog_ps = ScrapLogPageService()
        self.station_ps = StationPageService()
        self.user_ps = UserPageService()
        self.infra_ps = InfraPageService()
        self.region_ps = RegionPageService()
        self.logger = logger
        self.const = const

    def rhtml(self, html):
        p = re.compile('<[^>]+>')
        return p.sub('', html)

    def rline(self, html):
        p = re.compile('\n+')
        return p.sub('', html)

    def rtab(self, html):
        p = re.compile('\t+')
        return p.sub('', html)

    def nbsp2space(self, s):
        p = re.compile('&nbsp;')
        return p.sub(' ', s)

    def remove_all_html_label(self, s):
        startp = re.compile(r'<.*?>')
        s = startp.sub('', s)
        endp = re.compile(r'</.*?>')
        return endp.sub('', s)

    def get_nospace_str(self, html, i):
        r = re.compile(r"\S*")
        res = re.findall(r, html)
        if len(res) > i:
            return res[i]
        return ''

    def get_value_from_list(self, l, i, default=''):
        if len(l) > i:
            return l[i]
        else:
            return default

    def get_value_from_html(self, r, html, index=0, default=''):
        l = re.findall(r, html)
        if l:
            return self.get_value_from_list(l, index)
        return default

    def get_all_value_from_html(self, r, html):
        return re.findall(r, html)

    def get_compiled_value_from_html(self, r, html, idx=0):
        recomp = re.compile(r)
        find_res = re.findall(recomp, html)
        if len(find_res) > idx:
            return find_res[idx]
        return ''

    def remove_white_character(self, txt):
        p = re.compile('\s*')
        return p.sub('', txt)

    def replace_white_within_span(self, txt):

        '''
        替换span标签中的空格，换成&nbsp;
        :param html:
        :return:
        '''

        span_list = re.findall(r'<span.*?>(.*?)</span>', txt, re.S)
        for span in span_list:
            span = span.strip()
            span_new = span.replace(' ','&nbsp;')
            txt = txt.replace(span,span_new)
        return txt