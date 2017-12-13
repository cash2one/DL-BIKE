# coding=utf-8

'''
:author pyx0622@gmail.com
:date 2017.11.30
:desc 向摇号未中签的用户发送福利广告
'''

import traceback
import redis
import json

from tornado import gen
from tornado.ioloop import IOLoop
from setting import settings
from cache.hztrip import HztripCache
from util.tool.date_tool import curr_now
from util.tool.str_tool import to_str
from util.common import ObjectDict

from scripts.parser import Parser


class PublishAds(Parser):
    """
    每3分钟运行
    """

    hztrip = HztripCache()
    _pool = redis.ConnectionPool(
        host=settings["store_options"]["redis_host"],
        port=settings["store_options"]["redis_port"],
        max_connections=settings["store_options"]["max_connections"])
    _redis = redis.StrictRedis(connection_pool=_pool)
    p = _redis.pubsub()

    @gen.coroutine
    def get_pubsub(self):

        self.p.subscribe(self.const.CHANNEL_ADS)
        for item in self.p.listen():
            print(item)
            if item['type'] == 'message':
                data = item['data']
                content = json.loads(to_str(data))
                print(content)
                msg = ObjectDict(
                    FromUserName=content.from_username,
                    ToUserName=content.to_username,
                )

                if content.from_username == 'o4Ijkjhmjjip2O9Vin2BEay-QoQA':
                    res = yield self.hztrip_event_ps.wx_rep_text(msg, self.const.ADS_CONTENT)
                    print(111)
                    print(res)

    @gen.coroutine
    def runner(self):
        try:
            self.logger.debug("[PublishAds]start in:{}".format(curr_now()))
            yield self.get_pubsub()
        except Exception as e:
            self.logger.error(traceback.format_exc())
        finally:
            self.p.unsubscribe(self.const.CHANNEL_ADS)
            IOLoop.instance().stop()
            self.logger.debug("[PublishAds]end in:{}".format(curr_now()))


if __name__ == "__main__":
    jp = PublishAds()
    jp.runner()
    IOLoop.instance().start()
