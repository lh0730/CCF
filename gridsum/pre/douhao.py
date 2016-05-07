# -*- coding: utf8 -*-
import imp
import re 
import sys


imp.reload(sys)
sys.setdefaultencoding("utf8")

def douhao(sen):
    sen = sen.replace("，", ",")
    while 1:
        mm = re.search("\d,\d", sen)
        if mm:
            mm = mm.group()
            sen = sen.replace(mm, mm.replace(",", ""))
            # print sen
        else:
            break

    return sen
