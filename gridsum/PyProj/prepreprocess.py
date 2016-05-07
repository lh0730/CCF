# -*- coding: utf8 -*-
__author__ = 'Tan'

import sys
from hanzi import hanzi
from douhao import douhao
from baifenhao import baifenhao
from nianyueri import nianyueri
from dangdelete import dangdelete
from wanyuan import wanyuan


reload(sys)
sys.setdefaultencoding("utf8")

def pre(test_str):
    test_str = hanzi(test_str)
    test_str = douhao(test_str)
    test_str = baifenhao(test_str)
    test_str = nianyueri(test_str)
    test_str = dangdelete(test_str)
    test_str = wanyuan(test_str)
    return test_str
