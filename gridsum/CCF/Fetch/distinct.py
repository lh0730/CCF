# -*- coding: utf8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def distinct(readfile, writefile):
    pan = []
    f = open(readfile, 'rb')
    for line in f:
        pan.append(line.strip())
    tmp = pan[0]
    pan = pan[1:]
    length = len(pan)
    list.sort(pan)
    fuck = []
    define = pan[0]
    fuck.append(define)
    for i in range(1, length):
        if define == pan[i]:
            continue
        else:
            define = pan[i]
            fuck.append(pan[i])
    f.close()

    f = open(writefile, 'wb')
    f.write(tmp+'\n')
    length = len(fuck)
    for i in range(0, length):
        f.write(str(fuck[i]) + "\n")
    f.close()

    return 0
