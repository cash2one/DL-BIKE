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
            "17621856713": ObjectDict({
                'Host': 'cxj.activity.chexiang.com',
                'Referer': 'https://cxj.activity.chexiang.com/cx/cxj/cxjappweb/welfare/index.shtml',
                'X-Requested-With': 'XMLHttpRequest',
                'Accept-Encoding': 'br, gzip, deflate',
                'Accept-Language': 'zh-CN',
                'Content-Type': 'application/json;charset=UTF-8',
                'cookie': 'bbbbbbbbbbbbbbb=CEMAODLNGENADMNJCNMIBNNAEFIPDGBDLADHMOJACFIDADLFFPMFBAILLNMAAKMHHNNFLPEPOEKKKMIKCJGEKLCAEGLHKOGGLEJLLAEHMGMMAJNHKDFIGFIJJJMCCANH; scookie2=1513004402087; scookie0=eb0695d4223845879ecc7197239e73fb; scookie1=1513004392073; user_trace_cookie=CiCcQFounWZuaGOTL7/+Ag==; analysis_sign=10652305; wemall_cxid_c=10652305; wemall_equid_c=723D3C53-952C-4FF2-8C80-EE0D47788F4B; wemall_openid_c=""; wemall_opentype_c=6; wemall_userkey_c=29a04582-23c3-42cd-a92d-0337570a09ed; wcid=8D0A3F22-BCFF-4CA5-8F26-CBCC151A8200',
                'User-Agent': '{  "clientId" : "93c36ab85c994b04b184c3653297eaed",  "deviceId" : "723D3C53-952C-4FF2-8C80-EE0D47788F4B",  "appCode" : "MongoToC",  "plateformType" : "ios",  "signature" : "250C6C58ED3FC8F7550E33A755DABD80",  "origin" : "Mozilla\/5.0 (iPhone; CPU iPhone OS 11_1_2 like Mac OS X) AppleWebKit\/604.3.5 (KHTML, like Gecko) Mobile\/15B202",  "userToken" : "MTAwMDVhMmU5Y2ZiNWFhNTQzZmIxMDY1MjMwNWPmnOw3MNv4pbNakXxPPtcBAK27",  "sourceCode" : "APPStore",  "deviceManufacturer" : "iPhone",  "appVersion" : "4.5",  "userAccount" : "17621856713",  "signVersion" : "0.2"}',

            }),
            "18390536344": ObjectDict({
                'Host': 'cxj.activity.chexiang.com',
                'Referer': 'https://cxj.activity.chexiang.com/cx/cxj/cxjappweb/welfare/index.shtml',
                'X-Requested-With': 'XMLHttpRequest',
                'Accept-Encoding': 'br, gzip, deflate',
                'Accept-Language': 'zh-CN',
                'Content-Type': 'application/json;charset=UTF-8',
                'cookie': 'user_trace_cookie=CiCcQFounz1uaGOTL8TNAg==; wcid=CAD455B4-3CF6-41C3-A17E-30E080B23E94; scookie0=43b199d2cb0941abb4d726df6d9926cf; scookie1=1513004865842; scookie2=1513004866113; bbbbbbbbbbbbbbb=OFNINEIIMCAPGHMAEOMCNDENEIECHGIGFBNDOFEGIKODMHNLHIEKMAPKAILAEHGOHOEBLFCHMJGJIBEFPJKCOFHGNKGFKCCPDDEPBJFJJBAIHIBNPGMDAIKDCHJEHCBD',
                'User-Agent': '{"appCode":"MongoToC","appVersion":"4.4.1","clientId":"e48b4428c76440eebf02591feb2a999c","deviceId":"359250051938981","deviceManufacturer":"LGE","origin":"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/M4B30Z; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36","plateformType":"android","signVersion":"0.2","signature":"94E24341CF425DE53BF10D26931665D4","sourceCode":"CXB0004","userToken":"MTAwMDVhMmU5Y2RmNWFhNTQzZGYxMTIzOTgzMD-QPWKujOgseclOBRNu8nIIYQqb"}',
            })
        })

        jdata = ObjectDict({
            'currentCity': '上海市',
            'longitude': '121.326199',
            'latitude': '31.134585',
        })

        for key, header in routine_header.items():
            res = yield http_post("https://cxj.activity.chexiang.com/service/dailyfuli/list/0", jdata, headers=header)
            for store in res.obj.dailyFuliVos:
                yield self.get_dailyredpacket(store['prizeCode'])

    @gen.coroutine
    def get_dailyredpacket(self, prize_code):
        """
        每日福利领取
        :param prize_code:
        :return:
        """

        routine_header = ObjectDict({
            "17621856713": ObjectDict({
                'Host': 'cxj.activity.chexiang.com',
                'Referer': 'https://cxj.activity.chexiang.com/cx/cxj/cxjappweb/welfare/index.shtml',
                'X-Requested-With': 'XMLHttpRequest',
                'Accept-Encoding': 'br, gzip, deflate',
                'Accept-Language': 'zh-CN',
                'Content-Type': 'application/json;charset=UTF-8',
                'cookie': 'bbbbbbbbbbbbbbb=CEMAODLNGENADMNJCNMIBNNAEFIPDGBDLADHMOJACFIDADLFFPMFBAILLNMAAKMHHNNFLPEPOEKKKMIKCJGEKLCAEGLHKOGGLEJLLAEHMGMMAJNHKDFIGFIJJJMCCANH; scookie2=1513004402087; scookie0=eb0695d4223845879ecc7197239e73fb; scookie1=1513004392073; user_trace_cookie=CiCcQFounWZuaGOTL7/+Ag==; analysis_sign=10652305; wemall_cxid_c=10652305; wemall_equid_c=723D3C53-952C-4FF2-8C80-EE0D47788F4B; wemall_openid_c=""; wemall_opentype_c=6; wemall_userkey_c=29a04582-23c3-42cd-a92d-0337570a09ed; wcid=8D0A3F22-BCFF-4CA5-8F26-CBCC151A8200',
                'User-Agent': '{  "clientId" : "93c36ab85c994b04b184c3653297eaed",  "deviceId" : "723D3C53-952C-4FF2-8C80-EE0D47788F4B",  "appCode" : "MongoToC",  "plateformType" : "ios",  "signature" : "250C6C58ED3FC8F7550E33A755DABD80",  "origin" : "Mozilla\/5.0 (iPhone; CPU iPhone OS 11_1_2 like Mac OS X) AppleWebKit\/604.3.5 (KHTML, like Gecko) Mobile\/15B202",  "userToken" : "MTAwMDVhMmU5Y2ZiNWFhNTQzZmIxMDY1MjMwNWPmnOw3MNv4pbNakXxPPtcBAK27",  "sourceCode" : "APPStore",  "deviceManufacturer" : "iPhone",  "appVersion" : "4.5",  "userAccount" : "17621856713",  "signVersion" : "0.2"}',
            }),
            "18390536344": ObjectDict({
                'Host': 'cxj.activity.chexiang.com',
                'Referer': 'https://cxj.activity.chexiang.com/cx/cxj/cxjappweb/welfare/index.shtml',
                'X-Requested-With': 'XMLHttpRequest',
                'Accept-Encoding': 'br, gzip, deflate',
                'Accept-Language': 'zh-CN',
                'Content-Type': 'application/json;charset=UTF-8',
                'cookie': 'user_trace_cookie=CiCcQFounz1uaGOTL8TNAg==; wcid=CAD455B4-3CF6-41C3-A17E-30E080B23E94; scookie0=43b199d2cb0941abb4d726df6d9926cf; scookie1=1513004865842; scookie2=1513004866113; bbbbbbbbbbbbbbb=OFNINEIIMCAPGHMAEOMCNDENEIECHGIGFBNDOFEGIKODMHNLHIEKMAPKAILAEHGOHOEBLFCHMJGJIBEFPJKCOFHGNKGFKCCPDDEPBJFJJBAIHIBNPGMDAIKDCHJEHCBD',
                'User-Agent': '{"appCode":"MongoToC","appVersion":"4.4.1","clientId":"e48b4428c76440eebf02591feb2a999c","deviceId":"359250051938981","deviceManufacturer":"LGE","origin":"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/M4B30Z; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36","plateformType":"android","signVersion":"0.2","signature":"94E24341CF425DE53BF10D26931665D4","sourceCode":"CXB0004","userToken":"MTAwMDVhMmU5Y2RmNWFhNTQzZGYxMTIzOTgzMD-QPWKujOgseclOBRNu8nIIYQqb"}',
            })
        })

        for key, header in routine_header.items():
            yield http_get(
                "https://cxj.activity.chexiang.com/service/dailyfuli/receive?prizeCode={}".format(prize_code),
                headers=header)

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

        yield http_get(
            "https://cxj.activity.chexiang.com/service/fuliv2/luck?itemId={0}&storeId={1}".format(item_id, store_id),
            headers=header)

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

        res = yield http_get(
            "https://cxj.activity.chexiang.com/service/fuliv2/getStoreSchemeItem?storeId=&longitude=121.373299&latitude=31.312585&cityName=%E4%B8%8A%E6%B5%B7%E5%B8%82",
            headers=routine_header)
        for item in res.obj.get('items'):
            yield self.get_redpacket(item['sid'], res.obj.store.storeId)

    @gen.coroutine
    def runner(self):
        try:
            self.logger.debug("[chexiangjia]start in:{}".format(curr_now()))
            yield self.get_routine()
            # yield self.get_jufengyuan()
        except Exception as e:
            self.logger.error(traceback.format_exc())
        finally:
            IOLoop.instance().stop()
            self.logger.debug("[chexiangjia]end in:{}".format(curr_now()))


if __name__ == "__main__":
    jp = Chexiangjia()
    jp.runner()
    IOLoop.instance().start()
