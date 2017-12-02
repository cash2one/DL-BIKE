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
from service.page.base import PageService
from cache.hztrip import HztripCache
from util.tool.url_tool import make_static_url
from util.tool.date_tool import sec_2_time, format_hour_minute
from util.common import ObjectDict

class EventPageService(PageService):

    def __init__(self):
        super().__init__()
        self.hztrip_cache = HztripCache()

    @gen.coroutine
    def opt_default(self, msg):
        """被动回复用户消息的总控处理
        referer: https://mp.weixin.qq.com/wiki?action=doc&id=mp1421140543&t=0.5116553557196903
        :param msg: 消息
        :return:
        """

        content = "对不起，不明白您的意思。请先选择菜单功能，再输入查询内容。" \
                  "\n查实时公交，请选择菜单“查公交”->“实时公交”；" \
                  "\n查公共自行车，请选择菜单“查自行车”；" \
                  "\n查摇号，请选择菜单“更多”->“摇号查询”"
        res = yield self.wx_rep_text(msg, content)
        return res

    @gen.coroutine
    def opt_follow(self, msg):
        """
        处理关注事件
        :param msg:
        :return:
        """

        news = wx_const.WX_NEWS_REPLY_HEAD_TPL % (msg.FromUserName,
                                                  msg.ToUserName,
                                                  str(time.time()),
                                                  1)

        item = wx_const.WX_NEWS_REPLY_ITEM_TPL % (
            "杭州公共出行——公交车、公共自行车、停车位实时查询'",
            "杭州公共出行，可查实时公交、实时自行车、实时停车位信息，并提供汽车违章查询、杭州小客车摇号结果查询、空气质量查询等服务。"
            "杭州出行、生活、旅行必备应用。\n\n点击底部菜单，按提示输入查询条件获得实时信息。\n"
            "任何建议、反馈可编辑\"re+内容\",如re谢谢",
            make_static_url("http://www.hztrip.org/image/banner.jpg"),
            "https://mp.weixin.qq.com/s/liRLTrncTko3jsbuiJXMWw"
        )
        news += item

        news_info = news + wx_const.WX_NEWS_REPLY_FOOT_TPL
        raise gen.Return(news_info)

    @gen.coroutine
    def opt_click(self, msg, click_key):
        """处理用户点击事件，提示语
        """

        content = ""
        if click_key == "search":
            content += "查车站，线路名称:\n输入线路或车站，如B1路, 小车桥\n"
        elif click_key == "bus":
            content += "查公交实时到站:\n准确输入公交线路，如193路\n"
        elif click_key == "stop":
            content += "查车站电子站牌:\n准确输入车站名，如小车桥\n"
        elif click_key == "around":
            content += "查周边车站、线路:\n1.输入具体地址\n2.发送您的位置信息\n"
        elif click_key == "transfer":
            content += "查公交换乘:\n输入起点和终点，并以空格分割，如留下 小车桥\n"
        elif click_key == "bike":
            content += "查询实时自行车租赁点:\n1.输入详细的街道或小区\n2.发送您的位置信息\n3.用语音输入查询的地点\n\n提示：可点击结果查看具体租赁点地图\n"
        elif click_key == "park":
            content += "查实时停车位:\n1.输入具体地址\n2.发送您的位置信息\n3.用语音输入查询的地点\n"
        elif click_key == "yaohao":
            content += "杭州小客车摇号结果查询:\n1.输入姓名或个人申请编号\n市调控办每月26日组织摇号，如遇周末顺延\n"
        elif click_key == "pm25":
            content += "查实时空气污染指数:\n输入城市中文名称，如杭州\n"
        elif click_key == "contact":
            # text = "<a href='https://mmbiz.qlogo.cn/mmbiz_jpg/rqSdaj2zr5MPkcDRoNAtAI73jicgTvT7YDqsicmL8fLPw1qwNl6ryKSp7837Nia8qicPwJuZGAukDbkoDhHItdhiaibQ/0?wx_fmt=jp'>扫码关注勾搭作者</a>"
            # res = yield self.wx_rep_text(msg, text)
            # # res = yield self.wx_rep_image(msg)
            # return res
            res = yield self.wx_rep_image(msg, "o3ERCv0Z01payyqgdMz1y_Gn7SOB4J3NHvfMRJa8JN0")
            return res
        elif click_key == "good":
            res = yield self.wx_rep_image(msg, "o3ERCv0Z01payyqgdMz1y03aWGmbd7wqnOwVLtYUGIg")
            return res

        # content += "\n<a href='http://mp.weixin.qq.com/s?__biz=MjM5NzM0MTkyMA==&mid=200265581&idx=1&sn=3cb4415ab52fd40b24353212115917e3'># 微信查杭州实时公交、实时自行车、实时停车位</a>"

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
    def wx_rep_image(self, msg, media_id):
        """微信交互：回复图片消息
        微信号：hztrip 的二维码 9fTQ1RS4vuNQxxt9MlAHk6bb-RZwaYY5EHT4uHEqfoVMtXtnfG8O9K_4c3v5Ofdn
        :param msg: 消息
        :param text: 文本消息
        :param media_id: 图片id
        :return:
        """

        text_info = wx_const.WX_IMAGE_REPLY % (msg.FromUserName,
                                            msg.ToUserName,
                                            int(time.time()),
                                            media_id)
        raise gen.Return(text_info)

    @gen.coroutine
    def wx_custom_send_text(self, msg, text=None):
        """微信交互：发送文本客服消息 https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1421140547&token=&lang=zh_CN
        demo
        {
            "touser":"OPENID",
            "msgtype":"text",
            "text":
            {
                 "content":"Hello World"
            }
        }
        :return:
        """
        if not text:
            text = "【红包福利】人人可领，领完就能用。#吱口令#长按复制此消息，打开支付宝就能领取！yLl4je03Ux"
            # text = "<a href='http://mp.weixin.qq.com/s?__biz=MjM5NzM0MTkyMA==&mid=200265581&idx=1&sn=3cb4415ab52fd40b24353212115917e3'>微信查杭州实时公交、实时自行车、实时停车位</a>"

        jdata = ObjectDict({
            "touser": msg.FromUserName,
            "msgtype": "text",
            "text": ObjectDict({
                "content": text
            })
        })

        res = yield self.wechat_ds.send_custom(jdata)
        raise gen.Return(res)

    @gen.coroutine
    def wx_custom_send_news(self, msg, news):
        """微信交互：发送图文客服消息 https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1421140547
        demo
        {
            "touser":"OPENID",
            "msgtype":"news",
            "news":{
                "articles": [
                 {
                     "title":"Happy Day",
                     "description":"Is Really A Happy Day",
                     "url":"URL",
                     "picurl":"PIC_URL"
                 },
                 {
                     "title":"Happy Day",
                     "description":"Is Really A Happy Day",
                     "url":"URL",
                     "picurl":"PIC_URL"
                 }
                 ]
            }
        }
        :return:
        """
        jdata = ObjectDict({
            "touser": msg.FromUserName,
            "msgtype": "news",
            "news": ObjectDict({
                "articles": news
            })
        })

        self.logger.debug("wx_custom_send_news:{}".format(jdata))

        res = yield self.wechat_ds.send_custom(jdata)
        raise gen.Return(res)

    @gen.coroutine
    def opt_msg(self, msg, session_key):
        """针对用户的文本消息，被动回复消息
        :param msg: 消息
        :param session_key:
        :return:
        """
        # 增加取消订阅早晚高峰公交提醒
        if msg.MsgType == "text" and msg.Content.strip().startswith("退订"):
            res = yield self.do_cancel_bus_line_alert(msg)
        else:
            # 常规的业务查询
            # search; bus; station; around; transfer; bike; park; yaohao; pm25;
            if session_key == "search":
                res = yield self.do_search(msg)
            elif session_key == "bus":
                res = yield self.do_bus(msg)
            elif session_key == "stop":
                res = yield self.do_stop(msg)
            elif session_key == "around":
                res = yield self.do_around(msg)
            elif session_key == "transfer":
                res = yield self.do_transfer(msg)
            elif session_key == "bike":
                res = yield self.do_bike(msg)
            elif session_key == "park":
                res = yield self.do_park(msg)
            elif session_key == "yaohao":
                res = yield self.do_yaohao(msg)
            elif session_key == "pm25":
                res = yield self.do_pm25(msg)
            else:
                res = yield self.opt_default(msg)

        return res

    @gen.coroutine
    def do_search(self, msg):
        """
        按关键字，模糊查询公交线路
        :param msg:
        :return:
        """

        keyword = self._get_text(msg)

        line_res = yield self.hztrip_ds.get_bus_lines({
            "routeName": keyword,
        })

        stop_res = yield self.hztrip_ds.get_bus_stops({
            "stopName": keyword,
        })

        # 加标签：公交群
        yield self.wechat_ds.send_tagging(msg.FromUserName, 103)

        if not line_res.get("items") and not stop_res.get("items"):
            content = "抱歉，找不到【{}】的线路或车站信息！继续输入更详细的关键词，查找更精确\n" \
                      "如B1路, 小车桥等".format(keyword)
            res = yield self.wx_rep_text(msg, content)
            return res
        else:
            news = wx_const.WX_NEWS_REPLY_HEAD_TPL % (msg.FromUserName,
                                                      msg.ToUserName,
                                                      str(time.time()),
                                                      1)
            description = ""
            if stop_res.get("items"):
                description += "查询车站结果如下:\n"
                for item in stop_res.get("items"):
                    description += "{}\n".format(item.get("name", ""))

            if line_res.get("items"):
                description += "\n查询线路结果如下:\n"
                for item in line_res.get("items"):
                    description += "{}\n".format(item.get("name", ""))

            description += "\n小提示: \n1.可在底部菜单中切换到“实时公交”，查询实时公交到站\n2.可在底部菜单中切换到“电子站牌”，查询车站所有线路实时到站"
            title = "查找到【{}】相关车站或线路如下".format(keyword)
            url = "http://mp.weixin.qq.com/s?__biz=MjM5NzM0MTkyMA==&mid=200265581&idx=1&sn=3cb4415ab52fd40b24353212115917e3"
            headimg = ""

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
    def do_bus(self, msg, rsp_array=False):
        """
        查实时线路信息
        :param msg:
        :return:
        """
        # 加标签：公交群
        yield self.wechat_ds.send_tagging(msg.FromUserName, 103)

        keyword = self._get_text(msg)
        line_list = re.split(" ", keyword)
        # 线路名
        line_name = line_list[0] if len(line_list)>0 else ""
        # 方向
        line_order = line_list[1] if len(line_list)>1 else 0

        new_line_name = line_name.replace("(", "").replace(")","")
        if new_line_name.isdigit() or new_line_name[-1].isdigit():
            new_line_name = "{}路".format(new_line_name)
        line_cache = self.hztrip_cache.get_bus_lines(new_line_name)
        if not line_cache:
            yield self.hztrip_ds.get_bus_lines({
                "routeName": line_name,
            })
            line_cache = self.hztrip_cache.get_bus_lines(new_line_name)

        index = 1 if line_order else 0

        if line_cache and line_cache.get("routes"):
            if len(line_cache.get("routes")) <= index:
                content = "当前线路为单向线路"
                res = yield self.wx_rep_text(msg, content)
                return res
            route = line_cache.get("routes")[index]
            bus_res = yield self.hztrip_ds.get_bus_info({
                "routeId": route.get("routeId", 0),
            })

            news = wx_const.WX_NEWS_REPLY_HEAD_TPL % (msg.FromUserName,
                                                      msg.ToUserName,
                                                      str(time.time()),
                                                      1)

            title = "【{}】{} —> {}".format(route.get("routeName"), route.get("origin"),
                                          route.get("terminal"))
            d_first = datetime.strptime(str(route.get("firstBus")), "%H:%M:%S")
            d_last = datetime.strptime(str(route.get("lastBus")), "%H:%M:%S")
            description = "全程: {}公里    票价: {}元\n首班: {}    末班: {}\n\n".format('%.2f' % route.get("distance"),
                                                                       route.get("airPrice"),
                                                                       "{}时{}分".format(d_first.hour, d_first.minute),
                                                                       "{}时{}分".format(d_last.hour, d_last.minute))

            if bus_res and bus_res.get("items"):
                bus_info = bus_res.get("items", [])[0]
                stops = bus_info.get("routes", [])[0].get("stops", {})

                is_realtime = False
                for item in stops:
                    description += "{}  {}".format(item.get("routeStop",{}).get("seqNo"), item.get("routeStop",{}).get("stopName"))
                    description += "(地铁换乘)\n" if item.get("routeStop",{}).get("metroTrans") else "\n"
                    if item.get("buses",[]) and item.get("routeStop",{}).get("seqNo") != route.get("stationCnt"):
                        is_realtime = True
                        description += "   ↓----行驶中，距下一站{}米----↓\n".format(item.get("buses",[])[0].get("nextDistance"))

                if not is_realtime:
                    description += "\n当前暂无车辆实时信息\n"
                else:
                    # 添加第二天的实时公交提醒
                    yield self.hztrip_ds.add_bus_line_alert(msg.FromUserName, msg.ToUserName, keyword)
            description += "\n小提示:\n1.查询反向线路信息，请输入“{} {}”，关键词按空格分割\n2.可在底部菜单中切换到“电子站牌”，" \
                           "查询车站所有线路实时到站".format(route.get("routeName"), 1 if index==0 else 0)
            url = "https://mp.weixin.qq.com/s/liRLTrncTko3jsbuiJXMWw"
            headimg = ""

            if not rsp_array:
                item = wx_const.WX_NEWS_REPLY_ITEM_TPL % (
                    title,
                    description,
                    headimg,
                    url
                )
                news += item

                news_info = news + wx_const.WX_NEWS_REPLY_FOOT_TPL
                return news_info
            else:
                return ObjectDict(
                    title="[早晚高峰提醒]".title,
                    description=description,
                    url=url,
                    picurl=headimg,
                )
        else:
            content = "抱歉，找不到线路【{}】！输入更详细的线路名，查找更精确\n" \
                      "如B1路, B支3路区间, 193路\n\n小提示: \n如不清楚线路名称，" \
                      "可在底部菜单中切换到“搜索”，模糊查询杭州所有车站或线路".format(keyword)
            res = yield self.wx_rep_text(msg, content)
            return res

    @gen.coroutine
    def do_stop(self, msg):
        """
        查车站电子站牌
        :param msg:
        :return:
        """
        keyword = self._get_text(msg)
        line_list = re.split(" ", keyword)
        # 车站名
        stop_name = line_list[0] if len(line_list)>0 else ""
        # 方向
        stop_order = line_list[1] if len(line_list)>1 else 0

        stop_cache = self.hztrip_cache.get_bus_stops(stop_name)
        if not stop_cache:
            yield self.hztrip_ds.get_bus_stops({
                "stopName": stop_name,
            })
            stop_cache = self.hztrip_cache.get_bus_stops(stop_name)

        index = 0 if stop_cache and int(stop_order)>=len(stop_cache.get("stops")) else int(stop_order)

        # 加标签：公交群
        yield self.wechat_ds.send_tagging(msg.FromUserName, 103)

        if stop_cache and stop_cache.get("stops"):
            route = stop_cache.get("stops")[index]
            stop_res = yield self.hztrip_ds.get_stop_info({
                "amapStopId": route.get("amapId"),
            })

            news = wx_const.WX_NEWS_REPLY_HEAD_TPL % (msg.FromUserName,
                                                      msg.ToUserName,
                                                      str(time.time()),
                                                      1)


            title = "【{}】电子站牌".format(stop_cache.get("name"))

            headimg = "http://api.map.baidu.com/staticimage/v2?ak=lSbGt6Z31wK9Pwi2GLUCx6ywLeflbjHf" \
                      "&center={0},{1}&width=360&height=200&zoom=17&copyright=1&markers={2},{3}&markerStyles=l".format(
                route.get("lng", 0), route.get("lat", 0), route.get("lng", 0), route.get("lat", 0))
            description = "本站可换乘轨道交通\n" if route.get("metroTrans") else ""

            for item in stop_res.get("items",[]):
                for val in item.get("stops",[]):
                    for vval in val.get("routes",[]):
                        description += "\n★【{}】{} —> {}\n".format(vval.get("route",{}).get("routeName"),
                                                                vval.get("route",{}).get("origin"),
                                                                vval.get("route",{}).get("terminal"))

                        d_first = datetime.strptime(str(vval.get("route",{}).get("firstBus")), "%H:%M:%S")
                        d_last = datetime.strptime(str(vval.get("route",{}).get("lastBus")), "%H:%M:%S")
                        description += "首: {} 末: {} 票价: {}元\n".format("{}时{}分".format(d_first.hour,d_first.minute),
                                                                      "{}时{}分".format(d_last.hour, d_last.minute),
                                                                      vval.get("route", {}).get("airPrice", "未知"))
                        for vvval in vval.get("buses",[]):
                            description += "  ↑----最近一班的距离{}米----↑\n".format(vvval.get("targetDistance"))

            description += "\n小提示:\n1.查询其他【{}】车站电子站牌，请输入\n".format(stop_cache.get("name"))
            for idx, val in enumerate(stop_cache.get("stops")):
                description += "{} {}\n".format(val.get("stopName"), idx)
            description += "\n2.可在底部菜单中切换到“实时公交”，查询实时公交到站"
            url = "https://mp.weixin.qq.com/s/liRLTrncTko3jsbuiJXMWw"

            item = wx_const.WX_NEWS_REPLY_ITEM_TPL % (
                title,
                description,
                headimg,
                url
            )
            news += item

            news_info = news + wx_const.WX_NEWS_REPLY_FOOT_TPL
            return news_info
        else:
            content = "抱歉，找不到车站【{}】！输入更详细的车站名，查找更精确\n" \
                      "如艮山门东站, 小和山公交站\n\n小提示: \n如不清楚车站名称，" \
                      "可在底部菜单中切换到“搜索”，模糊查询杭州所有车站或线路".format(keyword)
            res = yield self.wx_rep_text(msg, content)
            return res

    @gen.coroutine
    def do_around(self, msg):
        """
        按关键字，查找周边的车站，线路
        :param msg:
        :return:
        """

        keyword, lng, lat = yield self._get_lng_lat(msg)

        around_res = yield self.hztrip_ds.get_around_bus_stop({
            "lng": lng,
            "lat": lat,
        })

        # 加标签：公交群
        yield self.wechat_ds.send_tagging(msg.FromUserName, 103)

        if not around_res.get("items") or around_res.get("result") != 0:
            content = "抱歉，找不到【{}】附近的线路或车站信息！继续输入更详细的关键词，查找更精确\n" \
                      "如小车桥等".format(keyword)
            res = yield self.wx_rep_text(msg, content)
            return res
        else:
            news = wx_const.WX_NEWS_REPLY_HEAD_TPL % (msg.FromUserName,
                                                      msg.ToUserName,
                                                      str(time.time()),
                                                      1)
            title = "查找到【{}】附近车站或线路如下".format(keyword)
            headimg = "http://api.map.baidu.com/staticimage/v2?ak=lSbGt6Z31wK9Pwi2GLUCx6ywLeflbjHf" \
                      "&center={0},{1}&width=360&height=200&zoom=17&copyright=1&markers={2},{3}&markerStyles=l".format(lng, lat, lng, lat)
            description = ""
            for item in around_res.get("items",[]):
                for val in item.get("stops",[]):
                    description += "\n★距离: {}米 【{}】".format(val.get("stop",{}).get("userDistance"), val.get("stop",{}).get("stopName"))
                    description += "(地铁换乘)\n" if val.get("stop", {}).get("metroTrans") else "\n"
                    for vval in val.get("routes",[]):
                        description += "【{}】{} —> {}\n".format(vval.get("route",{}).get("routeName"),
                                                                vval.get("route",{}).get("origin"),
                                                                vval.get("route",{}).get("terminal"))

                        d_first = datetime.strptime(str(vval.get("route",{}).get("firstBus")), "%H:%M:%S")
                        d_last = datetime.strptime(str(vval.get("route",{}).get("lastBus")), "%H:%M:%S")
                        description += "首: {} 末: {} 票价: {}元\n".format("{}时{}分".format(d_first.hour,d_first.minute),
                                                                      "{}时{}分".format(d_last.hour, d_last.minute),
                                                                      vval.get("route", {}).get("airPrice", "未知"))
                        for vvval in vval.get("buses",[]):
                            description += "  ↑----最近一班的距离{}米----↑\n".format(vvval.get("targetDistance"))


            description += "\n小提示: \n1.可在底部菜单中切换到“实时公交”，查询实时公交到站\n2.可在底部菜单中切换到“电子站牌”，查询车站所有线路实时到站"
            url = "http://mp.weixin.qq.com/s?__biz=MjM5NzM0MTkyMA==&mid=200265581&idx=1&sn=3cb4415ab52fd40b24353212115917e3"

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
    def do_transfer(self, msg):
        """
        查换乘信息
        :param msg:
        :return:
        """
        keyword = self._get_text(msg)
        line_list = re.split(" ", keyword)
        # 起点
        start_name = line_list[0] if len(line_list)>0 else ""
        # 终点
        end_name = line_list[1] if len(line_list)>1 else ""

        transfer_res = yield self.hztrip_ds.get_bd_transfer({
            "origin": start_name,
            "destination": end_name,
        })

        # 加标签：公交群
        yield self.wechat_ds.send_tagging(msg.FromUserName, 103)

        if transfer_res and transfer_res.get("status") == 0:
            news = wx_const.WX_NEWS_REPLY_HEAD_TPL % (msg.FromUserName,
                                                      msg.ToUserName,
                                                      str(time.time()),
                                                      1)

            title = "【{}】到【{}】的公交换乘方案".format(start_name, end_name)
            description = "共找到{}个公交换成方案\n".format(len(transfer_res.get("result",{}).get("routes",[])))

            for idx, val in enumerate(transfer_res.get("result",{}).get("routes",[])):
                description += "\n★方案{}: 距离: {}公里，约耗时: {}\n".format(idx+1, '%.2f' % (val.get("scheme")[0].get("distance")/1000), sec_2_time(val.get("scheme")[0].get("duration")))
                for idxx, vval in enumerate(val.get("scheme")[0].get("steps")):
                    description += "{}. {}\n".format(idxx+1, re.sub(r'</?\w+[^>]*>', '', vval[0].get("stepInstruction")))

            description += "\n打的: \n距离: {}公里，约耗时: {}\n打车费用: {}元（按驾车的最短路程计算）\n".format('%.2f' % (transfer_res.get("result",{}).get("taxi",{}).get("distance", 0)/1000),
                                                                                   sec_2_time(transfer_res.get("result", {}).get("taxi", {}).get("duration", 0)),
                                                                                   transfer_res.get("result", {}).get("taxi", {}).get("detail", [])[0].get("total_price",0) if transfer_res.get("result", {}).get("taxi", {}).get("detail", []) else 0)

            description += "\n小提示: \n1.可在底部菜单中切换到“实时公交”，查询实时公交到站\n" \
                           "2.可在底部菜单中切换到“电子站牌”，查询车站所有线路实时到站"
            url = "https://mp.weixin.qq.com/s/liRLTrncTko3jsbuiJXMWw"
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

        else:
            content = "抱歉，找不到从【{}】到【{}】的换乘方案，" \
                      "请准确输入起点和终点，如留下 小车桥\n".format(start_name, end_name)
            res = yield self.wx_rep_text(msg, content)
            return res

    @gen.coroutine
    def do_bike(self, msg):
        """
        公共自行车查询
        :param msg:
        :return:
        """

        keyword, lng, lat = yield self._get_lng_lat(msg, type="soso")

        if keyword.isdigit():
            res = yield self.hztrip_ds.get_bike_stations(msg.FromUserName, {
                "bean.number": int(keyword)
            })
        else:
            res = yield self.hztrip_ds.get_bikes(msg.FromUserName, {
                "lng": lng,
                "lat": lat,
            })

        # 加标签：自行车群
        yield self.wechat_ds.send_tagging(msg.FromUserName, 102)

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
                title = "【{0}】{1}_可租[{2}]_可还[{3}]".format(item.get("number", ""), item.get("name", ""), item.get("rentcount",""), item.get("restorecount", ""))
                description = "位置：{0}".format(item.get("address",""))
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
        """停车位查询"""

        keyword, lng, lat = yield self._get_lng_lat(msg)

        res = yield self.hztrip_ds.get_stop({
            "longitude": lng,
            "latitude": lat,
        })

        # 加标签：停车群
        yield self.wechat_ds.send_tagging(msg.FromUserName, 104)

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

            url = "https://mp.weixin.qq.com/s/liRLTrncTko3jsbuiJXMWw"
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
        """摇号查询"""

        keyword = msg.Content.strip()
        res = yield self.hztrip_ds.get_yaohao({
            "name": keyword,
        })

        # 加标签：摇号群
        yield self.wechat_ds.send_tagging(msg.FromUserName, 101)

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
        """pm25查询"""

        keyword = self._get_text(msg)
        pm25_cache = self.hztrip_cache.get_pm25_session()

        city_pm25 = pm25_cache.get(keyword)
        if not city_pm25:
            news = wx_const.WX_NEWS_REPLY_HEAD_TPL % (msg.FromUserName,
                                                      msg.ToUserName,
                                                      str(time.time()),
                                                      1)

            title = "抱歉，找不到【{}】的空气污染指数".format(keyword)
            description = "请正确输入查询城市，如杭州"

            url = "https://mp.weixin.qq.com/s/liRLTrncTko3jsbuiJXMWw"
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
            url = "https://mp.weixin.qq.com/s/liRLTrncTko3jsbuiJXMWw"
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
    def _get_lng_lat(self, msg, type="soso"):

        """
        获得经纬度信息
        :param msg:
        :param type: 经纬度类型，支持百度经纬度，微信经纬度（火星坐标）
        :return: lng, lat: 经度，纬度
        """

        lng, lat = 0, 0
        text = ""
        if msg.MsgType == "text":
            keyword = msg.Content.strip()
            text = keyword
            res = yield self.hztrip_ds.get_lnglat_by_baidu(keyword)
            if res.status == 0 and res.results:
                lng, lat = res.get("results", [])[0].get("location", {}).get("lng", 0), res.get("results", [])[0].get("location", {}).get("lat", 0)

            if type == "soso":
                res = yield self.hztrip_ds.get_soso_lnglat(lng, lat)
                if res.status == 0 and res.locations:
                    location = res.get("locations", [])[0] if len(res.get("locations", [])) > 0 else {}
                    lng, lat = location.get("lng", 0), location.get("lat", 0)

        elif msg.MsgType == "location":
            keyword = msg.Label.strip() if msg.Label else ""
            text = keyword
            if type == "soso":
                lng, lat = msg.Location_Y, msg.Location_X
            else:
                res = yield self.hztrip_ds.get_bd_lnglat(msg.Location_Y, msg.Location_X)
                if res.status == 0:
                    lng, lat = res.result[0].get("x", 0), res.result[0].get("y", 0)

        elif msg.MsgType == "voice":
            keyword = msg.Recognition.strip("。")
            text = keyword
            res = yield self.hztrip_ds.get_lnglat_by_baidu(keyword)
            if res.status == 0 and res.results:
                lng, lat = res.get("results", [])[0].get("location", {}).get("lng", 0), res.get("results", [])[0].get("location", {}).get("lat", 0)

            if type == "soso":
                res = yield self.hztrip_ds.get_soso_lnglat(lng, lat)
                if res.status == 0 and res.locations:
                    location = res.get("locations", [])[0] if len(res.get("locations", [])) > 0 else {}
                    lng, lat = location.get("lng", 0), location.get("lat", 0)


        return text, lng, lat

    @gen.coroutine
    def do_cancel_bus_line_alert(self, msg):
        """
        退订早晚高峰实时公交订阅
        :param msg:
        :return:
        """

        text = msg.Content.strip()
        if text == "退订":
            keys = self.hztrip_cache.get_hztrip_bus_line_alerts()
            self.logger.debug("all redis key:{}".format(keys))
            title = "【早晚高峰提醒】您有以下订阅"
            description = ''
            url = "https://mp.weixin.qq.com/s/liRLTrncTko3jsbuiJXMWw"
            headimg = ""
            news = wx_const.WX_NEWS_REPLY_HEAD_TPL % (msg.FromUserName,
                                                      msg.ToUserName,
                                                      str(time.time()),
                                                      1)
            example = ''
            for key in keys:
                value = self.hztrip_cache.get_hztrip_bus_line_alert_by_key(key)
                description += "公交: {}   提醒时间: {}\n".format(value['content'], format_hour_minute(value['time']))
                example = value['content']


            description += "\n您在早晚高峰期间查询的实时公交将自动订阅，系统将在第二天提前推送实时公交\n\n" \
                           "退订，请回复退订+内容，如退订{}".format(example)

            item = wx_const.WX_NEWS_REPLY_ITEM_TPL % (
                title,
                description,
                headimg,
                url
            )
            news += item

            news_info = news + wx_const.WX_NEWS_REPLY_FOOT_TPL
            return news_info
        elif text.startswith("退订"):
            content = text.replace("退订", "")
            key = self.hztrip_cache.get_hztrip_bus_line_alert_key(msg.FromUserName, content)
            self.hztrip_cache.del_hztrip_bus_line_alert_by_key(key)
            content = "退订【{}】成功\n若您在早晚高峰期间对同一公交线路手动发起查询，系统将自动调整订阅时间".format(content)
            res = yield self.wx_rep_text(msg, content)
            return res



