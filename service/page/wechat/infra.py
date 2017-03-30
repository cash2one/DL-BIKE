# coding=utf-8

from tornado import gen
from service.page.base import PageService
from util.common import ObjectDict

class InfraPageService(PageService):

    @gen.coroutine
    def get_city_poi(self, q, region, tag, page_num, coord_type=3, page_size=10):
        """
        获得百度 Place api 提供的城市poi 信息
        :param q:
        :param region:
        :param tag:
        :param page_num:
        :param coord_type:
        :param page_size:
        :return:
        """

        ret = yield self.infra_ds.get_city_poi(q, region, tag, page_num, coord_type, page_size)
        raise gen.Return(ret)

    @gen.coroutine
    def get_dingda_nearby(self, longitude, latitude):
        """
        叮嗒出行，获得附近租赁点列表
        :param longitude:
        :param latitude:
        :return:
        """

        ret = yield self.infra_ds.get_dingda_nearby(longitude, latitude)
        raise gen.Return(ret)

    @gen.coroutine
    def get_beijing_nearby(self, longitude, latitude):
        """
        北京公共自行车，获得附近租赁点列表
        :param longitude:
        :param latitude:
        :return:
        """

        ret = yield self.infra_ds.get_beijing_nearby(longitude, latitude)
        raise gen.Return(ret)

    @gen.coroutine
    def get_xian_nearby(self, longitude, latitude):
        """
        西安公共自行车，获得附近租赁点列表
        :param longitude:
        :param latitude:
        :return:
        """

        ret = yield self.infra_ds.get_xian_nearby(longitude, latitude)
        raise gen.Return(ret)

    @gen.coroutine
    def get_nanjing_list(self):
        """
        南京公共自行车，获得附近租赁点列表
        :return:
        """

        ret = yield self.infra_ds.get_nanjing_list()
        raise gen.Return(ret)
