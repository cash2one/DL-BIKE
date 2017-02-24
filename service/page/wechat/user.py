# coding=utf-8

from tornado import gen
from service.page.base import PageService

class UserPageService(PageService):

    @gen.coroutine
    def get_user(self, conds, fields=None):

        '''
        获得用户信息
        :param conds:
        :param fields: 示例:
        conds = {
            "id": company_id
        }
        :return:
        '''

        user = yield self.user_ds.get_user(conds, fields)
        raise gen.Return(user)