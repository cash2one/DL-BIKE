# coding=utf-8

# @Time    : 3/12/17 16:53
# @Author  : panda (panyuxin@moseeker.com)
# @File    : event.py
# @DES     :

import time
from datetime import datetime, timedelta
from tornado import gen

import conf.wechat as wx_const
import conf.common as const
from util.tool.url_tool import make_static_url
from service.page.base import PageService
from util.common import ObjectDict
from cache.hztrip import HztripCache

class EventPageService(PageService):

    def __init__(self):
        super().__init__()
        self.hztrip_cache = HztripCache()

    @gen.coroutine
    def opt_default(self, msg, session_key):
        """被动回复用户消息的总控处理
        referer: https://mp.weixin.qq.com/wiki?action=doc&id=mp1421140543&t=0.5116553557196903
        :param msg: 消息
        :param session_key:
        :return:
        """

        content = "对不起，不明白您的意思，手动输入一句话试试"
        res = yield self.wx_rep_text(msg, content)
        return res

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
    def opt_click(self, msg, click_key):

        content = ""
        if click_key == "bus":
            content += "查公交实时到站:\n输入公交线路，如900\n"
        elif click_key == "station":
            content += "查公交站点:\n输入站点名，如小车桥\n"
        elif click_key == "around":
            content += "查周边公交站:\n1.输入具体地址\n2.发送您的位置信息\n"
        elif click_key == "transfer":
            content += "查公交换乘:\n输入起点和终点，并以空格分割，如留下 小车桥\n"
        elif click_key == "bike":
            content += "查询实时自行车租赁点:\n1.输入详细的街道或小区\n2.发送您的位置信息\n"
        elif click_key == "park":
            content += "查实时停车位:\n1.输入具体地址\n2.发送您的位置信息\n"
        elif click_key == "yaohao":
            content += "杭州小客车摇号结果查询:\n1.输入姓名或个人申请编号\n市调控办每月26日组织摇号，如遇周末顺延\n"
        elif click_key == "pm25":
            content += "查实时空气污染指数:\n输入城市中文名称，如杭州"

        content += "\n<a href='http://mp.weixin.qq.com/s?__biz=MjM5NzM0MTkyMA==&mid=200265581&idx=1&sn=3cb4415ab52fd40b24353212115917e3'># 微信查杭州实时公交、实时自行车、实时停车位</a>"

        res = yield self.wx_rep_text(msg, content)
        return res

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
        elif session_key == "park":
            res = yield self.do_park(msg)
        elif session_key == "yaohao":
            res = yield self.do_yaohao(msg)
        elif session_key == "pm25":
            res = yield self.do_pm25(msg)
        else:
            res = yield self.opt_default(msg, session_key)

        return res

    @gen.coroutine
    def do_bus(self, msg):

        if msg.MsgType == "text":
            keyword = msg.Content.strip()

        pass

    @gen.coroutine
    def do_bike(self, msg):

        keyword, lng, lat = yield self._get_lng_lat(msg)

        res = yield self.hztrip_ds.get_bikes({
            "lng": lng,
            "lat": lat,
        })

        if not res.data:
            content = "抱歉，找不到【{}】附近的租赁点！输入更详细的地址，查找更精确\n\n" \
                      "查询实时自行车租赁点: \n1.输入详细的街道或小区\n2.发送您的位置信息".format(keyword)
            res = yield self.wx_rep_text(msg, content)
            return res
        else:
            data_list = res.data[0:8]
            news = wx_const.WX_NEWS_REPLY_HEAD_TPL % (msg.FromUserName,
                                                      msg.ToUserName,
                                                      str(time.time()),
                                                      len(data_list))
            for item in data_list:
                title = "{0}_可租[{1}]_可还[{2}]".format(item.get("name", ""), item.get("rentcount",""), item.get("restorecount", ""))
                description = "编号：{0}\n位置：{1}".format(item.get("number", ""), item.get("address",""))
                url = "http://api.map.baidu.com/marker?location={0},{1}&title={2}" \
                       "&content=[杭州公共出行]公共自行车租赁点&output=html".format(item.get("lat", 0), item.get("lon", 0), item.get("name", ""))
                headimg = "http://api.map.baidu.com/staticimage/v2?ak=lSbGt6Z31wK9Pwi2GLUCx6ywLeflbjHf" \
                          "&center={0},{1}&width=360&height=200&zoom=17&copyright=1&markers={2},{3}&markerStyles=l".format(item.get("lon", 0),item.get("lat", 0),item.get("lon", 0),item.get("lat", 0))

                news_item = wx_const.WX_NEWS_REPLY_ITEM_TPL % (
                    title,
                    description,
                    headimg,
                    url
                )
                news += news_item

            news_info = news + wx_const.WX_NEWS_REPLY_FOOT_TPL
            return news_info

    @gen.coroutine
    def do_park(self, msg):

        keyword, lng, lat = yield self._get_lng_lat(msg)

        res = yield self.hztrip_ds.get_stop({
            "longitude": lng,
            "latitude": lat,
        })

        if not res.List:
            content = "抱歉，找不到【{}】附近的停车位！输入更详细的地址，查找更精确\n\n" \
                      "查询实时停车位信息: \n1.输入详细的街道或小区\n2.发送您的位置信息".format(keyword)
            res = yield self.wx_rep_text(msg, content)
            return res
        else:
            news = wx_const.WX_NEWS_REPLY_HEAD_TPL % (msg.FromUserName,
                                                      msg.ToUserName,
                                                      str(time.time()),
                                                      1)

            title = "搜索【{}】周边的实时停车位".format(keyword)
            description = "共找到{0}处停车位\n\n".format(len(res.List))
            for item in res.List:
                description += "★停车场: {0}\n实时车位: 『{1}』\n地址: {2}\n距离: {3}米\n参考价: {4}\n\n".format(item.get("Name"),
                                                                                               const.STOP_STATE.get(str(
                                                                                                   item.get("State"))),
                                                                                               item.get("Address"),
                                                                                               item.get("Distance"),
                                                                                               item.get("Type"))

            url = "http://www.hztrip.org/?fr=wechat"
            headimg = make_static_url("http://www.hztrip.org/image/banner.jpg")

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
    def do_yaohao(self, msg):

        keyword = msg.Content.strip()
        res = yield self.hztrip_ds.get_yaohao({
            "name": keyword,
        })

        if res.status != '0' or not res.data[0].get("disp_data", ""):
            news = wx_const.WX_NEWS_REPLY_HEAD_TPL % (msg.FromUserName,
                                                      msg.ToUserName,
                                                      str(time.time()),
                                                      1)

            title = "抱歉，继续努力吧！"
            description = "抱歉，找不到【{}】的摇号结果\n\n" \
                      "摇号申请编码有效期为3个月，请及时登录官网延长有效期\n目前仅支持个人用户的中签查询".format(keyword)

            url = "http://mp.weixin.qq.com/s?__biz=MjM5NzM0MTkyMA==&mid=201864609&idx=1&sn=df673dd4a643301833453fcd503fce82#rd"
            headimg = ""

            item = wx_const.WX_NEWS_REPLY_ITEM_TPL % (
                title,
                description,
                headimg,
                url
            )
            news += item

        else:
            news = wx_const.WX_NEWS_REPLY_HEAD_TPL % (msg.FromUserName,
                                                      msg.ToUserName,
                                                      str(time.time()),
                                                      1)

            title = "恭喜，所有【{}】的同名中签结果如下".format(keyword)
            description = "中签有效期六个月，过期无效。本次查询只列出所有有效中签结果\n"

            Obj_dict = dict()
            for item in res.data[0].get("disp_data", ""):
                eid = item['eid']
                if not isinstance(Obj_dict.get(eid, None), list):
                    Obj_dict[eid] = list()
                    Obj_dict[eid].append(item)
                else:
                    Obj_dict[eid].append(item)

            Obj_list = sorted(Obj_dict.items(), key=lambda d: d[0], reverse=True)
            valid_month = (datetime.now() + timedelta(days=-200)).strftime("%Y%m")
            for k, v in Obj_list:
                res_date_time = datetime.strptime(str(k), "%Y%m")
                if k < valid_month:
                    break
                description += "\n★期号: {}年{}月\n".format(res_date_time.year, res_date_time.month)
                for item in v:
                    description += "{}  {}\n".format(item.get("name"), item.get("tid"))

            description += "\n温馨提示: \n1.指标配置成功后，您可以登录杭州小客车摇号官网打印《小客车配置指标确认通知书》办理购车、上牌等手续\n" \
                           "2.指标有效期为6个月。单位和个人应当在指标有效期内使用指标。\n" \
                           "3.逾期未使用的，视为放弃指标且自有效期届满次日起，两年内不得申请增量指标\n"
            url = "http://mp.weixin.qq.com/s?__biz=MjM5NzM0MTkyMA==&mid=201864609&idx=1&sn=df673dd4a643301833453fcd503fce82#rd"
            headimg = ""

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
    def do_pm25(self, msg):

        keyword = msg.Content.strip()

        pm25_cache = self.hztrip_cache.get_pm25_session()

        city_pm25 = pm25_cache.get(keyword)
        print (city_pm25)

        if not city_pm25:
            news = wx_const.WX_NEWS_REPLY_HEAD_TPL % (msg.FromUserName,
                                                      msg.ToUserName,
                                                      str(time.time()),
                                                      1)

            title = "抱歉，找不到【{}】的空气污染指数".format(keyword)
            description = "请正确输入查询城市，如杭州"

            url = "http://www.hztrip.org/?fr=wechat"
            headimg = ""

            item = wx_const.WX_NEWS_REPLY_ITEM_TPL % (
                title,
                description,
                headimg,
                url
            )
            news += item

        else:
            news = wx_const.WX_NEWS_REPLY_HEAD_TPL % (msg.FromUserName,
                                                      msg.ToUserName,
                                                      str(time.time()),
                                                      1)

            update_time_str = city_pm25[0].get("time_point")
            d = datetime.strptime(str(update_time_str), "%Y-%m-%dT%H:%M:%SZ")
            update_time = "{}年{}月{}日 {}时{}分".format(d.year, d.month, d.day, d.hour, d.minute)
            title = "{}实时空气质量指数(更新于{})".format(keyword, update_time)
            description = "您好，当前{}各监测点空气质量指数如下(数值单位: μg/m3)：\n".format(keyword)

            for item in city_pm25:
                description += "★{}\n空气质量指数类别: {}\n空气质量指数: {}\n首要污染物: {}\nPM2.5/小时: {}" \
                               "\nPM10/小时: {}\nO3/小时: {}\nSO2/小时: {}\n\n".format(item.get("position_name"),
                                                                             item.get("quality"),
                                                                             item.get("aqi") or "",
                                                                             item.get("primary_pollutant"),
                                                                             item.get("pm2_5"),
                                                                             item.get("pm10"),
                                                                             item.get("o3"),
                                                                             item.get("so2")
                                                                             )


            description += "\n数据更新时间: {} \n数据来源于pm25.in \n★可输入城市名，查询国内各城市实时空气污染指数".format(update_time)
            url = "http://www.hztrip.org/?fr=wechat"
            headimg = ""

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
    def _get_lng_lat(self, msg):

        """
        获得经纬度信息
        :param msg:
        :return: lng, lat: 经度，纬度
        """

        self.logger.debug("do_bike: {}".format(msg))

        lng, lat = 0, 0

        if msg.MsgType == "text":
            keyword = msg.Content.strip()
            res = yield self.hztrip_ds.get_lnglat_by_baidu(keyword)
            if res.status == 0:
                lng, lat = res.result.get("location", {}).get("lng", 0), res.result.get("location", {}).get("lat", 0)
        elif msg.MsgType == "location":
            keyword = msg.Label.strip()
            res = yield self.hztrip_ds.get_bd_lnglat(msg.Location_Y, msg.Location_X)
            if res.status == 0:
                lng, lat = res.result[0].get("x", 0), res.result[0].get("y", 0)
        elif msg.MsgType == "voice":
            keyword = msg.Recognition.strip()
            res = yield self.hztrip_ds.get_lnglat_by_baidu(keyword)
            if res.status == 0:
                lng, lat = res.result.get("location", {}).get("lng", 0), res.result.get("location", {}).get("lat", 0)

        return keyword, lng, lat