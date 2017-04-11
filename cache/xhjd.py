# coding=utf-8

# @Time    : 2/7/17 15:38
# @Author  : panda (panyuxin@moseeker.com)
# @File    : xhjd.py
# @DES     :

from app import redis
from app import logger
from util.common import ObjectDict


class XhjdCache(object):
    """
    xhjd session
    """

    def __init__(self):
        super(XhjdCache, self).__init__()
        # pm25 session key
        self.xhjd_session = "xhjd_{}"
        self.redis = redis

    def get_xhjd_session(self, openid):
        """获得 xhjd 的 session 信息"""
        key = self.xhjd_session.format(openid)
        xhjd = self.redis.get(key)
        if xhjd:
            return xhjd.key
        return None

    def set_xhjd_session(self, openid, eventkey):
        """
        更新xhjd 的指定元素的 value
        :param value: Dict 形式
        :return:
        """

        if not openid or not eventkey:
            return False

        value = ObjectDict(
            key=eventkey
        )

        key = self.xhjd_session.format(openid)

        logger.debug(
            "[XhjdCache] set_xhjd_session key:{0} "
            "value:{1} type:{2}".format(
                key, value, type(value)))

        self.redis.set(key, value)
        return True
