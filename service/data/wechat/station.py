# coding=utf-8

from tornado import gen
from service.data.base import *

class StationDataService(DataService):

    @cache(ttl=60)
    @gen.coroutine
    def get_station(self, conds, fields=[]):

        if conds is None or not (isinstance(conds, dict) or isinstance(conds, str)):
            self.logger.warn("Warning:[get_station][invalid parameters], Detail:[conds: {0}, "
                        "type: {1}]".format(conds, type(conds)))
            raise gen.Return(False)

        if not fields:
            fields = self.station_dao.fields_map.keys()

        response = yield self.station_dao.get_record_by_conds(conds, fields)
        raise gen.Return(response)

    @cache(ttl=60)
    @gen.coroutine
    def get_stations_list(self, conds, fields, options=[], appends=[], index='', params=[]):

        if conds is None or not (isinstance(conds, dict) or isinstance(conds, str)):
            self.logger.warn("Warning:[get_stations_list][invalid parameters], Detail:[conds: {0}, "
                        "type: {1}]".format(conds, type(conds)))
            raise gen.Return(False)

        if not fields:
            fields = self.station_dao.fields_map.keys()

        response = yield self.station_dao.get_list_by_conds(conds, fields, options, appends, index, params)
        raise gen.Return(response)