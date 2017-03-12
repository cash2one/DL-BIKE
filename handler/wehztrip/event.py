# coding=utf-8

# @Time    : 2/6/17 09:03
# @Author  : panda (panyuxin@moseeker.com)
# @File    : event.py
# @DES     : 杭州公共出行微信公众号消息交互

# Copyright 2016 MoSeeker

import traceback
from tornado import gen

from handler.metabase import MetaBaseHandler
from util.common import ObjectDict
from util.tool.xml_tool import parse_msg
from util.wechat.msgcrypt import SHA1


class WechatOauthHandler(MetaBaseHandler):

    """开发者模式"""

    def __init__(self, application, request, **kwargs):
        super(WechatOauthHandler, self).__init__(application, request, **kwargs)

        self.msg = None

    def check_xsrf_cookie(self):
        return True

    @gen.coroutine
    def prepare(self):
        self.msg = self.get_msg()

        user = ObjectDict()
        openid = self.msg.get('FromUserName', '')
        user.openid = openid
        self.current_user = user

    @gen.coroutine
    def get(self):
        echostr = self.params.echostr
        if echostr and self.verification():
            self.write(echostr)
        else:
            self.send_xml()

    @gen.coroutine
    def post(self):

        self.logger.debug("oauth: %s" % self.request.uri)
        self.logger.debug("oauth msg: %s" % self.msg)
        self.logger.debug("oauth params: %s" % self.params)
        self.logger.debug("oauth current_user: %s" % self.current_user)
        self.logger.debug(
            "++++++WECHAT START++++++++++++++++++++++++++++++++++++++\n")

        try:
            msg_type = self.msg['MsgType']
            if self.verification():
                yield getattr(self, 'post_' + msg_type)()
            else:
                self.logger.error(
                    "[wechat_oauth]verification failed:{}".format(
                        self.msg))
        except Exception as e:
            self.logger.error(traceback.format_exc())

    @gen.coroutine
    def post_verify(self):
        self.send_xml()

    # @gen.coroutine
    # def post_text(self):
    #     """文本消息, referer: https://mp.weixin.qq.com/wiki?action=doc&id=mp1421140453&t=0.33078310940365907"""
    #     res = yield self.event_ps.opt_text(self.msg, self.params.nonce, self.wechat)
    #     self.send_xml(res)
    #
    # @gen.coroutine
    # def post_image(self):
    #     """图片消息, referer: https://mp.weixin.qq.com/wiki?action=doc&id=mp1421140453&t=0.33078310940365907"""
    #     res = yield self.event_ps.opt_default(self.msg, self.params.nonce, self.wechat)
    #     self.send_xml(res)
    #
    # @gen.coroutine
    # def post_voice(self):
    #     """语音消息, referer: https://mp.weixin.qq.com/wiki?action=doc&id=mp1421140453&t=0.33078310940365907"""
    #     res = yield self.event_ps.opt_default(self.msg, self.params.nonce, self.wechat)
    #     self.send_xml(res)
    #
    # @gen.coroutine
    # def post_video(self):
    #     """视频消息, referer: https://mp.weixin.qq.com/wiki?action=doc&id=mp1421140453&t=0.33078310940365907"""
    #     res = yield self.event_ps.opt_default(self.msg, self.params.nonce, self.wechat)
    #     self.send_xml(res)
    #
    # @gen.coroutine
    # def post_shortvideo(self):
    #     """小视屏消息, referer: https://mp.weixin.qq.com/wiki?action=doc&id=mp1421140453&t=0.33078310940365907"""
    #     res = yield self.event_ps.opt_default(self.msg, self.params.nonce, self.wechat)
    #     self.send_xml(res)
    #
    # @gen.coroutine
    # def post_location(self):
    #     """地理位置消息, referer: https://mp.weixin.qq.com/wiki?action=doc&id=mp1421140453&t=0.33078310940365907"""
    #     res = yield self.event_ps.opt_default(self.msg, self.params.nonce, self.wechat)
    #     self.send_xml(res)
    #
    # @gen.coroutine
    # def post_link(self):
    #     """链接消息, referer: https://mp.weixin.qq.com/wiki?action=doc&id=mp1421140453&t=0.33078310940365907"""
    #     res = yield self.event_ps.opt_default(self.msg, self.params.nonce, self.wechat)
    #     self.send_xml(res)
    #
    # @gen.coroutine
    # def post_event(self):
    #     """微信事件, referer: https://mp.weixin.qq.com/wiki?action=doc&id=mp1421140454&t=0.6181039380535693"""
    #     event = self.msg['Event']
    #     yield getattr(self, 'event_' + event)()
    #
    # @gen.coroutine
    # def event_subscribe(self):
    #     """关注事件"""
    #     res = yield self.event_ps.opt_event_subscribe(self.msg, self.current_user, self.params.nonce)
    #     self.send_xml(res)
    #
    # @gen.coroutine
    # def event_unsubscribe(self):
    #     """取消关注事件"""
    #     res = yield self.event_ps.opt_event_unsubscribe(self.current_user)
    #     self.send_xml(res)
    #
    # @gen.coroutine
    # def event_SCAN(self):
    #     """用户扫码事件"""
    #     res = yield self.event_ps.opt_event_scan(self.current_user, self.msg)
    #     self.send_xml(res)
    #
    # @gen.coroutine
    # def event_CLICK(self):
    #     """自定义菜单事件
    #     用户点击自定义菜单后，微信会把点击事件推送给开发者，请注意，点击菜单弹出子菜单，不会产生上报"""
    #     self.send_xml()
    #
    # @gen.coroutine
    # def event_VIEW(self):
    #     """自定义菜单事件
    #     点击菜单跳转链接时的事件推送"""
    #     self.send_xml()
    #
    # @gen.coroutine
    # def event_LOCATION(self):
    #     """上报地理位置事件
    #     用户同意上报地理位置后，每次进入公众号会话时，都会在进入时上报地理位置，
    #     或在进入会话后每5秒上报一次地理位置，公众号可以在公众平台网站中修改以上设置。
    #     上报地理位置时，微信会将上报地理位置事件推送到开发者填写的URL。"""
    #     self.send_xml()
    #
    # @gen.coroutine
    # def event_kf_create_session(self):
    #     """客服功能, referer: https://mp.weixin.qq.com/wiki?action=doc&id=mp1421140547&t=0.4438341066455047
    #     获取多客服会话状态推送事件 - 接入会话"""
    #     self.send_xml()
    #
    # @gen.coroutine
    # def event_kf_close_session(self):
    #     """获取多客服会话状态推送事件 - 关闭会话"""
    #     self.send_xml()
    #
    # @gen.coroutine
    # def event_kf_switch_session(self):
    #     """获取多客服会话状态推送事件 - 转接会话"""
    #     self.send_xml()
    #
    # @gen.coroutine
    # def event_MASSSENDJOBFINISH(self):
    #     """微信群发事件 referer: https://mp.weixin.qq.com/wiki?action=doc&id=mp1481187827_i0l21&t=0.944874910600048"""
    #     self.send_xml()
    #
    # @gen.coroutine
    # def event_TEMPLATESENDJOBFINISH(self):
    #     """消息模板推送结果 referer: https://mp.weixin.qq.com/wiki?action=doc&id=mp1433751277&t=0.29629938341489237
    #     在模版消息发送任务完成后，微信服务器会将是否送达成功作为通知，发送到开发者中心中填写的服务器配置地址中"""
    #     self.send_xml()

    def on_finish(self):
        """继承MetaBaseHandler.on_finish(),添加部分日志"""

        self.log_info = {"wxmsg": self.msg}
        super().on_finish()

    def get_msg(self):
        from_xml = self.request.body
        if not from_xml:
            return ObjectDict()
        return parse_msg(from_xml)

    def verification(self):
        """
        验证 POST 数据是否真实有效
        :return:
        """
        toke = "63659a086f2011e5a2be00163e004a1f"

        try:
            ret, hashstr = SHA1().getSHA1(toke,
                                          self.params.timestamp,
                                          self.params.nonce,
                                          '')
        except Exception as e:
            self.logger.error(traceback.format_exc())

        if hashstr == self.params.signature:
            return True

        return False