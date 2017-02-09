# coding=utf-8

# @Time    : 9/9/16 22:36
# @Author  : Panda (panyuxin@moseeker.com）
# @File    : alarm.py

# Copyright 2016 MoSeeker

import json
from util.tool.http_tool import http_post
from setting import settings

# Moseeker Slack team webhook settings url:
# https://moseekermm.slack.com/services/B0TUGEK60#service_setup
SLACKMAN_WEBHOOK_URL="https://hooks.slack.com/services/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"


class Alarm(object):
    def __init__(self, webhook_url):
        self._webhook_url = webhook_url

    def biu(self, text, **kwargs):
        """
        slackman 报警
        :param text:
        :param kwargs:
        :return:
        """
        # debug 环境不报警
        assert text
        if not settings['debug']:
            payload = json.dumps({
                'text': text,
                'username': kwargs.get('botname'),
                'channel': kwargs.get('channel'),
                'icon_emoji': kwargs.get('emoji')
            })

            http_post(route=self._webhook_url, jdata=payload)

        return

Alarm = Alarm(SLACKMAN_WEBHOOK_URL)

if __name__ == '__main__':
    Alarm.biu('biu',
                 botname="公共自行车查询",
                 channel="#dl-bike")