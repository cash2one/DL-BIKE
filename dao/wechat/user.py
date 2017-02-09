# coding=utf-8
#
# :author pyx0622@gmail.com
# :date 2016.08.13
# :table user


from dao.base import BaseDao

class UserDao(BaseDao):

    def __init__(self):
        super(UserDao, self).__init__()
        self.table = "user"
        self.fields_map = {
            "id":                 self.constant.TYPE_INT,
            "is_subscribe":       self.constant.TYPE_INT, # 是否关注 0：否 1：是
            "openid":             self.constant.TYPE_STRING, # 用户openid
            "nickname":           self.constant.TYPE_STRING, # 用户昵称
            "sex":                self.constant.TYPE_INT, # 用户性别 0：未知 1：男性 2：女性
            "city":               self.constant.TYPE_STRING, # 用户所在城市
            "country":            self.constant.TYPE_STRING, # 用户所在国家
            "province":           self.constant.TYPE_STRING, # 用户所在省份
            "language":           self.constant.TYPE_STRING, # 用户语言
            "headimg":            self.constant.TYPE_STRING, # 用户头像
            "subscribe_time":     self.constant.TYPE_TIMESTAMP, # 用户关注时间
            "unsubscibe_time":    self.constant.TYPE_TIMESTAMP, # 用户取消关注时间
            "create_time":        self.constant.TYPE_TIMESTAMP, # 创建时间
            "update_time":        self.constant.TYPE_TIMESTAMP, # 更新时间
        }