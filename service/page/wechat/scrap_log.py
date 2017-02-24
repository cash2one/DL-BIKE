# coding=utf-8

from tornado import gen
from service.page.base import PageService

class ScrapLogPageService(PageService):

    @gen.coroutine
    def get_scrap_log(self, conds, fields=None):

        '''
        获得抓取 log
        :param conds:
        :param fields: 示例:
        conds = {
            "id": company_id
        }
        :return:
        '''

        scrap_log = yield self.scrap_log_ds.get_scrap_log(conds, fields)
        raise gen.Return(scrap_log)

    @gen.coroutine
    def add_scrap_log(self, fields, options=None):
        """
        增加scrap_log
        :param fields:
        :param options:
        :return:
        """

        res = yield self.scrap_log_ds.add_scrap_log(fields, options)
        raise gen.Return(res)