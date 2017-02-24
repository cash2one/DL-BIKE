# coding=utf-8

# :author pyx0622@gmail.com
# :date 2016.08.13
# :table station


from dao.base import BaseDao

class StationDao(BaseDao):

    def __init__(self):
        super(StationDao, self).__init__()
        self.table = "station"
        self.fields_map = {
            "id":               self.constant.TYPE_INT,
            "cid":              self.constant.TYPE_INT, # city.cid
            "code":             self.constant.TYPE_STRING, # 租赁点编号
            "type":             self.constant.TYPE_STRING, # 租赁点类型
            "status":           self.constant.TYPE_INT, # 是否有效，0：否 1：是
            "total":            self.constant.TYPE_INT, # 总车位数
            "name":             self.constant.TYPE_STRING, # 租赁点名称
            "address":          self.constant.TYPE_STRING, # 租赁点地址
            "rid":              self.constant.TYPE_STRING, # 租赁点城区id, region.rid
            "longitude":        self.constant.TYPE_STRING, # 租赁点经度（百度系）
            "latitude":         self.constant.TYPE_STRING, # 租赁点纬度（百度系）
            "telephone":        self.constant.TYPE_STRING, # 联系电话
            "service_time":     self.constant.TYPE_STRING, # 服务时间
            "is_24":            self.constant.TYPE_INT, # 是否24小时 0：否 1：是
            "is_duty":          self.constant.TYPE_INT, # 是否有人值守 0：否 1：是
            "create_time":      self.constant.TYPE_TIMESTAMP, # 创建时间
            "update_time":      self.constant.TYPE_TIMESTAMP, # 更新时间
        }