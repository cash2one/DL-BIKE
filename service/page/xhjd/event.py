# coding=utf-8

# @Time    : 3/12/17 16:53
# @Author  : panda (panyuxin@moseeker.com)
# @File    : event.py
# @DES     :

import re
import time
from datetime import datetime, timedelta
from tornado import gen

import conf.wechat as wx_const
import conf.common as const
from util.tool.url_tool import make_static_url
from util.tool.date_tool import sec_2_time
from service.page.base import PageService

class EventPageService(PageService):

    def __init__(self):
        super().__init__()
        self.appid = "wxa3bf32fdbd79dc04"
        self.appsecret = "848346ee2818483c2981243b20eba707"

    @gen.coroutine
    def opt_default(self, msg):
        """被动回复用户消息的总控处理
        referer: https://mp.weixin.qq.com/wiki?action=doc&id=mp1421140543&t=0.5116553557196903
        :param msg: 消息
        :return:
        """

        content = ""
        res = yield self.wx_rep_text(msg, content)
        return res

    @gen.coroutine
    def opt_follow(self, msg):
        """
        处理关注事件
        :param msg:
        :return:
        """

        content = "您好，这里是萧山区公安分局闻堰派出所微信公众平台，欢迎您的关注！"
        res = yield self.wx_rep_text(msg, content)
        return res

    @gen.coroutine
    def opt_click(self, msg, click_key):
        """处理用户点击事件，提示语
        """

        content = ""
        if click_key == "IDCardReservation":
            content += "您好，现进行身份证办理预约。\n\n孤寡老人或行动不便病人预约上门服务请回复“0”;\n\n户籍窗口错时服务预约请回复“1”;"
        elif click_key == "residenceReservation":
            content += "您好，临时居住证办理预约已提交，请回复您的姓名与联系电话，工作人员将会在2个工作日内与您联系。\n户籍窗口联系电话0571-82301032"
        elif click_key == "accountResultCheck":
            content += "您好，您需查询的事项已提交，请回复您的姓名和联系电话，工作人员将会在2个工作日内查询并反馈。\n户籍窗口联系电话0571-82301032"
        elif click_key == "IDCardResultCheck":
            content += "您好，您需查询的事项已提交，请回复您的姓名和联系电话，工作人员将会在2个工作日内查询并反馈。\n户籍窗口联系电话0571-82301032"
        elif click_key == "alarmPosition":
            content += "您好，此功能为报警辅助功能，请点击键盘“位置”，确认位置后点击“发送”。\n报警请直接拨打0571-82306110或110"
        elif click_key == "clueProvide":
            content += "您好，谢谢您提供的线索，请回复您的线索，民警会及时核查，一旦发现违法犯罪活动，绝不姑息!"
        elif click_key == "suggestion":
            content += "您好，请回复您的意见建议。\n谢谢您对我们的工作提出宝贵的意见建议，我们将不断整改完善，确保更好地为人民服务！"

        res = yield self.wx_rep_text(msg, content)
        return res

    @gen.coroutine
    def wx_rep_text(self, msg, text):
        """微信交互：回复文本消息
        :param msg: 消息
        :param text: 文本消息
        :return:
        """

        if text is None:
            raise gen.Return("")

        text_info = wx_const.WX_TEXT_REPLY % (msg.FromUserName,
                                            msg.ToUserName,
                                            int(time.time()),
                                            text)

        raise gen.Return(text_info)

    @gen.coroutine
    def opt_text(self, msg, session_key):
        """针对用户的文本消息，被动回复消息
        :param msg: 消息
        :param session_key:
        :return:
        """
        content = "您的回复已经收到，谢谢！"
        if not session_key:
            content = "您的回复已经收到，请留下您的姓名和手机号码，我们会在2个工作日内通过平台或电话与您联系，谢谢！"
        else:
            if session_key == "IDCardReservation":
                keyword = self._get_text(msg)
                if keyword == "0":
                    content = "您好，您预约的孤寡老人（行动不便病人）身份证办理上门服务已提交，" \
                              "请回复您的姓名与联系电话，工作人员将会在2个工作日内与您联系。\n户籍窗口联系电话0571-82301032"
                elif keyword == "1":
                    content = "您好，您预约的户籍窗口错时服务已提交，请提供你的姓名与联系电话，" \
                              "工作人员将会在2个工作日内与您联系。\n户籍窗口联系电话0571-82301032"

        userinfo = yield self._get_user_info(msg.FromUserName)

        res = yield self.wx_rep_text(msg, content)

        return res

    def _get_text(self, msg):

        """
        获得文本信息
        :param msg:
        :return:  str
        """

        keyword = ""
        if msg.MsgType == "text":
            keyword = msg.Content.strip()
        elif msg.MsgType == "voice":
            keyword = msg.Recognition.strip("。")

        return keyword.upper()

    @gen.coroutine
    def _get_lng_lat(self, msg):

        """
        获得经纬度信息
        :param msg:
        :param type: 经纬度类型，支持百度经纬度，微信经纬度（火星坐标）
        :return: lng, lat: 经度，纬度
        """

        lng, lat = 0, 0
        res = yield self.hztrip_ds.get_bd_lnglat(msg.Location_Y, msg.Location_X)
        if res.status == 0:
            lng, lat = res.result[0].get("x", 0), res.result[0].get("y", 0)

        return lng, lat

    @gen.coroutine
    def _get_user_info(self, openid):
        """
        获得用户微信信息
        :param openid:
        :return:
        """
        ret = yield self.wechat_ds.get_userinfo(openid, self.appid, self.appsecret)
        return ret

    @gen.coroutine
    def _send_template(self, touser, template_id, url, data):
        """
        发送消息模板
        :param touser:
        :param template_id:
        :param url:
        :param data:
        :return:
        """

        ret = yield self.wechat_ds.send_template(self.appid, self.appsecret, touser, template_id, url, data)
        return ret
