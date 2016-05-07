#coding:utf-8
import sys
import imp
import csv
import prepreprocess
import chardet
imp.reload(sys)
sys.setdefaultencoding('utf-8')



f=csv.reader(open('newdata.csv','rb'))
fp=open('final_data.txt','wb')
for line in f:
    content=line[1].decode('utf-8').split('\n')
    fp.write(line[0]+'\t')
    for sen in content:
        content1=prepreprocess.pre(sen)
        fp.write(content1)
    fp.write('\n')
#    x=chardet.detect(content1)
fp.close()
