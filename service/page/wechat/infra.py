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
    def get_ip_proxy(self, count=5, types=0, protocol=1, country='国内'):
        """
        获得代理 IP
        :param count: 数量
        :param types: 0: 高匿,1:匿名,2 透明
        :param protocol: 0: http, 1 https, 2 http/https
        :param country: 取值为国内, 国外
        :return:
        """

        ret = yield self.infra_ds.get_ip_proxy(count, types, protocol, country)
        raise gen.Return(ret)

    @gen.coroutine
    def del_ip_proxy(self, ip):
        """
        删除无效的代理 IP
        :param ip: 类似192.168.1.1
        :return:
        """

        ret = yield self.infra_ds.del_ip_proxy(ip)
        raise gen.Return(ret)
