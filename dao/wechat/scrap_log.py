# coding=utf-8
#
# :author pyx0622@gmail.com
# :date 2016.08.13
# :table scrap_log


from dao.base import BaseDao

class ScrapLogDao(BaseDao):

    def __init__(self):
        super(ScrapLogDao, self).__init__()
        self.table = "scrap_log"
        self.fields_map = {
            "id":           self.constant.TYPE_INT,
            "city_id":      self.constant.TYPE_INT, # city.id
            "status":       self.constant.TYPE_INT, # 是否成功，0：否 1：是
            "create_time":  self.constant.TYPE_TIMESTAMP, # 创建时间
        }