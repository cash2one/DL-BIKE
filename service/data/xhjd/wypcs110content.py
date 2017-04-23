# coding=utf-8

from tornado import gen

from service.data.base import DataService
from util.common.decorator import cache
from util.common import ObjectDict


class Wypcs110ContentDataService(DataService):

    @cache(ttl=60)
    @gen.coroutine
    def get_wypcs110content(self, conds, fields=None):

        fields = fields or []

        if conds is None or not (isinstance(conds, (dict, str))):
            self.logger.warn("Warning:[get_wypcs110content][invalid parameters], Detail:[conds: {0}, "
                        "type: {1}]".format(conds, type(conds)))
            raise gen.Return(ObjectDict())

        if not fields:
            fields = list(self.wypcs110content_dao.fields_map.keys())

        response = yield self.wypcs110content_dao.get_record_by_conds(conds, fields)
        raise gen.Return(response)

    @gen.coroutine
    def add_wypcs110content(self, fields, options=None):

        options = options or []

        if not fields or not isinstance(fields, dict):
            self.Log.warning("Warning:[add_wypcs110content][invalid parameters], Detail:[fields: {0}, "
                        "type: {1}]".format(fields, type(fields)))
            raise gen.Return(False)

        response = yield self.wypcs110content_dao.insert_record(fields, options)
        raise gen.Return(response)