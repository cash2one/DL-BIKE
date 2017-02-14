# coding=utf-8

from tornado import gen
from service.page.base import PageService

class ScrapLogPageService(PageService):

    @gen.coroutine
    def get_scrap_log(self, conds, fields=[]):

        '''
        获得城市信息
        :param conds:
        :param fields: 示例:
        conds = {
            "id": company_id
        }
        :return:
        '''

        scrap_log = yield self.scrap_log_ds.get_scrap_log(conds, fields)

        raise gen.Return(scrap_log)