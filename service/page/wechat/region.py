# coding=utf-8

from tornado import gen
from service.page.base import PageService

class RegionPageService(PageService):

    @gen.coroutine
    def get_region(self, conds, fields=None):

        '''
        获得多级城市信息
        :param conds:
        :param fields: 示例:
        conds = {
            "rid": rid
        }
        :return:
        '''

        city = yield self.region_ds.get_region(conds, fields)
        raise gen.Return(city)

    @gen.coroutine
    def get_regions(self, conds, fields=None, options=None, appends=None):

        '''
        获得多级城市列表信息
        :param conds:
        :param fields: 示例:
        conds = {
            "rid": rid
        }
        :return:
        '''

        city = yield self.region_ds.get_regions(conds, fields, options, appends)
        raise gen.Return(city)