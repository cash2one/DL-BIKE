# coding=utf-8

from tornado import gen

from service.data.base import DataService
from util.common.decorator import cache
from util.common import ObjectDict


class RegionDataService(DataService):

    @cache(ttl=60)
    @gen.coroutine
    def get_region(self, conds, fields=None):

        fields = fields or []

        if conds is None or not (isinstance(conds, (dict, str))):
            self.logger.warn("Warning:[get_region][invalid parameters], Detail:[conds: {0}, "
                        "type: {1}]".format(conds, type(conds)))
            raise gen.Return(ObjectDict())

        if not fields:
            fields = list(self.region_dao.fields_map.keys())

        response = yield self.region_dao.get_record_by_conds(conds, fields)
        raise gen.Return(response)

    @cache(ttl=60)
    @gen.coroutine
    def get_regions(self, conds, fields, options=None, appends=None, index='', params=None):

        options = options or []
        appends = appends or []
        params = params or []

        if conds is None or not (isinstance(conds, (dict, str))):
            self.logger.warn("Warning:[get_stations_list][invalid parameters], Detail:[conds: {0}, "
                        "type: {1}]".format(conds, type(conds)))
            raise gen.Return(list())

        if not fields:
            fields = list(self.region_dao.fields_map.keys())

        response = yield self.region_dao.get_list_by_conds(conds, fields, options, appends, index, params)
        raise gen.Return(response)