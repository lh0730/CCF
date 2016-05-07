# -*- coding: utf8 -*-

import re
import sys
from pretranslate import hanzi,wanyuan,douhao

reload(sys)
sys.setdefaultencoding("utf8")


def pre(test_str):
    # 汉字转数字
    test_str = hanzi(test_str)
    # 万元变数字
    test_str = wanyuan(test_str)
    # 'l' 转 '1'
    test_str = test_str.replace('l','1')
    # 删去数字间逗号
    test_str = douhao(test_str)
    # 删除 '判决如下'
    test_str = panjue(test_str)
    # 删除 括号中内容
    # test_str = re.sub(u"(\（.*\）)", '', test_str)
    # 删除 第xx号、章
    test_str = re.sub(u'第(\d+)', '', test_str)
    # 删除 人民币、元、本金、代理
    test_str = re.sub(u'人民币|元|本金|代理', '', test_str)
    # 删除 计\即
    # test_str = re.sub(u'[计|即][\d\.]+', '', test_str)
    # 删除 中的
    test_str = re.sub(u'中的[\d\.]+', '', test_str)
    # 删除 xx计息
    test_str = re.sub(u'[\d\.]+计息', '', test_str)
    # 删除 xx%
    test_str = re.sub(u'[\d\.]+[%|％]', '', test_str)
    # 删除 年月日
    test_str = re.sub(u'\d+[年|月|日]', '', test_str)
    # 删除 已付利息
    test_str = re.sub(u'已付利息[\d\.]+', '', test_str)
    return test_str


# 出现'判决如下'，删除这句话
def panjue(test_str):
    if test_str.find(u'判决如下') > 0:
        length = test_str.find(u'判决如下') + 5
        return test_str[length:]
    return test_str