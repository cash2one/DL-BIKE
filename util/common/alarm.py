# coding=utf-8

# @Time    : 9/9/16 22:36
# @Author  : Panda (panyuxin@moseeker.com）
# @File    : alarm.py

import json
import requests
import socket

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
        text = "[{0}]: {1}".format(socket.gethostname(), text)
        payload = json.dumps({
            'text': text,
            'username': kwargs.get('botname') or "公共自行车查询",
            'channel': kwargs.get('channel') or "#dl-bike",
            'icon_emoji': kwargs.get('emoji')
        })

        requests.post(self._webhook_url, data=payload)

Alarm = Alarm(SLACKMAN_WEBHOOK_URL)

if __name__ == '__main__':
    Alarm.biu('biu')