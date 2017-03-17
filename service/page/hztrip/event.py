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
            make_static_url("http://www.hztrip.org/image/banner.jpg"),
            "http://www.hztrip.org/?fr=wechat"
        )
        news += item

        news_info = news + wx_const.WX_NEWS_REPLY_FOOT_TPL

        raise gen.Return(news_info)

    @gen.coroutine
    def wx_rep_text(self, msg, text):
        """微信交互：回复文本消息
        :param msg: 消息
        :param text: 文本消息
        :param nonce:
        :param wechat:
        :return:
        """

        if text is None:
            raise gen.Return("")

        text_info = wx_const.WX_TEXT_REPLY % (msg.FromUserName,
                                            msg.ToUserName,
                                            int(time.time()),
                                            text)

        self.logger.debug("text_info: %s" % text_info)

        raise gen.Return(text_info)

    @gen.coroutine
    def opt_msg(self, msg, session_key):
        """针对用户的文本消息，被动回复消息
        :param msg: 消息
        :param session_key:
        :return:
        """

        # bus; station; around; transfer; bike; park; yaohao; pm25;
        if session_key == "bus":
            res = yield self.do_bus(msg)
        # elif session_key == "station":
        #     do_station()
        # elif session_key == "around":
        #     do_around()
        # elif session_key == "transfer":
        #     do_transfer()
        elif session_key == "bike":
            res = yield self.do_bike(msg)
        # elif session_key == "park":
        #     do_park()
        # elif session_key == "yaohao":
        #     do_yaohao()
        # elif session_key == "pm25":
        #     do_pm25()
        else:
            res = yield self.opt_default(msg, session_key)

        return res

    @gen.coroutine
    def do_bike(self, msg):

        self.logger.debug("do_bike: {}".format(msg))

        if msg.MsgType == "text":
            keyword = msg.Content.strip()
            res = yield self.hztrip_ds.get_lnglat_by_baidu(keyword)
            if res.status == 0:
                lng, lat = res.result.get("location", {}).get("lng", 0), res.result.get("location", {}).get("lat", 0),
        elif msg.MsgType == "location":
            res = yield self.hztrip_ds.get_bd_lnglat(msg.Location_Y, msg.Location_X)
            if res.status == 0:
                lng, lat = res.result[0].get("y", 0), res.result[0].get("x", 0)

        res = yield self.hztrip_ds.get_bikes({
            "lng": lng,
            "lat": lat,
        })

        if not res.data:
            content = "抱歉，找不到这附近的租赁点！输入更详细的地址，查找更精确\n" \
                      "查询实时自行车租赁点: \n1.输入详细的街道或小区\n2.发送您的位置信息"
            res = yield self.wx_rep_text(msg, content)
            return res
        else:

            news = wx_const.WX_NEWS_REPLY_HEAD_TPL % (msg.FromUserName,
                                                      msg.ToUserName,
                                                      str(time.time()),
                                                      res.count)
            data_list = res.data[0:3]
            for item in data_list:
                title = "{0}_可租【{1}】_可还【{2}】".format(item.get("name", ""), item.get("rentcount",""), item.get("restorecount", ""))
                description = "编号：{0}\n位置：{1}".format(item.get("number", ""), item.get("address",""))
                url = "http://api.map.baidu.com/marker?location={0},{1}&title={2}" \
                       "&content=[杭州公共出行]公共自行车租赁点查询&output=html&src=hztrip|hztrip".format(item.get("lat", 0), item.get("lon", 0), item.get("name", ""))
                headimg = "http://api.map.baidu.com/staticimage/v2?ak=lSbGt6Z31wK9Pwi2GLUCx6ywLeflbjHf" \
                          "&center={0},{1}&width=256&height=256&zoom=17&copyright=1&markers={2},{3}&markerStyles=l".format(item.get("lon", 0),item.get("lat", 0),item.get("lon", 0),item.get("lat", 0))

                item = wx_const.WX_NEWS_REPLY_ITEM_TPL % (
                    title,
                    description,
                    headimg,
                    url
                )
                news += item

            news_info = news + wx_const.WX_NEWS_REPLY_FOOT_TPL
            return news_info

    @gen.coroutine
    def do_bus(self, msg):

        if msg.MsgType == "text":
            keyword = msg.Content.strip()

        pass