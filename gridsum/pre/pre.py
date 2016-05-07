import preprocess
f=open('data.txt','rb')
fp=open('newdata.txt','w')
for line in f:
    content=line.decode('utf-8').split('\t')
    content1=content[1].split()
    fp.write(content[0]+'\t')
    for item in content1:
        fp.write(item.strip('\n'))
    fp.write('\n')
f.close()
fp.close()
f=open('newdata.txt','rb')
fp=open('pre_data.txt','w')
for line in f:
    content=line.decode('utf-8').split('\t')
    content1=preprocess.pre(content[1].strip().strip('\n'))
    fp.write(content[0]+'\t'+content1+'\n')
f.close()
fp.close()
    
