# coding=utf-8

'''
:author pyx0622@gmail.com
:date 2017.10.28
:desc chexiang


'''

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
        每日福利列表
        :return:
        """

        routine_header = ObjectDict({
            # html 页面 header
            'Host': 'cxj.activity.chexiang.com',
            'Referer': 'https://cxj.activity.chexiang.com/cx/cxj/cxjappweb/welfare/index.shtml',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'br, gzip, deflate',
            'Accept-Language': 'zh-CN',
            'Content-Type': 'application/json;charset=UTF-8',
            'cookie': 'user_trace_cookie=CiCcIloRcyFtlXYEZEWIAg==; wemall_equid_c=723D3C53-952C-4FF2-8C80-EE0D47788F4B; wemall_openid_c=""; wemall_opentype_c=6; wemall_userkey_c=62882c7f-3644-46d1-ad1c-c8131d339161; analysis_sign=10652305; wemall_cxid_c=10652305; _ga=GA1.2.1080391224.1509372664; wcid=26D47ADB-80AD-4FAF-BD19-06952B0647E7',
            'User-Agent': '{  "clientId" : "93c36ab85c994b04b184c3653297eaed",  "deviceId" : "723D3C53-952C-4FF2-8C80-EE0D47788F4B",  "appCode" : "MongoToC",  "plateformType" : "ios",  "signature" : "C5A6EF5B83B374489C7F8BD23C59FB68",  "origin" : "Mozilla\/5.0 (iPhone; CPU iPhone OS 11_1_2 like Mac OS X) AppleWebKit\/604.3.5 (KHTML, like Gecko) Mobile\/15B202",  "userToken" : "MTAwMDU5ZjczMmY1NWE2ZGQ5ZjUxMDY1MjMwNZPa1JVvyV9odOSfXbwvM6z9jGrb",  "sourceCode" : "APPStore",  "deviceManufacturer" : "iPhone",  "appVersion" : "4.4",  "userAccount" : "17621856713",  "signVersion" : "0.2"}',
        })

        jdata = ObjectDict({
            'currentCity': '上海市',
            'longitude': '121.326199',
            'latitude': '31.134585',
        })

        res = yield http_post("https://cxj.activity.chexiang.com/service/dailyfuli/list/0", jdata, headers=routine_header)
        for store in res.obj.dailyFuliVos:
            yield self.get_dailyredpacket(store['prizeCode'])

    @gen.coroutine
    def get_dailyredpacket(self, prize_code):
        """
        每日福利领取
        :param prize_code:
        :return:
        """

        header = ObjectDict({
            # html 页面 header
            'Host': 'cxj.activity.chexiang.com',
            'Referer': 'https://cxj.activity.chexiang.com/cx/cxj/cxjappweb/welfare/index.shtml',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'br, gzip, deflate',
            'Accept-Language': 'zh-CN',
            'Content-Type': 'application/json;charset=UTF-8',
            'cookie': 'scookie0=78d482c639d244488b56725b2e776d87; scookie1=1511092804876; scookie2=1511092804876; user_trace_cookie=CiCcIloRckNshXYFZJoDAg==; wemall_equid_c=723D3C53-952C-4FF2-8C80-EE0D47788F4B; wemall_openid_c=""; wemall_opentype_c=6; wemall_userkey_c=62882c7f-3644-46d1-ad1c-c8131d339161; analysis_sign=10652305; wemall_cxid_c=10652305; _ga=GA1.2.1080391224.1509372664; wcid=26D47ADB-80AD-4FAF-BD19-06952B0647E7',
            'User-Agent': '{  "clientId" : "93c36ab85c994b04b184c3653297eaed",  "deviceId" : "723D3C53-952C-4FF2-8C80-EE0D47788F4B",  "appCode" : "MongoToC",  "plateformType" : "ios",  "signature" : "C5A6EF5B83B374489C7F8BD23C59FB68",  "origin" : "Mozilla\/5.0 (iPhone; CPU iPhone OS 11_1_2 like Mac OS X) AppleWebKit\/604.3.5 (KHTML, like Gecko) Mobile\/15B202",  "userToken" : "MTAwMDU5ZjczMmY1NWE2ZGQ5ZjUxMDY1MjMwNZPa1JVvyV9odOSfXbwvM6z9jGrb",  "sourceCode" : "APPStore",  "deviceManufacturer" : "iPhone",  "appVersion" : "4.4",  "userAccount" : "17621856713",  "signVersion" : "0.2"}',
        })

        yield http_get("https://cxj.activity.chexiang.com/service/dailyfuli/receive?prizeCode={}".format(prize_code), headers=header)

    @gen.coroutine
    def get_redpacket(self, item_id, store_id):
        """
        门店福利领福利
        :return:
        """

        header = ObjectDict({
            # html 页面 header
            'Host': 'cxj.activity.chexiang.com',
            'Referer': 'https://cxj.activity.chexiang.com/cx/cxj/cxjappweb/welfare/index.shtml',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'br, gzip, deflate',
            'Accept-Language': 'zh-CN',
            'Content-Type': 'application/json;charset=UTF-8',
            'cookie': 'bbbbbbbbbbbbbbb=OJNGAMEFOFMEDDFMCNGGPFPNMNNMGCOIOGPGFOHMHDEDJKHHHHNHMMAGGONAPFCFNGAFIJIIKIPJAHBJIHJLMPDLGBMNCAFPNBKOFBEKGGNDEKCABODHCPJAAIFINBHI; scookie2=1511093976210; sc_s=MTAwMDU5ZjczMmY1NWE2ZGQ5ZjUxMDY1MjMwNZPa1JVvyV9odOSfXbwvM6z9jGrb; scookie0=e58e265eaa1d4f649e7979535c13e11b; scookie1=1511093025936; user_trace_cookie=CiCcIloRcyFtlXYEZEWIAg==; wemall_equid_c=723D3C53-952C-4FF2-8C80-EE0D47788F4B; wemall_openid_c=""; wemall_opentype_c=6; wemall_userkey_c=62882c7f-3644-46d1-ad1c-c8131d339161; analysis_sign=10652305; wemall_cxid_c=10652305; _ga=GA1.2.1080391224.1509372664; wcid=26D47ADB-80AD-4FAF-BD19-06952B0647E7',
            'User-Agent': '{  "clientId" : "93c36ab85c994b04b184c3653297eaed",  "deviceId" : "723D3C53-952C-4FF2-8C80-EE0D47788F4B",  "appCode" : "MongoToC",  "plateformType" : "ios",  "signature" : "C5A6EF5B83B374489C7F8BD23C59FB68",  "origin" : "Mozilla\/5.0 (iPhone; CPU iPhone OS 11_1_2 like Mac OS X) AppleWebKit\/604.3.5 (KHTML, like Gecko) Mobile\/15B202",  "userToken" : "MTAwMDU5ZjczMmY1NWE2ZGQ5ZjUxMDY1MjMwNZPa1JVvyV9odOSfXbwvM6z9jGrb",  "sourceCode" : "APPStore",  "deviceManufacturer" : "iPhone",  "appVersion" : "4.4",  "userAccount" : "17621856713",  "signVersion" : "0.2"}'
        })

        res = yield http_get("https://cxj.activity.chexiang.com/service/fuliv2/luck?itemId={0}&storeId={1}".format(item_id, store_id), headers=header)

    @gen.coroutine
    def get_jufengyuan(self):
        """
        聚丰园路活动列表
        :return:
        """

        routine_header = ObjectDict({
            # html 页面 header
            'Host': 'cxj.activity.chexiang.com',
            'Referer': 'https://cxj.activity.chexiang.com/cx/cxj/cxjappweb/welfare/index.shtml',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'br, gzip, deflate',
            'Accept-Language': 'zh-CN',
            'Content-Type': 'application/json;charset=UTF-8',
            'cookie': 'sc_s=MTAwMDU5ZjczMmY1NWE2ZGQ5ZjUxMDY1MjMwNZPa1JVvyV9odOSfXbwvM6z9jGrb; scookie0=e58e265eaa1d4f649e7979535c13e11b; scookie1=1511093025936; scookie2=1511093025936; user_trace_cookie=CiCcIloRcyFtlXYEZEWIAg==; wemall_equid_c=723D3C53-952C-4FF2-8C80-EE0D47788F4B; wemall_openid_c=""; wemall_opentype_c=6; wemall_userkey_c=62882c7f-3644-46d1-ad1c-c8131d339161; analysis_sign=10652305; wemall_cxid_c=10652305; _ga=GA1.2.1080391224.1509372664; wcid=26D47ADB-80AD-4FAF-BD19-06952B0647E7',
            'User-Agent': '{  "clientId" : "93c36ab85c994b04b184c3653297eaed",  "deviceId" : "723D3C53-952C-4FF2-8C80-EE0D47788F4B",  "appCode" : "MongoToC",  "plateformType" : "ios",  "signature" : "C5A6EF5B83B374489C7F8BD23C59FB68",  "origin" : "Mozilla\/5.0 (iPhone; CPU iPhone OS 11_1_2 like Mac OS X) AppleWebKit\/604.3.5 (KHTML, like Gecko) Mobile\/15B202",  "userToken" : "MTAwMDU5ZjczMmY1NWE2ZGQ5ZjUxMDY1MjMwNZPa1JVvyV9odOSfXbwvM6z9jGrb",  "sourceCode" : "APPStore",  "deviceManufacturer" : "iPhone",  "appVersion" : "4.4",  "userAccount" : "17621856713",  "signVersion" : "0.2"}',
        })

        res = yield http_get("https://cxj.activity.chexiang.com/service/fuliv2/getStoreSchemeItem?storeId=&longitude=121.373299&latitude=31.312585&cityName=%E4%B8%8A%E6%B5%B7%E5%B8%82", headers=routine_header)
        for item in res.obj.get('items'):
            yield self.get_redpacket(item['sid'], res.obj.store.storeId)

    @gen.coroutine
    def runner(self):
        try:
            self.logger.debug("[chexiangjia]start in:{}".format(curr_now()))
            yield self.get_routine()
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
