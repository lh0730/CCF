# -*- coding: utf8 -*-
import sys
import csv
from PreProcess.pre import pre

reload(sys)
sys.setdefaultencoding('utf-8')


def fetch_pre(readfile,writefile):
    f = csv.reader(open(readfile, 'rb'))
    fp = open(writefile, 'wb')
    for line in f:
        content = line[1].decode('utf-8').split('\n')
        for sen in content:
            fp.write(line[0] + '\t')
            content1 = pre(sen)
            fp.write(content1)
            fp.write('\n')
    fp.close()
    return
