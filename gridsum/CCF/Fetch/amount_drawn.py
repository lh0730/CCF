# -*- coding: utf8 -*-
import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')


def amount_drawn(readfile, writefile):
    f = open('custom.dict', 'rb')
    dict = []
    for line in f:
        dict.append(line.strip())
    f.close()

    fp = open(readfile, 'rb')
    test0 = []
    test1 = []
    test2 = []
    for line in fp:
        content = line.split('\t')
        items = re.findall(r'[\d+\.\d+|\d+]{2,}', content[1])
        content1 = content[1].split()
        for item in items:
            if item in content1:
                a = content1.index(item)
                for x in range(0, 5):
                    if a - x >= 0:
                        if content1[a - x] in dict:
                            test0.append(content[0])
                            test1.append(content1[a - x])
                            test2.append(item)
                            break
    fp.close()

    f = open(writefile, 'wb')
    f.write('documentid' + ',' + 'property' + ',' + 'value' + '\n')
    for x in range(0, len(test0)):
        f.write(test0[x] + ',' + test1[x] + ',' + test2[x] + '\n')
    f.close()

    return 0
