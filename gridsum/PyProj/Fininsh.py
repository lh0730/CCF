# -*- coding: utf8 -*-
__author__ = 'Administrator'
import csv
import sys
import re
import jieba
reload(sys)
sys.setdefaultencoding("utf8")

reload(sys)
sys.setdefaultencoding("utf8")

def LoadData(filename):
	fr=open(filename)
	Dataline=csv.reader(fr)
	Data=[];label=[]
	for line in Dataline:
		label.append(line[0])
		Data.append(line[1])
	return  Data,label

# data,lable=LoadData('test.csv')

def  PRO(StrL):  #函数将判决如下之前去除，把括号以及括号内的内容去除
	lenl=StrL.find(u'判决如下')+5
	ll=StrL[lenl:]
	DBracket=re.sub(r"(\（.*\）)", '',ll)  #去除括号
	if u'万'  in DBracket:
		DBracket=DBracket.replace(u'万','0000')  #将万改成0000
	DBracket=re.sub(u'第(\d+)','',DBracket)  #删除第。。。。
	return DBracket

def Rewan(StrL): #函数将字符串中的万元修改为数字，如23.5万元改为235000
	mm=re.compile(r'\d+.(\d+)')
	ll=mm.match(StrL)
	if ll.group(1) and len(ll.group(1))>4:
		numI=float(StrL)*10000
		StrL=str(numI)
	return StrL








