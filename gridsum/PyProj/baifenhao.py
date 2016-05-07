# -*- coding: utf8 -*-
__author__ = 'Tan'

import sys
import re

reload(sys)
sys.setdefaultencoding("utf8")

def baifenhao(str):
    while 1:
        mm = re.search("[\d\.]+%", str)
        if mm:
            mm = mm.group()
            str = str.replace(mm, "")
            # print str
        else:
            break
    return str