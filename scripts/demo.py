# coding=utf-8

'''
:author pyx0622@gmail.com
:date 2016.08.13
:desc 北京租赁点抓取脚本

    由百度 place api 获得 POI 经纬度，再根据叮嗒出行的经纬度列表接口，由这些经纬度查询所有公共自行车租赁点

'''
import time
import traceback

from tornado import gen
from tornado.ioloop import IOLoop

from scripts.bikestation.parser import Parser

# 北京
CITY_ID = 11000


class Demo(Parser):
    """
    北京租赁点抓取，包括市区，郊县。数据来自北京市公共自行车官方客户端
    """

    @gen.coroutine
    def get_demo(self):

        ips = yield self.infra_ps.get_beijing_nearby(120, 30)
        print (ips)

    @gen.coroutine
    def main(self):
        try:
            yield self.get_demo()
        except Exception as e:
            self.logger.error(traceback.format_exc())

    @gen.coroutine
    def async_sleep(self, timeout):
        # Sleep without blocking the IOLoop
        yield gen.Task(IOLoop.instance().add_timeout, time.time() + timeout)

    def close(self):
        IOLoop.instance().stop()

    @gen.coroutine
    def runner(self):
        yield self.main()
        self.close()


if __name__ == "__main__":
    jp = Demo()
    jp.runner()
    IOLoop.instance().start()
