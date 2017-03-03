# coding=utf-8

'''
:author pyx0622@gmail.com
:date 2016.08.13
:desc 江苏南京租赁点抓取脚本

    由百度 place api 获得 POI 经纬度，再根据叮嗒出行的经纬度列表接口，由这些经纬度查询所有公共自行车租赁点

'''
import time
import traceback

from tornado import gen
from tornado.ioloop import IOLoop
from tornado.util import ObjectDict

from bike.scripts.parser import Parser

# 南京
CITY_ID = 32001
SID = 5


class JiangsunanjingParser(Parser):
    """
    数据来自南京公共自行车微信号
    """

    @gen.coroutine
    def get_stations(self):

        data_list = yield self.infra_ps.get_nanjing_list()
        if data_list.get("netword"):
            for item in data_list.get("netword"):
                station = ObjectDict()
                station['code'] = str(item.get('networdId'))
                station['status'] = self.const.STATUS_INUSE
                # station['type'] = ""
                # station['total'] = ""
                station['name'] = item['networdName']
                # station['address'] = ""
                # station['district'] = ""
                station['longitude'] = item["jd"]
                station['latitude'] = item["wd"]
                # station['service_time'] = ""
                # station['is_24'] = ""
                # station['is_duty'] = ""
                print (station)
                yield self.update_station(station)
        print ("end")
        raise gen.Return(True)

    @gen.coroutine
    def main(self):
        try:
            yield self.get_stations()
        except Exception as e:
            self.logger.error(traceback.format_exc())
            # 增加抓取记录 log
            yield self.scraplog_ps.add_scrap_log(fields={
                "cid": CITY_ID,
                "status": self.const.STATUS_UNUSE,
            })

    @gen.coroutine
    def update_station(self, item):

        """
        增加或更新数据库中租赁点信息
        :param station:
        :return:
        """
        station = yield self.station_ps.get_station(conds={
            "code": item.code,
            "cid": CITY_ID,
            "sid": SID,
        })
        if station:
            # 存在，则更新
            self.station_ps.update_station(
                conds={
                    "id": station.id
                },
                fields={
                    "status": item.status,
                    # "total": item.total,
                    "name": item.name,
                    # "address": item.address,
                    # "district": item.district,
                    # "district_id": item.district_id,
                    "longitude": item.longitude,
                    "latitude": item.latitude
                }
            )
        else:
            # 不存在，则增加
            yield self.station_ps.add_station(fields={
                "code": item.code,
                "cid": CITY_ID,
                "sid": SID,
                "status": item.status,
                # "total": item.total,
                "name": item.name,
                # "address": item.address,
                # "district": item.district,
                # "district_id": item.district_id,
                "longitude": item.longitude,
                "latitude": item.latitude
            })

    @gen.coroutine
    def async_sleep(self, timeout):
        # Sleep without blocking the IOLoop
        yield gen.Task(IOLoop.instance().add_timeout, time.time() + timeout)

    def close(self):
        IOLoop.instance().stop()
        # 增加抓取记录 log
        yield self.scraplog_ps.add_scrap_log(fields={
            "cid": CITY_ID,
            "status": self.const.STATUS_INUSE,
        })

    @gen.coroutine
    def runner(self):
        yield self.main()
        self.close()


if __name__ == "__main__":
    jp = JiangsunanjingParser()
    jp.runner()
    IOLoop.instance().start()
