# coding=utf-8

from tornado import gen
from service.data.base import DataService

class UserDataService(DataService):

    @gen.coroutine
    def get_user(self, conds, fields=[]):

        if conds is None or not (isinstance(conds, dict) or isinstance(conds, str)):
            self.logger.warn("Warning:[get_user][invalid parameters], Detail:[conds: {0}, "
                        "type: {1}]".format(conds, type(conds)))
            raise gen.Return(False)

        if not fields:
            fields = self.user_dao.fields_map.keys()

        response = yield self.user_dao.get_record_by_conds(conds, fields)
        raise gen.Return(response)