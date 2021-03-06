# coding=utf-8

from tornado import gen
from selenium import webdriver

import conf.path as path
from service.data.base import DataService
from util.common import ObjectDict
from util.tool.http_tool import http_get, http_fetch


class PaperDataService(DataService):
    """
    paper刷榜
    """

    @gen.coroutine
    def add_vote(self, id):
        """
        为文章点赞
        :param id: 文章 id
        :return:
        """
        params = ObjectDict({
            "contentId": id,
        })

        host, port = yield self.get_ip_proxy()

        ret = yield http_fetch(path.PAPER_ADD_VOTE,
                               data=params,
                               proxy_host=host,
                               proxy_port=port)

        raise gen.Return(ret)

    @gen.coroutine
    def read_article(self, id):
        """
        刷文章浏览数
        :param id: 文章 id
        :return:
        """

        host, port = yield self.get_ip_proxy()

        ret = yield http_get(path.PAPER_ARTICLE.format(id),
                               res_json=False,
                               proxy_host=host,
                               proxy_port=port)

        raise gen.Return(ret)

    @gen.coroutine
    def refresh_article(self, id):
        """
        利用selenium刷新网页
        :param id:
        :return:
        """

        host, port = yield self.get_ip_proxy()
        proxy = "{}:{}".format(host,port)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=http://%s' % proxy)
        chrome = webdriver.Chrome(chrome_options=chrome_options)
        chrome.get(path.PAPER_ARTICLE.format(id))

        raise gen.Return(True)
