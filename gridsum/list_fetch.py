import sys
from imp import reload
reload(sys)
sys.setdefaultencoding('utf-8')


f=open('custom.dict','rb')
dict=[]
for line in f:
    dict.append(line.decode('utf-8').strip('\n'))
f.close()
f=open('data1.txt','rb')
word=[]
id=[]
for line in f:
    content=line.decode('utf-8').split('\t')
    word.append(content[1].strip('\n'))
    id.append(content[0])
match=[]
for item in word:
    content=item.split()
    test=[]
    for item1 in content:
        if item1 in dict:    
            test.append(item1)
    match.append(test)
f.close()
f=open('cash1.csv','w')
i=0
for item in match:
    for item1 in item:
        f.write(id[i])
        f.write(',')
        f.write(item1)
        f.write('\n')
    i=i+1
f.close()

