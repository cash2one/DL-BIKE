# coding=utf-8

from tornado import gen
from service.page.base import PageService

class StationPageService(PageService):

    @gen.coroutine
    def get_station(self, conds, fields=[]):

        '''
        获得城市信息
        :param conds:
        :param fields: 示例:
        conds = {
            "id": company_id
        }
        :return:
        '''

        station = yield self.station_ds.get_station(conds, fields)

        raise gen.Return(station)