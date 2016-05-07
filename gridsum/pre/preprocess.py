# -*- coding: utf8 -*-
import imp
import sys
import re
from douhao import douhao
from chinese_digit import getResultForDigit

imp.reload(sys)
sys.setdefaultencoding("utf8")

def pre(test_str):
    test_str = douhao(test_str)
    while 1:
        result = re.search(u'[〇零一二三四五六七八九十百千万壹贰叁肆伍陆柒捌玖拾佰仟萬亿元角分]{3,}', test_str)
        if result:
            result = result.group()
           # print(result)
           # print(getResultForDigit(result))
            test_str = test_str.replace(result, str(getResultForDigit(result)),1)
        else:
            break
    return test_str
