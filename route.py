# coding=utf-8

'''
说明:
api接口的route都加上api，非api的route会被统计为PV、UV
'''

routes = [

    # weapp
    # (r"/weapp",                                  "handler.weapp.weapp.WechatHandler")

    # hztrip
    (r"/hztrip",                 "handler.wehztrip.event.WechatOauthHandler",  {"event": "wechat_hztrip"}),
    (r"/xhjd",                   "handler.xhjd.event.WechatOauthHandler",      {"event": "wechat_xhjd"})
]
