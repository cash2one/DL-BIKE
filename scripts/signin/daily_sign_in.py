# coding=utf-8

# @Time    : 2/21/17 14:33
# @Author  : panda (panyuxin@moseeker.com)
# @File    : daily_sign_in.py
# @DES     : 

# Copyright 2016 MoSeeker

import http.client

def qyer_sign_in():

    """穷游客户端签到"""
    conn = http.client.HTTPConnection("open.qyer.com")

    payload = "account_s=fef74474cd9678792d86e83dfafbfb9e&client_id=qyer_ios&client_secret=cd254439208ab658ddf9&count=20&lat=31.19774147548028&lon=121.4274459760588&oauth_token=0b03e0779e7c7daf114945ef1df24ec6&page=1&track_app_channel=AppStore&track_app_version=7.4&track_device_info=iPhone&track_deviceid=39DA2458-316C-70AE-F956-B3C46ED9CCE6&track_os=ios10.2.1&track_user_id=1793208&v=1"

    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'host': "open.qyer.com",
        'accept': "*/*",
        'connection': "keep-alive",
        'cookie': "__utma=253397513.1667471721.1476627137.1486093623.1486177584.17; __utmb=253397513.1.10.1486177584; __utmc=253397513; __utmt=1; __utmz=253397513.1476627137.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _guid=c50082bd-15a4-c693-dc03-24ffffdcfad0; init_refer=; new_session=1; new_uv=17; session_time=1486177583; cdb_auth=2fd7%2BuJDATGAZtUZ0sEocWnV6ZVZ79H5s14PpNFflLUhPiIP%2B6uVCZhQfqg1CEo2fqc3dWPe6fqcql919ot4FPqJEJd3fA; als=0",
        'user-agent': "QYER/7.4 (iPhone; iOS 10.2.1; Scale/2.00)",
        'cache-control': "no-cache",
        'postman-token': "3e10c310-f214-0af9-dea6-d2ed1fcd4c16"
    }

    conn.request("POST", "/qyer/mileage/sign/add_mileage", payload, headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def smzdm_sign_in():

    """什么值得买客户端签到"""
    conn = http.client.HTTPSConnection("api.smzdm.com")

    payload = "f=iphone&sk=uiWkBkg57AMGgHLwyyG2m1qDxYhzQNRLBxZfKVS4%252BIx1%2FMNqprtg4BKecGkdxDTy&token=54537f7044811152704&v=5.0&weixin=1"

    headers = {
        'host': "api.smzdm.com",
        'content-type': "application/x-www-form-urlencoded",
        'cookie': "device_id=0ggWhPmKxHzTDvKF24YJ3y6Py1Qv9dNyjVHDEwazEAUN9a5RZWpvpQ==; device_name=iPhone 6s; device_push=notifications_are_disabled; device_s=4AV2/Xtutz19ebZ6LkBPT5PdjEzAF2arHXBblhuQMRuYGa4RMTPgI1zQhJe81ZkHz8fVBPKucw=; device_smzdm=iphone; device_smzdm_version=7.6; device_system_version=10.2.1; device_type=iPhone8,1; login=1; network=WiFi_Net; partner_id=0; partner_name=AppStore; sess=54537f7044811152704; smzdm_id=6418214012; __ckguid=lpi28Cg154wJ7N4VkL4H6N4; __jsluid=ab4c1ed89fd3fb715b47dd3f4f402848; __ckguid=ecu4hlnBgB7f1VftHOl3Co2; _ga=GA1.2.1848225762.1447993948; Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58=1482416015; smzdm_user_source=AEF63FB28C36CAC0B5F09EC24FEEC252",
        'user-agent': "smzdm_iPhone/7.6 (iPhone; iOS 10.2.1; Scale/2.00)smzdmapp",
        'accept-language': "zh-Hans-CN;q=1, en-CN;q=0.9, zh-Hant-CN;q=0.8",
        'cache-control': "no-cache",
        'postman-token': "a35921dd-e68e-15f2-dcd0-1b8711e1f84b"
    }

    conn.request("POST", "/v1/user/checkin", payload, headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def music_163_sign_in():

    """网易云音乐签到"""
    conn = http.client.HTTPConnection("music.163.com")

    payload = "params=04F1A0AB8150EFD085BC839891D19E2E488A2D6C2924C5589260A62E82B1A0D3BA7AC29333EDAA68300EE4FE29CFD7407CD065FD9D8BA0153B98A3AFE422456DF5B4AF6FEFB7011FC85EA28E8CEDADA4233BB43F0F8B76F24D9AB171B538220CD0398941677B9A89C628F424FB2AA0984E7F0F7D305BC5E35F5CF756D6BBB996B3F64B78E30003F2BD1D9529165DB9B95EE290D58921FD5D7D507433E66DF78F7CDDFC5F2C86D11134D14C4B9B162C8977B4A63B5BB595B0FAB0D94F59DCAF14C9C699D5D439369EAD11BA4BECCD7A3B0403D0DA14A27CC6B3C203788789AF492F3143287CEC1B7337F1EDBB99350C42DAC41BEAA61A53C40E8843ECB98BF6067CD065FD9D8BA0153B98A3AFE422456DF5B4AF6FEFB7011FC85EA28E8CEDADA4BB0B520B36F7B62359FB9EB25282CC53A4C855FE4D769B5AB9C1D5DB9B54C3B2908C2C2A2120DEAD8E028BD6AB85403EA94369B1DA20D473D69042283FAC324869C1115961DA65615815ABFD139405586D5B7732442D99A133AB15391677B6A00898EBF741BDFBE28C530FF426061A398D3DEB528DEA5D61EABCD3CD5F422ECEF2908E4EE1670EFB61C5211C87369F6E636D2FFFAE5D4D6358E104D39B42D6E9D4356D88F4AA9D810259CC200D69CAB6F681FC595E0FB0A228CBDB657F0F5B2B14A4DD97D79CE7E7DC3A3BC17B29C0C6107390459EEF14A4D43B10BB9099BFE8A2C299DEA6763894248443BB2C40B0A9952E6ACF1C2F1F50ED3695822C3532B288240948A06BD80FF90823B9C06AA93E4C888336B2B3BAAF301A662B2BD332B3C1B5F865E0C0F565830D262C482C2C74A1D185CB6DCAF83656F1F43B87D0E72865115AD72EA6A613F467B50ED19A51EA5FA1ED92A570EFEAA6B49207CB2B6D1F"

    headers = {
        'host': "music.163.com",
        'content-type': "application/x-www-form-urlencoded",
        'cookie': "os=iPhone OS; osver=10.2.1; appver=3.7.5; deviceId=d03ab28a26a9b5b35d3dee25c3eb00d2; MUSIC_U=61a5d719c83ecbfc5c7b8435f560458e1592dcc50ab2a078cf3c61ff4a7ec5e0ad2ea5269380b8893eb7658aeefa351d365b7c0d8e97a004c3061cd18d77b7a0",
        'accept-encoding': "gzip",
        'cache-control': "no-cache",
        'postman-token': "fbd3a91c-99bb-575d-af49-462253fd46d7"
    }

    conn.request("POST", "/eapi/point/dailyTask", payload, headers)

    res = conn.getresponse()

if __name__ == '__main__':

    qyer_sign_in()
    smzdm_sign_in()
    music_163_sign_in()