# coding=utf-8

from tornado import gen

from service.data.base import DataService
from util.common import ObjectDict
from util.common.decorator import cache


class ScrapLogDataService(DataService):

    @gen.coroutine
    def get_scrap_log(self, conds, fields=None):

        fields = fields or []

        if conds is None or not (isinstance(conds, (dict, str))):
            self.logger.warn("Warning:[get_scrap_log][invalid parameters], Detail:[conds: {0}, "
                        "type: {1}]".format(conds, type(conds)))
            raise gen.Return(ObjectDict())

        if not fields:
            fields = list(self.scrap_log_dao.fields_map.keys())

        response = yield self.scrap_log_dao.get_record_by_conds(conds, fields)
        raise gen.Return(response)

    @gen.coroutine
    def add_scrap_log(self, fields, options=None):

        options = options or []

        if not fields or not isinstance(fields, dict):
            self.Log.warning("Warning:[add_scrap_log][invalid parameters], Detail:[fields: {0}, "
                        "type: {1}]".format(fields, type(fields)))
            raise gen.Return(False)

        response = yield self.scrap_log_dao.insert_record(fields, options)
        raise gen.Return(response)