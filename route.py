# coding=utf-8

'''
说明:
api接口的route都加上api，非api的route会被统计为PV、UV
'''

routes = [

    # weapp
    # (r"/weapp",                                  "handler.weapp.weapp.WechatHandler")

    # hztrip
    (r"/hztrip",                        "handler.wehztrip.event.WechatOauthHandler",  {"event": "wechat_hztrip"}),

    # # job
    # (r"/job/api/positionfav",                   "handler.job.position_fav.PositionFavHandler"),
    # (r"/job/search",                            "handler.job.position_list.PositionListHandler"),
    # (r"/job/?(.*)",                             "handler.job.position.PositionHandler"),
    #
    # # 公共方法
    # (r"/common/?(.*)",                          "handler.common.common.CommonHandler"),
    #
    # # sitemap
    # (r"/sitemap.xml",                           "handler.common.sitemap.SitemapHandler"),
    # (r"/sitemap_all.xml",                       "handler.common.sitemap.SitemapAllHandler"),
    #
    # # 官网
    # (r"/official/aboutus",                      "handler.official.index.AboutUsHandler"),
    # (r"/?(.*)",                                 "handler.official.index.IndexHandler")
]
