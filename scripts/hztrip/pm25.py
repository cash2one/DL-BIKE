# coding=utf-8

'''
:author pyx0622@gmail.com
:date 2016.08.13
:desc 获得 PM25数据


'''

import traceback

from tornado import gen
from tornado.ioloop import IOLoop
from tornado.util import ObjectDict
from cache.hztrip import HztripCache
from util.tool.http_tool import http_get
from util.tool.date_tool import curr_datetime_now

from scripts.parser import Parser

class PM25(Parser):
    """
    pm25每小时更新一次
    """

    hztrip = HztripCache()

    @gen.coroutine
    def get_pm25(self):

        res = yield http_get("http://www.pm25.in/api/querys/all_cities.json?token=dSL6xvEWvyYxTeAX4Wyy", timeout=60)

        Obj_dict = ObjectDict()
        for item in res:
            city = item['area']
            if not isinstance(Obj_dict.get(city, None), list):
                Obj_dict[city] = list()
                Obj_dict[city].append(item)
            else:
                Obj_dict[city].append(item)

        if Obj_dict:
            self.hztrip.set_pm25_session(Obj_dict)

    @gen.coroutine
    def runner(self):
        print ("[{}]pm25 start".format(curr_datetime_now()))
        try:
            yield self.get_pm25()
        except Exception as e:
            self.logger.error(traceback.format_exc())

        print("[{}]pm25 end".format(curr_datetime_now()))
        IOLoop.instance().stop()


if __name__ == "__main__":
    jp = PM25()
    jp.runner()
    IOLoop.instance().start()
