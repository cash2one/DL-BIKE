# coding=utf-8

'''
:author pyx0622@gmail.com
:date 2017.11.30
:desc 第二天早晚高峰，通知用户实时公交情况
'''

import traceback

from tornado import gen
from tornado.ioloop import IOLoop
from cache.hztrip import HztripCache
from util.tool.date_tool import curr_now
from util.common import ObjectDict
from util.tool.http_tool import http_get

from scripts.parser import Parser


class BusLineAlert(Parser):
    """
    每3分钟运行
    """

    hztrip = HztripCache()

    @gen.coroutine
    def get_bus_line_alerts(self):

        keys = self.hztrip.get_hztrip_bus_line_alerts()
        self.logger.debug("all redis key:{}".format(keys))
        for key in keys:
            value = self.hztrip.get_hztrip_bus_line_alert_by_key(key)
            # 脚本每2分钟运行
            self.logger.debug("start redis key:{} value:{}".format(key, value))
            # 先清除该 redis 记录，避免被其他进程消费
            self.hztrip.del_hztrip_bus_line_alert_by_key(key)
            # for test
            if not value['FromUserName'] == 'o4Ijkjhmjjip2O9Vin2BEay-QoQA':
                continue

            if value['quality'] == 7:
                self.hztrip.set_hztrip_bus_line_alert(value['FromUserName'], value['ToUserName'], value['content'],
                                                      0, alert_time=value['time'] + 24*3600)
                continue

            msg = ObjectDict(
                MsgType='text',
                Content=value['content'],
                FromUserName=value['FromUserName'],
                ToUserName=value['ToUserName']
            )
            news_array = yield self.hztrip_event_ps.do_bus(msg,rsp_array=True)
            self.logger.debug("msg:{}".format(msg))
            self.logger.debug("news_info:{}".format(news_array))
            res = yield self.hztrip_event_ps.wx_custom_send_news(msg, [news_array])
            self.logger.debug("res:{}".format(res))
            self.hztrip.set_hztrip_bus_line_alert(value['FromUserName'], value['ToUserName'], value['content'], value['quality'] + 1, alert_time=value['time'])

    @gen.coroutine
    def runner(self):
        try:
            self.logger.debug("[BusLineAlert]start in:{}".format(curr_now()))
            yield self.get_bus_line_alerts()
        except Exception as e:
            self.logger.error(traceback.format_exc())
        finally:
            IOLoop.instance().stop()
            self.logger.debug("[BusLineAlert]end in:{}".format(curr_now()))


if __name__ == "__main__":
    jp = BusLineAlert()
    jp.runner()
    IOLoop.instance().start()