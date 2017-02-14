# coding: utf-8

'''
时间工具类
'''

from datetime import datetime

import conf.common as const


def curr_datetime_now():
    return datetime.now()


def curr_now():
    return datetime.now().strftime(const.TIME_FORMAT)


def curr_now_pure():
    return datetime.now().strftime(const.TIME_FORMAT_PURE)


def curr_now_dateonly():
    return datetime.now().strftime(const.TIME_FORMAT_DATEONLY)


def curr_now_minute():
    return datetime.now().strftime(const.TIME_FORMAT_MINUTE)


def curr_now_msec():
    return datetime.now().strftime(const.TIME_FORMAT_MSEC)


def format_dateonly(time):
    return time.strftime(const.TIME_FORMAT_DATEONLY)


def is_time_valid(str_time, form):
    """
    判断时间格式是否符合要求
    """
    ret = False
    try:
        if datetime.strptime(str_time, form):
            ret = True
    except ValueError:
        pass
    finally:
        return ret
