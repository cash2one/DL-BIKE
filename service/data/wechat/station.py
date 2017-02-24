# coding=utf-8

from tornado import gen

from util.common.decorator import cache
from service.data.base import DataService
from util.common import ObjectDict


class StationDataService(DataService):

    @gen.coroutine
    def get_station(self, conds, fields=None):

        fields = fields or []

        if conds is None or not (isinstance(conds, (dict, str))):
            self.logger.warn("Warning:[get_station][invalid parameters], Detail:[conds: {0}, "
                        "type: {1}]".format(conds, type(conds)))
            raise gen.Return(ObjectDict())

        if not fields:
            fields = list(self.station_dao.fields_map.keys())

        response = yield self.station_dao.get_record_by_conds(conds, fields)
        raise gen.Return(response)

    @gen.coroutine
    def get_stations_list(self, conds, fields, options=None, appends=None, index='', params=None):

        options = options or []
        appends = appends or []
        params = params or []

        if conds is None or not (isinstance(conds, (dict, str))):
            self.logger.warn("Warning:[get_stations_list][invalid parameters], Detail:[conds: {0}, "
                        "type: {1}]".format(conds, type(conds)))
            raise gen.Return(list())

        if not fields:
            fields = list(self.station_dao.fields_map.keys())

        response = yield self.station_dao.get_list_by_conds(conds, fields, options, appends, index, params)
        raise gen.Return(response)

    @gen.coroutine
    def add_station(self, fields, options=None):

        options = options or []

        if not fields or not isinstance(fields, dict):
            self.Log.warning("Warning:[add_station][invalid parameters], Detail:[fields: {0}, "
                        "type: {1}]".format(fields, type(fields)))
            raise gen.Return(False)

        response = yield self.station_dao.insert_record(fields, options)
        raise gen.Return(response)

    @gen.coroutine
    def update_station(self, conds, fields, options=None, appends=None):

        options = options or []
        appends = appends or []

        if not fields or not isinstance(fields, dict):
            self.Log.warning("Warning:[update_station][invalid parameters], Detail:[fields: {0}, "
                        "type: {1}]".format(fields, type(fields)))
            raise gen.Return(False)

        response = yield self.station_dao.update_by_conds(conds, fields, options, appends)
        raise gen.Return(response)