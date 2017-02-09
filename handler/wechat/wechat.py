# coding=utf-8

import hashlib
from tornado import gen
from handler.base import BaseHandler
from util.common.decorator import handle_response
from util.tool.http_tool import http_get


class WechatHandler(BaseHandler):

    @handle_response
    @gen.coroutine
    def get(self, *args, **kwargs):
        """
        公众平台接入
        :param args:
        :param kwargs:
        :return:
        """

        html = yield http_get(route='http://bjggzxc.btic.org.cn/Bicycle/views/wdStatus.html', timeout=10)
        # print (html)

        self.logger.debug("com: %s" % self.constant.BEIJING_JSON_HEADERS)

        self.send_json_success({
            "hai": 1,
            "html": html
        })
        # if self.get_argument("echostr", "") and self._verify_wexin_request():
        #     ret = self.get_argument("echostr", "", True)
        #     self.write(ret)

    def _verify_wexin_request(self):
        signature = self.get_argument("signature")
        timestamp = self.get_argument("timestamp")
        nonce = self.get_argument("nonce")
        # id = self.get_argument("id")
        #
        # token = self.db.get(
        #     "SELECT token FROM hr_wx_wechat "
        #     "WHERE id = %s", id)
        token = "cd717d02a93d11e5a2be00163e004a1f"

        hashstr = hashlib.sha1(
            "".join(sorted([token, timestamp, nonce]))).hexdigest()

        return hashstr == signature
