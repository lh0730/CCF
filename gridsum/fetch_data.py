import csv
import jieba
import sys
import imp

imp.reload(sys)
sys.setdefaultencoding('utf-8')

f=open('custom.dict','r')
for line in f:
    jieba.add_word(line.strip())
f.close()
'''f=csv.reader(open('newdata.csv','r'))
fp=open('test.txt','w')
for line in f:
    content=line[1].split('\n')
    fp.write(line[0]+'\t')
    for item in content:
        fp.write(item)
    fp.write('\n')
fp.close()'''
fp=open('final_data.txt','r')
ID=[]
words=[]
for line in fp:
    test=[]
    content=line.split('\t')   
    ID.append(content[0])
    final=jieba.cut(content[1])
    a=' '.join(final)
    test.append(a.strip('\n'))
    words.append(test)
#del words[0]
#del ID[0]
fpp=open('data1.txt','wb')
i=0
for item in words:
    fpp.write(ID[i]+'\t')
    for itemo in item:
        fpp.write(itemo)
    fpp.write('\n')
    i=i+1
fp.close()
fpp.close()
