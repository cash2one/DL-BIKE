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
from cache.pm25 import Pm25Cache
from util.tool.http_tool import http_get

from scripts.parser import Parser

class PM25(Parser):
    """
    pm25每小时更新一次
    """

    pm25 = Pm25Cache()

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
            self.pm25.set_pm25_session(Obj_dict)

    @gen.coroutine
    def runner(self):
        try:
            yield self.get_pm25()
        except Exception as e:
            self.logger.error(traceback.format_exc())

        IOLoop.instance().stop()


if __name__ == "__main__":
    jp = PM25()
    jp.runner()
    IOLoop.instance().start()
