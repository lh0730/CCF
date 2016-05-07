# -*- coding: utf8 -*-
__author__ = 'Tan'

import sys
import re

reload(sys)
sys.setdefaultencoding("utf8")

def nianyueri(str):
    while 1:
        mm = re.search(u"\d+[年|月|日]", str)
        if mm:
            mm = mm.group()
            str = str.replace(mm, "")
            # print str
        else:
            break
    return str

