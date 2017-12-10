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
        'user-agent': '{"appCode":"MongoToC","appVersion":"4.4.1","clientId":"e48b4428c76440eebf02591feb2a999c","deviceId":"359250051938981","deviceManufacturer":"LGE","origin":"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/M4B30Z; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36","plateformType":"android","signVersion":"0.2","signature":"030894A336A292BB49FA54D2B3A3DF31","sourceCode":"CXB0004","userToken":"MTAwMDVhMmNkMGI0NWFhMzc3YjQxMDY1MjMwNftC_PseiUhdusE2dJ3uQPGthnNH"}',
        'referer': "https://h.jia.chexiang.com/cx/cxj/cxjweb/checkins/checkins.shtml?userInfo=JTdCJTIyc291cmNlVHlwZSUyMiUzQSUyMjIlMjIlMkMlMjJsb2NhbFglMjIlM0ElMjIxMjEuMzc3NDAxJTIyJTJDJTIybG9jYWxZJTIyJTNBJTIyMzEuMzI0Mzk4JTIyJTJDJTIybW9iaWxlUGhvbmUlMjIlM0ElMjIxNzYyMTg1NjcxMyUyMiUyQyUyMmNpdHlOYW1lJTIyJTNBJTIyJUU0JUI4JThBJUU2JUI1JUI3JUU1JUI4JTgyJTIyJTJDJTIydXNlcklkJTIyJTNBJTIyS0h5OTJnJTJGV2UxTXRYbTRBUWVmRld3JTNEJTNEJTIyJTJDJTIyZXF1SWQlMjIlM0ElMjI3MjNEM0M1My05NTJDLTRGRjItOEM4MC1FRTBENDc3ODhGNEIlMjIlMkMlMjJjdXN0TmFtZSUyMiUzQSUyMiUyMiU3RA==",
        'cookie': 'user_trace_cookie=CiCcVFos0LdUV3kYMCdiAg==; wcid=F2C07C01-382E-414D-A43B-8176BAED2D69; sc_s=MTAwMDVhMmNkMGI0NWFhMzc3YjQxMDY1MjMwNftC_PseiUhdusE2dJ3uQPGthnNH; analysis_sign=10652305; wemall_cxid_c=10652305; _ga=GA1.2.304772011.1512886460; _gid=GA1.2.169479479.1512886460; scookie0=4b7f858aae794f298479d14d790ca7b0; scookie1=1512886477279; bbbbbbbbbbbbbbb=PBGIELEBGMLAFMKICAKOJPDJPFIBHLLHNELFIAGCMEIDNMCLNMBHNCJIIFDAKMFLCAGHAMIJNIHOICLDINEOJJDPPJGKIAHAJFBIGLAMNBOHHFKEBJLHMOMFMAFOCFJA; wemall_opentype_c=6; wemall_openid_c=""; wemall_equid_c=359250051938981; wemall_userkey_c=cb32b937-e2fe-4b43-a5d0-5bb3f1508b23; scookie2=1512886489433',
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
        'user-agent': "{  \"clientId\" : \"93c36ab82c994104b184c3653297eaed\",  \"deviceId\" : \"723D1C53-952C-4FF2-8C20-E25D4778894B\",  \"appCode\" : \"MongoToC\",  \"plateformType\" : \"ios\",  \"signature\" : \"2009CFFC21D78FE8B8C0A0B1E5741ACF\",  \"origin\" : \"Mozilla\/5.0 (iPhone; CPU iPhone OS 11_0_3 like Mac OS X) AppleWebKit\/604.1.38 (KHTML, like Gecko) Mobile\/15A432\",  \"userToken\" : \"MTAwMDU5ZWNhNzg4NWE2MzRlODgxMDY1MjMwNSLkvLka68lia3_un5ki1aVctZjN\",  \"sourceCode\" : \"APPStore\",  \"deviceManufacturer\" : \"iPhone\",  \"appVersion\" : \"4.3.1\",  \"userAccount\" : \"18390536344\",  \"signVersion\" : \"0.2\"}",
        'referer': "https://h.jia.chexiang.com/cx/cxj/cxjweb/checkins/checkins.shtml?userInfo=JTdCJTIyc291cmNlVHlwZSUyMiUzQSUyMjIlMjIlMkMlMjJsb2NhbFglMjIlM0ElMjIxMjEuMzc3NDAxJTIyJTJDJTIybG9jYWxZJTIyJTNBJTIyMzEuMzI0Mzk4JTIyJTJDJTIybW9iaWxlUGhvbmUlMjIlM0ElMjIxNzYyMTg1NjcxMyUyMiUyQyUyMmNpdHlOYW1lJTIyJTNBJTIyJUU0JUI4JThBJUU2JUI1JUI3JUU1JUI4JTgyJTIyJTJDJTIydXNlcklkJTIyJTNBJTIyS0h5OTJnJTJGV2UxTXRYbTRBUWVmRld3JTNEJTNEJTIyJTJDJTIyZXF1SWQlMjIlM0ElMjI3MjNEM0M1My05NTJDLTRGRjItOEM4MC1FRTBENDc3ODhGNEIlMjIlMkMlMjJjdXN0TmFtZSUyMiUzQSUyMiUyMiU3RA==",
        'cookie': "bbbbbbbbbbbbbbb=CGPLHIOKOBPLKEPHAMMOOCPBOPBOGMIAGOOHGENJBOGDPBDCEIAMKKKPNLBACGEDFLOCHMMLKBLGJHNNJHOJJEJJCMDGBLGPBJKEFCCOOOANHKOGBDBNPIEALIFCBIJO; user_trace_cookie=CiCcEForedobkWTAUY2RAg==; wcid=A7897D88-49F9-4812-96E7-B761ED6229C8; OUTFOX_SEARCH_USER_ID_NCOO=1741702166.7859335; erroMsg=0; captchaType=action; high=9; picWidth=305; picHigh=100; originalWidth=300; originalHigh=100; originalMaskWidth=70; originalMaskHigh=70; captchaKey=da5fe4e8f3e548b08767196c4e9363a1; CASTGC-MAIN=\"TGT-182178-AuOHeWDvZbX4kmUMUtMGb9E55u2Xcl9vVdFakapdhjK7aprssz-https://sso.chexiang.com\"; sc_s=MDEyMzVhMmI3YmEyNWE1MzA4YTIxMTIzOTgzMCci-fjDk_7p40tMCaYXwQCUz2kE; analysis_sign=11239830; Hm_lvt_f8ba65b380f665911ecab4df90bfe056=1512798684,1512798951; Hm_lpvt_f8ba65b380f665911ecab4df90bfe056=1512799184; scookie0=19f4c1e5c2084e4e8244f76c1a344d4d; scookie1=1512799198321; wemall_opentype_c=10; wemall_userkey_c=5908bcfb-4df5-4f54-8102-07f2389fd2d3; wemall_cxid_c=11239830; _ga=GA1.2.2134700616.1512798684; _gid=GA1.2.1315227946.1512798684; Hm_lvt_28c4ea50b587487c8791d9a58f45af78=1512798684,1512798951; Hm_lpvt_28c4ea50b587487c8791d9a58f45af78=1512799264; cityId=310100; city.id=310100; city.name=%E4%B8%8A%E6%B5%B7; city_id=310100; city_name=%E4%B8%8A%E6%B5%B7; area.code=244000; city.domain=.chexiang.com; scookie2=1512799445577",
    }

    conn.request("POST", "/water/addWater.htm", payload, headers)

    res = conn.getresponse()
    data = res.read()
    print("[chexiang][18390536344][time:{}][res:{}]".format(curr_now(), data.decode("utf-8")))


if __name__ == '__main__':
    chexiang_sign_in_17621856713()
    chexiang_sign_in_18390536344()