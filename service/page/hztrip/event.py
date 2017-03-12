# coding=utf-8

# @Time    : 3/12/17 16:53
# @Author  : panda (panyuxin@moseeker.com)
# @File    : event.py
# @DES     :

from tornado import gen

from service.page.base import PageService

class EventPageService(PageService):

    def __init__(self):
        super().__init__()

    @gen.coroutine
    def opt_default(self, msg, nonce, wechat):
        """被动回复用户消息的总控处理
        referer: https://mp.weixin.qq.com/wiki?action=doc&id=mp1421140543&t=0.5116553557196903
        :param msg: 消息
        :param nonce:
        :param wechat:
        :return:
        """

        pass

        # rule = yield self.hr_wx_rule_ds.get_wx_rule(conds={
        #     "wechat_id": wechat.id,
        #     "id": wechat.default,
        # })
        #
        # if rule:
        #     res = yield getattr(self, "rep_{}".format(rule.module))(msg, rule.id, nonce, wechat)
        #     raise gen.Return(res)
        # else:
        #     raise gen.Return("")