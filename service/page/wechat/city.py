# coding=utf-8

from tornado import gen
from service.page.base import PageService

class CityPageService(PageService):

    @gen.coroutine
    def get_city(self, conds, fields=[]):

        '''
        获得城市信息
        :param conds:
        :param fields: 示例:
        conds = {
            "id": company_id
        }
        :return:
        '''

        city = yield self.city_ds.get_city(conds, fields)

        raise gen.Return(city)