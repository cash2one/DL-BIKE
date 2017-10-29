# coding=utf-8

# @Time    : 28/10/17 15:38
# @Author  : panda (panyuxin@moseeker.com)
# @File    : paper.py
# @DES     :


from app import redis
from app import logger


class PaperCache(object):
    """
    paper session
    """

    def __init__(self):
        super(PaperCache, self).__init__()
        # paper的 session key
        self.paper = "thepaper_{}"
        self.redis = redis

    def get_paper_session(self, id):
        """获得 paper 的 session 信息"""
        paper = self.redis.get(self.paper.format(id))
        return paper

    def get_paper_session_by_key(self, key):
        """获得 paper 的 session 信息"""
        paper = self.redis.get(key, prefix=False)
        return paper

    def get_paper_sessions(self):
        """获得所有带 thpaper 前缀的 session"""
        pattern = "{}_thepaper_*".format(self.redis._PREFIX)
        paper = self.redis.keys(pattern)
        return paper

    def set_paper_session(self, id, value):
        """
        更新 paper 的指定元素的 value
        :param id: id
        :param value: Dict 形式
        :return:
        """

        if not isinstance(value, dict):
            return False

        self.redis.set(self.paper.format(id), value, ttl=3 * 24 * 60 * 60)
        return True

    def del_paper_session(self, id):
        """删除 paper 的 session 信息"""
        self.redis.delete(self.paper.format(id))
        return True
