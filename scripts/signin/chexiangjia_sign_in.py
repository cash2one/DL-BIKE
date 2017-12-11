# coding=utf-8

# @Time    : 2/21/17 14:33
# @Author  : panda (panyuxin@moseeker.com)
# @File    : daily_sign_in.py
# @DES     : 

import http.client
from util.tool.date_tool import curr_now

def chexiang_sign_in_17621856713():
    """17621856713 车享家ios客户端灌水签到"""

    conn = http.client.HTTPSConnection("h.jia.chexiang.com")
    payload = "--compressed"
    headers = {
        'host': "h.jia.chexiang.com",
        'accept': "application/json, text/plain, */*",
        'x-requested-with': "XMLHttpRequest",
        'accept-language': "zh-cn",
        'content-type': "application/json;charset=utf-8",
        'origin': "https://h.jia.chexiang.com",
        'user-agent': '{  "clientId" : "93c36ab85c994b04b184c3653297eaed",  "deviceId" : "723D3C53-952C-4FF2-8C80-EE0D47788F4B",  "appCode" : "MongoToC",  "plateformType" : "ios",  "signature" : "250C6C58ED3FC8F7550E33A755DABD80",  "origin" : "Mozilla\/5.0 (iPhone; CPU iPhone OS 11_1_2 like Mac OS X) AppleWebKit\/604.3.5 (KHTML, like Gecko) Mobile\/15B202",  "userToken" : "MTAwMDVhMmU5Y2ZiNWFhNTQzZmIxMDY1MjMwNWPmnOw3MNv4pbNakXxPPtcBAK27",  "sourceCode" : "APPStore",  "deviceManufacturer" : "iPhone",  "appVersion" : "4.5",  "userAccount" : "17621856713",  "signVersion" : "0.2"}',
        'referer': "https://h.jia.chexiang.com/cx/cxj/cxjweb/checkins/checkins.shtml?userInfo=JTdCJTIyc291cmNlVHlwZSUyMiUzQSUyMjIlMjIlMkMlMjJsb2NhbFglMjIlM0ElMjIxMjEuMzc3NDAxJTIyJTJDJTIybG9jYWxZJTIyJTNBJTIyMzEuMzI0Mzk4JTIyJTJDJTIybW9iaWxlUGhvbmUlMjIlM0ElMjIxNzYyMTg1NjcxMyUyMiUyQyUyMmNpdHlOYW1lJTIyJTNBJTIyJUU0JUI4JThBJUU2JUI1JUI3JUU1JUI4JTgyJTIyJTJDJTIydXNlcklkJTIyJTNBJTIyS0h5OTJnJTJGV2UxTXRYbTRBUWVmRld3JTNEJTNEJTIyJTJDJTIyZXF1SWQlMjIlM0ElMjI3MjNEM0M1My05NTJDLTRGRjItOEM4MC1FRTBENDc3ODhGNEIlMjIlMkMlMjJjdXN0TmFtZSUyMiUzQSUyMiUyMiU3RA==",
        'cookie': 'bbbbbbbbbbbbbbb=CEMAODLNGENADMNJCNMIBNNAEFIPDGBDLADHMOJACFIDADLFFPMFBAILLNMAAKMHHNNFLPEPOEKKKMIKCJGEKLCAEGLHKOGGLEJLLAEHMGMMAJNHKDFIGFIJJJMCCANH; scookie2=1513004402087; scookie0=eb0695d4223845879ecc7197239e73fb; scookie1=1513004392073; user_trace_cookie=CiCcQFounWZuaGOTL7/+Ag==; analysis_sign=10652305; wemall_cxid_c=10652305; wemall_equid_c=723D3C53-952C-4FF2-8C80-EE0D47788F4B; wemall_openid_c=""; wemall_opentype_c=6; wemall_userkey_c=29a04582-23c3-42cd-a92d-0337570a09ed; wcid=8D0A3F22-BCFF-4CA5-8F26-CBCC151A8200',
    }
    conn.request("POST", "/water/addWater.htm", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print("[chexiang][17621856713][time:{}][res:{}]".format(curr_now(), data.decode("utf-8")))


def chexiang_sign_in_18390536344():
    """18390536344 车享家ios客户端灌水签到"""
    conn = http.client.HTTPSConnection("h.jia.chexiang.com")
    payload = "--compressed"
    headers = {
        'host': "h.jia.chexiang.com",
        'accept': "application/json, text/plain, */*",
        'x-requested-with': "XMLHttpRequest",
        'accept-language': "zh-cn",
        'content-type': "application/json;charset=utf-8",
        'origin': "https://h.jia.chexiang.com",
        'user-agent': '{"appCode":"MongoToC","appVersion":"4.4.1","clientId":"e48b4428c76440eebf02591feb2a999c","deviceId":"359250051938981","deviceManufacturer":"LGE","origin":"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/M4B30Z; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36","plateformType":"android","signVersion":"0.2","signature":"94E24341CF425DE53BF10D26931665D4","sourceCode":"CXB0004","userToken":"MTAwMDVhMmU5Y2RmNWFhNTQzZGYxMTIzOTgzMD-QPWKujOgseclOBRNu8nIIYQqb"}',
        'referer': "https://h.jia.chexiang.com/cx/cxj/cxjweb/checkins/checkins.shtml?userInfo=JTdCJTIyc291cmNlVHlwZSUyMiUzQSUyMjIlMjIlMkMlMjJsb2NhbFglMjIlM0ElMjIxMjEuMzc3NDAxJTIyJTJDJTIybG9jYWxZJTIyJTNBJTIyMzEuMzI0Mzk4JTIyJTJDJTIybW9iaWxlUGhvbmUlMjIlM0ElMjIxNzYyMTg1NjcxMyUyMiUyQyUyMmNpdHlOYW1lJTIyJTNBJTIyJUU0JUI4JThBJUU2JUI1JUI3JUU1JUI4JTgyJTIyJTJDJTIydXNlcklkJTIyJTNBJTIyS0h5OTJnJTJGV2UxTXRYbTRBUWVmRld3JTNEJTNEJTIyJTJDJTIyZXF1SWQlMjIlM0ElMjI3MjNEM0M1My05NTJDLTRGRjItOEM4MC1FRTBENDc3ODhGNEIlMjIlMkMlMjJjdXN0TmFtZSUyMiUzQSUyMiUyMiU3RA==",
        'cookie': 'bbbbbbbbbbbbbbb=JNEFONBAKCDGKDAHKNMDDJFOCLIHELLDDHDECKCBOMADPMCBPFPPGCDHLJBAKGIJGOALOPJOBFHLAGCDPJGGOMODFPGONJCABOPCBPEDOAECNFGBECBHKCDFHFCKJPNK; user_trace_cookie=CiCcQFounz1uaGOTL8TNAg==; wcid=CAD455B4-3CF6-41C3-A17E-30E080B23E94; scookie0=43b199d2cb0941abb4d726df6d9926cf; scookie1=1513004865842; bbbbbbbbbbbbbbb=OFNINEIIMCAPGHMAEOMCNDENEIECHGIGFBNDOFEGIKODMHNLHIEKMAPKAILAEHGOHOEBLFCHMJGJIBEFPJKCOFHGNKGFKCCPDDEPBJFJJBAIHIBNPGMDAIKDCHJEHCBD; scookie2=1513005071034',
    }

    conn.request("POST", "/water/addWater.htm", payload, headers)

    res = conn.getresponse()
    data = res.read()
    print("[chexiang][18390536344][time:{}][res:{}]".format(curr_now(), data.decode("utf-8")))


if __name__ == '__main__':
    chexiang_sign_in_17621856713()
    chexiang_sign_in_18390536344()
