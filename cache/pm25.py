# coding=utf-8

# @Time    : 2/7/17 15:38
# @Author  : panda (panyuxin@moseeker.com)
# @File    : pm25.py
# @DES     :


from app import redis
from app import logger


class Pm25Cache(object):
    """
    iproxy session
    """

    def __init__(self):
        super(Pm25Cache, self).__init__()
        # pm25 session key
        self.pm25 = "get_pm25"
        self.redis = redis

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

        logger.debug(
            "[Pm25Cache] set_pm25_session key:{0} "
            "value:{1} type:{2}".format(
                self.pm25, value, type(value)))

        self.redis.set(self.pm25, value, ttl=60*60*2)
        return True
