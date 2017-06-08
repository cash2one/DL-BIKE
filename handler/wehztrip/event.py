# coding=utf-8

# @Time    : 2/6/17 09:03
# @Author  : panda (panyuxin@moseeker.com)
# @File    : event.py
# @DES     : 杭州公共出行微信公众号消息交互

import time
import traceback
from tornado import gen, ioloop

from handler.metabase import MetaBaseHandler
from util.common import ObjectDict
from util.tool.xml_tool import parse_msg
from util.wechat.msgcrypt import SHA1
from cache.hztrip import HztripCache


class WechatOauthHandler(MetaBaseHandler):

    """开发者模式"""

    def __init__(self, application, request, **kwargs):
        super(WechatOauthHandler, self).__init__(application, request, **kwargs)

        self.msg = None
        self.hztrip = HztripCache()
        self.key = None

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
        try:
            msg_type = self.msg['MsgType']
            if self.verification():
                # session_key: bus; station; around; transfer; bike; park; yaohao; pm25;
                session_key = self.hztrip.get_hztrip_session(self.current_user.openid)
                yield getattr(self, 'post_' + msg_type)(session_key)
                yield gen.sleep(1)
                yield self.event_ps.wx_custom_send(self.msg)
            else:
                self.logger.error(
                    "[wechat_oauth]verification failed:{}".format(
                        self.msg))
        except Exception as e:
            self.send_xml()
            self.logger.error(traceback.format_exc())

    @gen.coroutine
    def post_verify(self):
        self.send_xml()

    @gen.coroutine
    def post_text(self, session_key):
        """文本消息, referer: https://mp.weixin.qq.com/wiki?action=doc&id=mp1421140453&t=0.33078310940365907"""
        res = yield self.event_ps.opt_msg(self.msg, session_key)
        self.send_xml(res)

    @gen.coroutine
    def post_image(self, session_key):
        """图片消息, referer: https://mp.weixin.qq.com/wiki?action=doc&id=mp1421140453&t=0.33078310940365907"""
        res = yield self.event_ps.opt_default(self.msg)
        self.send_xml(res)

    @gen.coroutine
    def post_voice(self, session_key):
        """语音消息, referer: https://mp.weixin.qq.com/wiki?action=doc&id=mp1421140453&t=0.33078310940365907"""
        res = yield self.event_ps.opt_msg(self.msg, session_key)
        self.send_xml(res)

    @gen.coroutine
    def post_video(self, session_key):
        """视频消息, referer: https://mp.weixin.qq.com/wiki?action=doc&id=mp1421140453&t=0.33078310940365907"""
        res = yield self.event_ps.opt_default(self.msg)
        self.send_xml(res)

    @gen.coroutine
    def post_shortvideo(self, session_key):
        """小视屏消息, referer: https://mp.weixin.qq.com/wiki?action=doc&id=mp1421140453&t=0.33078310940365907"""
        res = yield self.event_ps.opt_default(self.msg)
        self.send_xml(res)

    @gen.coroutine
    def post_location(self, session_key):
        """地理位置消息, referer: https://mp.weixin.qq.com/wiki?action=doc&id=mp1421140453&t=0.33078310940365907"""
        res = yield self.event_ps.opt_msg(self.msg, session_key)
        self.send_xml(res)

    @gen.coroutine
    def post_link(self, session_key):
        """链接消息, referer: https://mp.weixin.qq.com/wiki?action=doc&id=mp1421140453&t=0.33078310940365907"""
        res = yield self.event_ps.opt_default(self.msg)
        self.send_xml(res)

    @gen.coroutine
    def post_event(self, session_key):
        """微信事件, referer: https://mp.weixin.qq.com/wiki?action=doc&id=mp1421140454&t=0.6181039380535693"""
        event = self.msg['Event']
        yield getattr(self, 'event_' + event)()
    #
    @gen.coroutine
    def event_subscribe(self):
        """关注事件"""
        res = yield self.event_ps.opt_follow(self.msg)
        self.send_xml(res)

    @gen.coroutine
    def event_unsubscribe(self):
        """取消关注事件"""
        res = yield self.event_ps.opt_default(self.msg)
        self.send_xml(res)

    @gen.coroutine
    def event_SCAN(self):
        """用户扫码事件"""
        res = yield self.event_ps.opt_default(self.msg)
        self.send_xml(res)

    @gen.coroutine
    def event_CLICK(self):
        """自定义菜单事件
        用户点击自定义菜单后，微信会把点击事件推送给开发者，请注意，点击菜单弹出子菜单，不会产生上报"""
        self.key = self.msg['EventKey']
        self.hztrip.set_hztrip_session(self.current_user.openid, self.key)

        res = yield self.event_ps.opt_click(self.msg, self.key)
        self.send_xml(res)

        # 发送客服消息
        # ioloop.IOLoop.instance().add_timeout(time.time() + 2, self.event_ps.wx_custom_send(self.msg))

    @gen.coroutine
    def event_VIEW(self):
        """自定义菜单事件
        点击菜单跳转链接时的事件推送"""
        self.send_xml()

    @gen.coroutine
    def event_LOCATION(self):
        """上报地理位置事件
        用户同意上报地理位置后，每次进入公众号会话时，都会在进入时上报地理位置，
        或在进入会话后每5秒上报一次地理位置，公众号可以在公众平台网站中修改以上设置。
        上报地理位置时，微信会将上报地理位置事件推送到开发者填写的URL。"""
        self.send_xml()

    @gen.coroutine
    def event_TEMPLATESENDJOBFINISH(self):
        """消息模板推送结果 referer: https://mp.weixin.qq.com/wiki?action=doc&id=mp1433751277&t=0.29629938341489237
        在模版消息发送任务完成后，微信服务器会将是否送达成功作为通知，发送到开发者中心中填写的服务器配置地址中"""
        self.send_xml()

    def on_finish(self):
        """继承MetaBaseHandler.on_finish(),添加部分日志"""

        self.log_info = {"wxmsg": self.msg}
        super().on_finish()

    def get_msg(self):
        from_xml = self.request.body
        # self.logger.debug("get_msg:{}".format(from_xml))
        if not from_xml:
            return ObjectDict()
        return parse_msg(from_xml)

    def verification(self):
        """
        验证 POST 数据是否真实有效
        :return:
        """

        token = self.settings.get("hztrip_token")

        hashstr = None
        try:
            ret, hashstr = SHA1().getSHA1(token,
                                          self.params.timestamp,
                                          self.params.nonce,
                                          '')
        except Exception as e:
            self.logger.error(traceback.format_exc())

        return hashstr == self.params.signature