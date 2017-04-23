# coding=utf-8
#
# :author pyx0622@gmail.com
# :date 2016.08.13
# :table wypcs110Content

from dao.base import BaseDao

class Wypcs110ContentDao(BaseDao):

    def __init__(self):
        super(Wypcs110ContentDao, self).__init__()
        self.table = "wypcs110Content"
        self.fields_map = {
            "id":          self.constant.TYPE_INT,
            "openid":      self.constant.TYPE_STRING,
            "nickname":    self.constant.TYPE_STRING,
            "sex":         self.constant.TYPE_INT,
            "city":        self.constant.TYPE_STRING,
            "country":     self.constant.TYPE_STRING,
            "province":    self.constant.TYPE_STRING,
            "msgType":     self.constant.TYPE_STRING,
            "event":       self.constant.TYPE_STRING,
            "text":        self.constant.TYPE_STRING,
            "latitude":    self.constant.TYPE_STRING,
            "longitude":   self.constant.TYPE_STRING,
            "label":       self.constant.TYPE_STRING,
            "createTime":  self.constant.TYPE_STRING,
        }