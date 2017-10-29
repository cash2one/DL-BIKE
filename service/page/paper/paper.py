# coding=utf-8

from tornado import gen
from service.page.base import PageService

class PaperPageService(PageService):

    @gen.coroutine
    def add_vote(self, id):
        """
        为文章点赞
        :param id:
        :return:
        """

        ret = yield self.paper_ds.add_vote(id)
        raise gen.Return(ret)

    @gen.coroutine
    def read_article(self, id):
        """
        刷文章浏览数
        :param id:
        :return:
        """

        ret = yield self.paper_ds.read_article(id)
        raise gen.Return(ret)
