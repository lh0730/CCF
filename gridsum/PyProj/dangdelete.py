# -*- coding: utf8 -*-
__author__ = 'Dang'

import re
import sys

reload(sys)
sys.setdefaultencoding("utf8")


def dangdelete(StrL):  # 函数将判决如下之前去除，把括号以及括号内的内容去除
    if StrL.find(u'判决如下')>0:
        lenl = StrL.find(u'判决如下') + 6
        StrL = StrL[lenl:]
    DBracket = re.sub(u"(\（.*\）)", '', StrL)  # 去除括号
    DBracket = re.sub(u'第(\d+)', '', DBracket)  # 删除第。。。。
    DBracket=re.sub(u'[计|即](\d+.\d+)','',DBracket)
    DBracket=re.sub(u'人民币','',DBracket)
    DBracket=re.sub(u'[\d\.]+计息','',DBracket)

    return DBracket