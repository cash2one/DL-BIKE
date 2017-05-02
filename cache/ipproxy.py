# coding=utf-8

# @Time    : 2/7/17 15:38
# @Author  : panda (panyuxin@moseeker.com)
# @File    : ipproxy.py
# @DES     :


from app import redis
from app import logger


class IpproxyCache(object):
    """
    iproxy session
    """

    def __init__(self):
        super(IpproxyCache, self).__init__()
        # ipproxy的 session key
        self.ipproxy = "get_ip_proxy"
        self.redis = redis

    def get_ipproxy_session(self):
        """获得 ipproxy 的 session 信息"""
        ipproxy = self.redis.get(self.ipproxy)
        return ipproxy

    def set_ipproxy_session(self, value):
        """
        更新ipproxy 的指定元素的 value
        :param value: Dict 形式
        :return:
        """

        if not isinstance(value, dict) or not value:
            return False

        # logger.debug(
        #     "[IpproxyCache] set_ipproxy_session key:{0} "
        #     "value:{1} type:{2}".format(
        #         self.ipproxy, value, type(value)))

        self.redis.set(self.ipproxy, value, ttl=60*60*6)
        return True

    def del_ipproxy_session(self):
        """删除 ipproxy 的 session 信息"""
        self.redis.delete(self.ipproxy)
        return True
