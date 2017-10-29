# coding=utf-8

'''
:author pyx0622@gmail.com
:date 2017.10.28
:desc paper 刷榜


'''

import random
import time
import traceback

from tornado import gen
from tornado.ioloop import IOLoop
from cache.paper import PaperCache
from util.tool.date_tool import curr_now

from scripts.parser import Parser


class Paper(Parser):
    """
    pm25每小时更新一次
    """

    paper = PaperCache()

    @gen.coroutine
    def get_papers(self):

        keys = self.paper.get_paper_sessions()
        for key in keys:
            value = self.paper.get_paper_session_by_key(key)
            if time.time() - value['time'] >= 60 * 30:
                # 每隔半小时运行一次
                # 根据刷榜次数得出每次刷榜次数
                self.logger.debug("redis key:{} value:{}".format(key, value))
                degree = round(value['quality'] / (3 * 24 * 2))
                self.logger.debug("degree:{}".format(degree))
                i = 0
                while i < degree:
                    read_ret = yield self.paper_ps.read_article(value['id'])

                    if i % 2 == 0:
                        vote_ret = yield self.paper_ps.add_vote(value['id'])
                        self.logger.debug("add_vote ret:{}".format(vote_ret))
                    # 刷榜成功才计数
                    if read_ret:
                        i += 1
                    time.sleep(random.randint(0, 20))

    @gen.coroutine
    def runner(self):
        try:
            self.logger.debug("[paper]start in:{}".format(curr_now()))
            yield self.get_papers()
        except Exception as e:
            self.logger.error(traceback.format_exc())
        finally:
            IOLoop.instance().stop()
            self.logger.debug("[paper]end in:{}".format(curr_now()))


if __name__ == "__main__":
    jp = Paper()
    jp.runner()
    IOLoop.instance().start()
