# coding=utf-8

# @Time    : 2/7/17 15:38
# @Author  : panda (panyuxin@moseeker.com)
# @File    : hztrip.py
# @DES     :


from app import redis
from app import logger
from util.common import ObjectDict


class HztripCache(object):
    """
    hztrip session
    """

    def __init__(self):
        super(HztripCache, self).__init__()
        # pm25 session key
        self.pm25 = "get_pm25"
        self.hztrip_session = "hztrip_{}"
        self.bus_line = "hztrip_bus_line_{}"
        self.bus_stop = "hztrip_bus_stop_{}"
        self.redis = redis

    def get_bus_lines(self, bus_line):
        """获得 bus_line 的 session 信息"""
        key = self.bus_line.format(bus_line)
        bus_line = self.redis.get(key)
        return bus_line

    def set_bus_lines(self, bus_line, value):
        """
        更新bus_line 的指定元素的 value
        :param value: Dict 形式
        :param bus_line:
        :return:
        """

        if not isinstance(value, dict) or not value:
            return False

        key = self.bus_line.format(bus_line)
        # logger.debug(
        #     "[HztripCache] set_bus_lines key:{0} "
        #     "value:{1} type:{2}".format(
        #         key, value, type(value)))

        self.redis.set(key, value, ttl=60*60*24)
        return True

    def get_bus_stops(self, bus_stop):
        """获得 bus_stop 的 session 信息"""
        key = self.bus_stop.format(bus_stop)
        bus_line = self.redis.get(key)
        return bus_line

    def set_bus_stops(self, bus_stop, value):
        """
        bus_stop 的指定元素的 value
        :param value: Dict 形式
        :param bus_stop
        :return:
        """

        if not isinstance(value, dict) or not value:
            return False

        key = self.bus_stop.format(bus_stop)
        # logger.debug(
        #     "[HztripCache] set_bus_stops key:{0} "
        #     "value:{1} type:{2}".format(
        #         key, value, type(value)))

        self.redis.set(key, value, ttl=60*60*24)
        return True

    def get_pm25_session(self):
        """获得 pm25 的 session 信息"""
        pm25 = self.redis.get(self.pm25)
        return pm25

    def set_pm25_session(self, value):
        """
        更新pm25 的指定元素的 value
        :param value: Dict 形式
        :return:
        """

        if not isinstance(value, dict) or not value:
            return False

        # logger.debug(
        #     "[HztripCache] set_pm25_session key:{0} "
        #     "value:{1} type:{2}".format(
        #         self.pm25, value, type(value)))

        self.redis.set(self.pm25, value, ttl=60*60*2)
        return True

    def get_hztrip_session(self, openid):
        """获得 hztrip 的 session 信息"""
        key = self.hztrip_session.format(openid)
        hztrip = self.redis.get(key)
        if hztrip:
            return hztrip.key
        return None

    def set_hztrip_session(self, openid, eventkey):
        """
        更新hztrip 的指定元素的 value
        :param value: Dict 形式
        :return:
        """

        if not openid or not eventkey:
            return False

        value = ObjectDict(
            key=eventkey
        )

        key = self.hztrip_session.format(openid)

        # logger.debug(
        #     "[HztripCache] set_hztrip_session key:{0} "
        #     "value:{1} type:{2}".format(
        #         key, value, type(value)))

        self.redis.set(key, value)
        return True
