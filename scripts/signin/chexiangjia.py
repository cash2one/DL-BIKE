# coding=utf-8

'''
:author pyx0622@gmail.com
:date 2017.10.28
:desc chexiang


'''

import random
import time
import traceback

from tornado import gen
from tornado.ioloop import IOLoop
from util.tool.date_tool import curr_now
from util.common import ObjectDict
from util.tool.http_tool import http_get, http_post

from scripts.parser import Parser


class Chexiangjia(Parser):
    """
    每小时更新
    """

    @gen.coroutine
    def get_routine(self):
        """
        每日福利
        :return:
        """

        routine_header = ObjectDict({
            # html 页面 header
            'Host': 'h.jia.chexiang.com',
            'Referer': 'https://h.jia.chexiang.com/cx/cxj/cxjweb/redpack/redpack.shtml?cityName=%E4%B8%8A%E6%B5%B7%E5%B8%82&longitude=121.377015&latitude=31.324592&msgCode=&plateformType=&cityCode=&appVersion=',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'br, gzip, deflate',
            'Accept-Language': 'zh-CN',
            'Content-Type': 'application/json;charset=UTF-8',
            'cookie': 'sc_s=MTAwMDU5ZjczMmY1NWE2ZGQ5ZjUxMDY1MjMwNZPa1JVvyV9odOSfXbwvM6z9jGrb; scookie0=0f55c513821b4625bee0372ec62f520b; scookie1=1509373193032; scookie2=1509373193032; user_trace_cookie=CiCcDln3NQdJ5lSQL/DQAg==; wemall_equid_c=723D3C53-952C-4FF2-8C80-EE0D47788F4B; wemall_openid_c=""; wemall_opentype_c=6; wemall_userkey_c=62882c7f-3644-46d1-ad1c-c8131d339161; analysis_sign=10652305; wemall_cxid_c=10652305; _ga=GA1.2.1080391224.1509372664; _gid=GA1.2.879806854.1509372664; wcid=26D47ADB-80AD-4FAF-BD19-06952B0647E7',
            'User-Agent': '{  "clientId" : "93c36ab85c994b04b184c3653297eaed",  "deviceId" : "723D3C53-952C-4FF2-8C80-EE0D47788F4B",  "appCode" : "MongoToC",  "plateformType" : "ios",  "signature" : "2009CFFC21D78FE8B8C0A0B1E5741ACF",  "origin" : "Mozilla\/5.0 (iPhone; CPU iPhone OS 11_0_3 like Mac OS X) AppleWebKit\/604.1.38 (KHTML, like Gecko) Mobile\/15A432",  "userToken" : "MTAwMDU5ZWNhNzg4NWE2MzRlODgxMDY1MjMwNSLkvLka68lia3_un5ki1aVctZjN",  "sourceCode" : "APPStore",  "deviceManufacturer" : "iPhone",  "appVersion" : "4.3.1",  "userAccount" : "17621856713",  "signVersion" : "0.2"}',
        })

        jdata = ObjectDict({
            'currentCity': '上海',
            'activityCode': 'ATTLB01'
        })

        res = yield http_post("http://h.jia.chexiang.com/daily/list/0.htm", jdata, headers=routine_header)
        self.logger.debug("get_routine res:{}".format(res))
        for store in res.obj:
            yield self.get_redpacket(store['prizeCode'], store['storeId'])

    @gen.coroutine
    def get_redpacket(self, prize_code, store_id):
        """
        领福利
        :return:
        """

        header = ObjectDict({
            # html 页面 header
            'Host': 'h.jia.chexiang.com',
            'Referer': 'https://h.jia.chexiang.com/cx/cxj/cxjweb/redpack/redpack.shtml?cityName=%E4%B8%8A%E6%B5%B7%E5%B8%82&longitude=121.377015&latitude=31.324592&msgCode=&plateformType=&cityCode=&appVersion=',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'br, gzip, deflate',
            'Accept-Language': 'zh-CN',
            'Content-Type': 'application/json;charset=UTF-8',
            'cookie': 'sc_s=MTAwMDU5ZjczMmY1NWE2ZGQ5ZjUxMDY1MjMwNZPa1JVvyV9odOSfXbwvM6z9jGrb; scookie0=0f55c513821b4625bee0372ec62f520b; scookie1=1509373193032; scookie2=1509373193032; user_trace_cookie=CiCcDln3NQdJ5lSQL/DQAg==; wemall_equid_c=723D3C53-952C-4FF2-8C80-EE0D47788F4B; wemall_openid_c=""; wemall_opentype_c=6; wemall_userkey_c=62882c7f-3644-46d1-ad1c-c8131d339161; analysis_sign=10652305; wemall_cxid_c=10652305; _ga=GA1.2.1080391224.1509372664; _gid=GA1.2.879806854.1509372664; wcid=26D47ADB-80AD-4FAF-BD19-06952B0647E7',
            'User-Agent': '{  "clientId" : "93c36ab85c994b04b184c3653297eaed",  "deviceId" : "723D3C53-952C-4FF2-8C80-EE0D47788F4B",  "appCode" : "MongoToC",  "plateformType" : "ios",  "signature" : "2009CFFC21D78FE8B8C0A0B1E5741ACF",  "origin" : "Mozilla\/5.0 (iPhone; CPU iPhone OS 11_0_3 like Mac OS X) AppleWebKit\/604.1.38 (KHTML, like Gecko) Mobile\/15A432",  "userToken" : "MTAwMDU5ZWNhNzg4NWE2MzRlODgxMDY1MjMwNSLkvLka68lia3_un5ki1aVctZjN",  "sourceCode" : "APPStore",  "deviceManufacturer" : "iPhone",  "appVersion" : "4.3.1",  "userAccount" : "17621856713",  "signVersion" : "0.2"}',
        })

        jdata = ObjectDict({
            'prizeCode': prize_code,
            'actFlag': 0,
            'storeId': store_id,
            'currentUrl': 'https://h.jia.chexiang.com/cx/cxj/cxjweb/redpack/redpack.shtml?cityName=%E4%B8%8A%E6%B5%B7%E5%B8%82&longitude=121.377034&latitude=31.324527&msgCode=&plateformType=&cityCode=&appVersion='
        })

        res = yield http_post("https://h.jia.chexiang.com/daily/receive.htm", jdata, headers=header)

        self.logger.debug("get_redpacket res:{}".format(res))

    @gen.coroutine
    def get_jufengyuan(self):
        """
        聚丰园路活动
        :return:
        """

        routine_header = ObjectDict({
            # html 页面 header
            'Host': 'h.jia.chexiang.com',
            'Referer': 'https://h.jia.chexiang.com/cx/cxj/cxjweb/redpack/redpack.shtml?cityName=%E4%B8%8A%E6%B5%B7%E5%B8%82&longitude=121.377015&latitude=31.324592&msgCode=&plateformType=&cityCode=&appVersion=',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'br, gzip, deflate',
            'Accept-Language': 'zh-CN',
            'Content-Type': 'application/json;charset=UTF-8',
            'cookie': 'sc_s=MTAwMDU5ZWNhNzg4NWE2MzRlODgxMDY1MjMwNSLkvLka68lia3_un5ki1aVctZjN; scookie0=284d2b4230ee4a9fb4368bbaa817357e; scookie1=1509278647398; scookie2=1509278647398; user_trace_cookie=CiCcQFn1w7ZBhSEhLC7ZAg==; wemall_equid_c=723D3C53-952C-4FF2-8C80-EE0D47788F4B; wemall_openid_c=""; wemall_opentype_c=6; wemall_userkey_c=1b16cfc3-de9d-4b47-83e4-394987e54452; COOKIE_USER_CARD_CITYID=310100; _ga=GA1.2.1017692364.1508681626; COOKIE_USER_CARD_CITYID=310100; analysis_sign=10652305; wemall_cxid_c=10652305; wcid=08A1DE46-CBFF-4960-AEAC-E4037E1A3E36',
            'User-Agent': '{  "clientId" : "93c36ab85c994b04b184c3653297eaed",  "deviceId" : "723D3C53-952C-4FF2-8C80-EE0D47788F4B",  "appCode" : "MongoToC",  "plateformType" : "ios",  "signature" : "2009CFFC21D78FE8B8C0A0B1E5741ACF",  "origin" : "Mozilla\/5.0 (iPhone; CPU iPhone OS 11_0_3 like Mac OS X) AppleWebKit\/604.1.38 (KHTML, like Gecko) Mobile\/15A432",  "userToken" : "MTAwMDU5ZWNhNzg4NWE2MzRlODgxMDY1MjMwNSLkvLka68lia3_un5ki1aVctZjN",  "sourceCode" : "APPStore",  "deviceManufacturer" : "iPhone",  "appVersion" : "4.3.1",  "userAccount" : "17621856713",  "signVersion" : "0.2"}',
        })

        jdata = ObjectDict({
            'locationCity': '上海',
            'currentCity': '上海市',
            'Y': '121.366928',
            'X': '31.313469',
            'activityCode': 'ATTLB01',
        })

        res = yield http_post("https://h.jia.chexiang.com/daily/list/1.htm", jdata, headers=routine_header)
        self.logger.debug("get_jufengyuan res:{}".format(res))
        for store in res.obj:
            yield self.get_redpacket(store['prizeCode'], store['storeId'])

    @gen.coroutine
    def runner(self):
        try:
            self.logger.debug("[chexiangjia]start in:{}".format(curr_now()))
            # yield self.get_routine()
            yield self.get_jufengyuan()
        except Exception as e:
            self.logger.error(traceback.format_exc())
        finally:
            IOLoop.instance().stop()
            self.logger.debug("[chexiangjia]end in:{}".format(curr_now()))


if __name__ == "__main__":
    jp = Chexiangjia()
    jp.runner()
    IOLoop.instance().start()
