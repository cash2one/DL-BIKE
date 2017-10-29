# coding=utf-8

import time
from tornado import gen
from handler.base import BaseHandler
from util.common.decorator import handle_response
from util.common import ObjectDict
from util.tool.date_tool import curr_now
from cache.paper import PaperCache


class PaperHandler(BaseHandler):
    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)

        self.paper_cache = PaperCache()

    @handle_response
    @gen.coroutine
    def get(self, *args, **kwargs):
        """
        paper刷榜
        1. 获得paper的文章 id
        2. 获得点赞得次数
        :param args:
        :param kwargs:
        :return:
        """

        # 获得请求后，拼接 json 数据：
        # 1. 赞次数为 x，则浏览次数为40x
        # 2. 每次刷榜，间隔60分钟
        if not self.params.id or not self.params.zan:
            self.send_json_error(data="请输入文章 id 或点赞数")
            return

        quality = int(self.params.zan) * 40
        jdata = ObjectDict({
            "id": self.params.id,
            "quality": quality,
            "time": time.time(),
        })
        self.paper_cache.set_paper_session(self.params.id, jdata)

        self.send_json_success(data="我知道了，你可以去做其他事了。预计三天后，文章阅读量会上涨{}，点赞数会上涨{}".format(quality, self.params.zan))
