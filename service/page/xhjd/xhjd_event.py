# coding=utf-8

# @Time    : 3/12/17 16:53
# @Author  : panda (panyuxin@moseeker.com)
# @File    : xhjd_event.py
# @DES     :

import time
from tornado import gen

import conf.wechat as wx_const
from util.tool.date_tool import curr_now_minute
from service.page.base import PageService

class XhjdEventPageService(PageService):

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
        print (userinfo)
        yield self.wypcs110content_ds.add_wypcs110content(fields={
            "openid": msg.FromUserName,
            "nickname": userinfo.nickname,
            "sex": userinfo.sex,
            "city": userinfo.city,
            "country": userinfo.country,
            "province": userinfo.province,
            "msgType": msg.MsgType,
            "event": session_key,
            "text": msg.Content,
            "createTime": curr_now_minute()
        })

        res = yield self.wx_rep_text(msg, content)

        return res

    @gen.coroutine
    def opt_location(self, msg, session_key):
        """针对用户的location消息，被动回复消息
        :param msg: 消息
        :param session_key:
        :return:
        """
        content = "您的位置已经收到，谢谢！"
        res = yield self.wx_rep_text(msg, content)
        userinfo = yield self._get_user_info(msg.FromUserName)
        yield self.wypcs110content_ds.add_wypcs110content(fields={
            "openid": msg.FromUserName,
            "nickname": userinfo.nickname,
            "sex": userinfo.sex,
            "city": userinfo.city or "",
            "country": userinfo.country or "",
            "province": userinfo.province or "",
            "msgType": msg.MsgType,
            "event": session_key,
            "latitude": msg.Location_X,
            "longitude": msg.Location_Y,
            "label": msg.Label,
            "createTime": curr_now_minute()
        })

        # 发送警情消息模板
        url = "http://api.map.baidu.com/marker?location={},{}&title=用户的位置" \
              "&content={}&coord_type=gcj02&output=html&src=wypcs110|wypcs110".format(msg.Location_X, msg.Location_Y, "警情")
        template_id = "g58vKw9yJmFg33_Y6HBXUSy5wqTx7bcPAy6YZG0X-2Q"
        data = {
            "first": {
                "value":"您的管辖范围有一起警情",
                "color" : "#743A3A",
            },
            "keyword1" : {
                "value" :"微信报警位置标注",
                "color" :"#743A3A",
            },
            "keyword2" :{
                "value" :"",
                "color" :"#743A3A",
            },
            "remark" :{
                "value" :"微信用户：{}于{}在{}发出报警位置标注。请尽快赶到现场".format(userinfo.nickname, curr_now_minute(), msg.Label),
                "color": "#743A3A",
            }
        }
        # yield self._send_template("oznRwtzG0IxBPLlBH-oUWZnJo6Gk", template_id, url, data) # 项
        yield self._send_template("oznRwt19ILiJzRW3ENy5miRWH3zQ", template_id, url, data) # 潘
        # yield self._send_template("oznRwtwAyDAjF2gBZ1ws4VYZ8oyo", template_id, url, data) # 湘湖警点收听号1
        # yield self._send_template("oznRwt6yoyAg_pw93kvMIVSy9qos", template_id, url, data) # 湘湖警点收听号2
        # yield self._send_template("oznRwtzJyyqVXyxBSMFUOrkAYG4E", template_id, url, data) # 湘湖警点收听号2
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
