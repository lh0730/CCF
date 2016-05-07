# -*- coding: utf8 -*-

import jieba
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def fetch_data(readfile, writefile):
    f = open('custom.dict', 'r')
    for line in f:
        jieba.add_word(line.strip())
    f.close()

    fp = open(readfile, 'r')
    ID = []
    words = []
    for line in fp:
        test = []
        content = line.split('\t')
        ID.append(content[0])
        final = jieba.cut(content[1])
        a = ' '.join(final)
        test.append(a.strip())
        words.append(test)


    fpp = open(writefile, 'wb')
    i = 0
    for item in words:
        fpp.write(ID[i] + '\t')
        for itemo in item:
            fpp.write(itemo)
        fpp.write('\n')
        i = i + 1
    fp.close()
    fpp.close()

    return
