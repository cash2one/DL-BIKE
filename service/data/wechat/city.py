# coding=utf-8

from tornado import gen

from service.data.base import DataService
from util.common.decorator import cache
from util.common import ObjectDict


class CityDataService(DataService):

    @cache(ttl=60)
    @gen.coroutine
    def get_city(self, conds, fields=None):

        fields = fields or []

        if conds is None or not (isinstance(conds, (dict, str))):
            self.logger.warn("Warning:[get_city][invalid parameters], Detail:[conds: {0}, "
                        "type: {1}]".format(conds, type(conds)))
            raise gen.Return(ObjectDict())

        if not fields:
            fields = list(self.city_dao.fields_map.keys())

        response = yield self.city_dao.get_record_by_conds(conds, fields)
        raise gen.Return(response)