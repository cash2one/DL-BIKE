# coding=utf-8

from tornado import gen
from service.page.base import PageService

class UserPageService(PageService):

    @gen.coroutine
    def get_user(self, conds, fields=[]):

        '''
        获得城市信息
        :param conds:
        :param fields: 示例:
        conds = {
            "id": company_id
        }
        :return:
        '''
        # 
        # company = yield self.hr_company_ds.get_company(conds, fields)
        # 
        # raise gen.Return(company)