# coding=utf-8

from tornado import gen

from util.common.decorator import cache
from service.data.base import DataService


class ScrapLogDataService(DataService):

    @cache(ttl=60)
    @gen.coroutine
    def get_scrap_log(self, conds, fields=[]):

        if conds is None or not (isinstance(conds, dict) or isinstance(conds, str)):
            self.logger.warn("Warning:[get_scrap_log][invalid parameters], Detail:[conds: {0}, "
                        "type: {1}]".format(conds, type(conds)))
            raise gen.Return(False)

        if not fields:
            fields = self.scrap_log_dao.fields_map.keys()

        response = yield self.scrap_log_dao.get_record_by_conds(conds, fields)
        raise gen.Return(response)