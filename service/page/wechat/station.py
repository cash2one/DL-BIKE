# coding=utf-8

from tornado import gen
from service.page.base import PageService

class StationPageService(PageService):

    @gen.coroutine
    def get_station(self, conds, fields=None):
        """
        获得租赁点信息
        :param conds:
        :param fields: 示例:
        conds = {
            "id": company_id
        }
        :return:
        """

        station = yield self.station_ds.get_station(conds, fields)
        raise gen.Return(station)

    @gen.coroutine
    def add_station(self, fields, options=None):
        """
        增加租赁点
        :param fields:
        :param options:
        :return:
        """

        res = yield self.station_ds.add_station(fields, options)
        raise gen.Return(res)

    @gen.coroutine
    def update_station(self, conds, fields, options=None, appends=None):
        """
        更新租赁点信息
        :param conds:
        :param fields:
        :param options:
        :param appends:
        :return:
        """

        res = yield self.station_ds.update_station(conds, fields, options, appends)
        raise gen.Return(res)