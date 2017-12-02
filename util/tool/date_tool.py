# coding: utf-8

'''
时间工具类
'''

import time
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

def curr_now_minuteonly():
    return datetime.now().strftime(const.TIME_MINUTE_ONLY)


def curr_now_minute():
    return datetime.now().strftime(const.TIME_FORMAT_MINUTE)


def curr_now_msec():
    return datetime.now().strftime(const.TIME_FORMAT_MSEC)


def format_dateonly(time):
    return time.strftime(const.TIME_FORMAT_DATEONLY)

def is_today(timestamp):
    timestamp = time.localtime(timestamp)
    dt = time.strftime(const.TIME_FORMAT_DATEONLY, timestamp)
    cur_dateonly = curr_now_dateonly()
    if (dt == cur_dateonly):
        return True
    return False

def format_hour_minute(timestamp):
    timestamp = time.localtime(timestamp)
    dt = time.strftime(const.TIME_MINUTE_ONLY, timestamp)
    return dt


def weekend():
    weekend = datetime.now().weekday()
    if weekend in [6,7]:
        return True
    return False


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

def str_2_date(str_time, format):
    """
    将字符串时间格式转化为 datetime
    :param str_time:
    :param form:
    :return:
    """
    res_date_time = str_time
    try:
        res_date_time = datetime.strptime(str(str_time), format)
    except ValueError:
        res_date_time = datetime.strptime(str(str_time), const.TIME_FORMAT)
        res_date_time = res_date_time.strftime(format)
    finally:
        return res_date_time

def sec_2_time(seconds):
    """
    将秒数转换为时分秒
    :param seconds:
    :return:
    """
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)

    return "%02d时%02d分%02d秒" % (h, m, s)

if __name__ == '__main__':
    print (weekend())
