# coding=utf-8

from tornado import gen

import conf.path as path
from setting import settings
from service.data.base import DataService
from util.common import ObjectDict
from util.common.decorator import cache
from util.tool.http_tool import http_get, http_post


class WechatDataService(DataService):

    """微信 Api服务"""

    @cache(ttl=60*60)
    @gen.coroutine
    def get_access_token(self, appid, appsecret):
        """开发者模式，获得公众号 access_token

        :param appid:
        :param appsecret:
        :return json
        """

        ret = yield http_get(route=path.WECHAT_ACCESS_TOKEN.format(appid, appsecret), timeout=5)
        if ret:
            raise gen.Return(ret)
        else:
            raise gen.Return(ObjectDict())

    @gen.coroutine
    def get_userinfo(self, openid, appid, appsecret):
        """
        获得微信用户信息
        :param openid:
        :return:
        """
        access_token_res = yield self.get_access_token(appid, appsecret)
        ret = yield http_get(route=path.WECHAT_USER_INFO.format(access_token_res.access_token, openid), timeout=5)
        if ret:
            raise gen.Return(ret)
        else:
            raise gen.Return(ObjectDict())

    @gen.coroutine
    def send_template(self, appid, appsecret, touser, template_id, url, data, topcolor ='#7B68EE'):
        """
        发送消息模板
        :param touser:
        :param template_id:
        :param url:
        :param data:
        :param topcolor:
        :return:
        """

        template = ObjectDict({
            "touser": touser,
            "template_id": template_id,
            "url": url,
            "topcolor": topcolor,
            "data": data,
        })
        access_token_res = yield self.get_access_token(appid, appsecret)
        ret = yield http_post(path.WECHAT_TEMPALTE.format(access_token_res.access_token), template)
        if ret:
            raise gen.Return(ret)
        else:
            raise gen.Return(ObjectDict())

    @gen.coroutine
    def send_custom(self, jdata):
        """
        发送客服消息 https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1421140547&token=&lang=zh_CN
        :return:
        """

        access_token_res = yield self.get_access_token(settings['hztrip_appid'], settings['hztrip_appsecret'])
        ret = yield http_post(path.WX_CUSTOM_SEND.format(access_token_res.access_token), jdata)
        raise gen.Return(ret)