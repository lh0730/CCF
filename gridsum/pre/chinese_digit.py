# -*- coding: utf8 -*-
import sys

reload(sys)
sys.setdefaultencoding("utf8")

dict = {u'零': 0, u'一': 1, u'二': 2, u'三': 3, u'四': 4, u'五': 5, u'六': 6, u'七': 7, u'八': 8, u'九': 9, u'十': 10, u'百': 100, u'千': 1000, u'万': 10000,
        u'０': 0, u'１': 1, u'２': 2, u'３': 3, u'４': 4, u'５': 5, u'６': 6, u'７': 7, u'８': 8, u'９': 9,
        u'壹': 1, u'贰': 2, u'叁': 3, u'肆': 4, u'伍': 5, u'陆': 6, u'柒': 7, u'捌': 8, u'玖': 9, u'拾': 10, u'佰': 100, u'仟': 1000, u'萬': 10000,
        u'角': 0.1, u'分': 0.01,u'元':None}

def getResultForDigit(a, encoding="utf-8"):
    if isinstance(a, str): 
        a = a.decode(encoding)

    count = 0
    result = 0
    tmp = 0
    flag = False
    while count < len(a):
        tmpChr = a[count]
        # print tmpChr
        if tmpChr == u'元':
            flag = True
        tmpNum = dict.get(tmpChr, None)
        # 如果等于1万
        if tmpNum == 10000:
            result += tmp
            result = result * tmpNum
            tmp = 0
        # 如果等于十或者百，千
        elif tmpNum >= 10:
            if tmp == 0:
                tmp = 1
            result += tmpNum * tmp
            tmp = 0
        # 如果等于分、角
        elif tmpNum < 1 and tmpNum>0:
            if tmp == 0:
                tmp = 1
            if tmpNum == 0.01 and tmp>10:
                tmp2= tmp
                tmp = tmp2/10*100+tmp2%10
            result = result + tmpNum * tmp
            tmp = 0
        # 如果是个位数
        elif tmpNum is not None:
            tmp = tmp * 10 + tmpNum
        count += 1
    result = result + tmp
    if flag == False:
        return result
    else:
        if result==0:
            return u'元'
        return str(result)+u'元'
