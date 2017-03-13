# coding=utf-8

# @Time    : 3/12/17 16:53
# @Author  : panda (panyuxin@moseeker.com)
# @File    : event.py
# @DES     :
import time
from tornado import gen

import conf.wechat as wx_const
from util.tool.url_tool import make_static_url
from service.page.base import PageService

class EventPageService(PageService):

    def __init__(self):
        super().__init__()

    @gen.coroutine
    def opt_default(self, msg, session_key):
        """被动回复用户消息的总控处理
        referer: https://mp.weixin.qq.com/wiki?action=doc&id=mp1421140543&t=0.5116553557196903
        :param msg: 消息
        :param session_key:
        :return:
        """

        raise gen.Return("对不起，不明白您的意思，手动输入一句话试试")

    @gen.coroutine
    def opt_follow(self, msg):

        news = wx_const.WX_NEWS_REPLY_HEAD_TPL % (msg.FromUserName,
                                                  msg.ToUserName,
                                                  str(time.time()),
                                                  1)

        item = wx_const.WX_NEWS_REPLY_ITEM_TPL % (
            "杭州公共出行——公交车、公共自行车、停车位实时查询'",
            "杭州公共出行，可查实时公交、实时自行车、实时停车位信息，并提供汽车违章查询、杭州小客车摇号结果查询、空气质量查询等服务。"
            "杭州出行、生活、旅行必备应用。\n点击菜单，按提示输入查询条件获得实时信息。如需杭州公共交通使用帮助，请输入\"?\"\n"
            "『去百度手机助手下载安装杭州公共出行Android应用，体验更多功能』任何建议、反馈可编辑\"re+内容\",如re谢谢",
            make_static_url("http://hztrip.sinaapp.com/image/banner.jpg"),
            "http://hztrip.sinaapp.com/?fr=wechat"
        )
        news += item

        news_info = news + wx_const.WX_NEWS_REPLY_FOOT_TPL

        raise gen.Return(news_info)

    @gen.coroutine
    def opt_msg(self, msg, session_key):
        """针对用户的文本消息，被动回复消息
        :param msg: 消息
        :param session_key:
        :return:
        """

        # bus; station; around; transfer; bike; park; yaohao; pm25;
        if session_key == "bus":
            self.do_bus(msg)
        # elif session_key == "station":
        #     do_station()
        # elif session_key == "around":
        #     do_around()
        # elif session_key == "transfer":
        #     do_transfer()
        elif session_key == "bike":
            self.do_bike(msg)
        # elif session_key == "park":
        #     do_park()
        # elif session_key == "yaohao":
        #     do_yaohao()
        # elif session_key == "pm25":
        #     do_pm25()
        else:
            self.opt_default(msg, session_key)

    @gen.coroutine
    def do_bike(self, msg):

        self.logger.debug("do_bike: {}".format(msg))

        if msg.MsgType == "text":
            keyword = msg.Content.strip()
        elif msg.MsgType == "location":
            pass

        pass

    @gen.coroutine
    def do_bus(self, msg):

        if msg.MsgType == "text":
            keyword = msg.Content.strip()

        pass