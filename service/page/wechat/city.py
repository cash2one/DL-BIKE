# coding=utf-8

from tornado import gen
from service.page.base import PageService

class CityPageService(PageService):

    @gen.coroutine
    def get_city(self, conds, fields=None):

        '''
        获得城市信息
        :param conds:
        :param fields: 示例:
        conds = {
            "cid": cid
        }
        :return:
        '''

        city = yield self.city_ds.get_city(conds, fields)
        raise gen.Return(city)