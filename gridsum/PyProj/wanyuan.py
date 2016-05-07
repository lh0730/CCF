# -*- coding: utf8 -*-
__author__ = 'Dang'

import re
import sys

reload(sys)
sys.setdefaultencoding("utf8")

def wanyuan(Strl):   
     while  1:
         Num=re.search(u'[\d+\.]+万',Strl)
         if Num: 
             Num0=Num.group(0)
             Num1=(int)((float)(Num0[:-1])*10000)
             Num2=str(Num1)
             Strl=Strl.replace(Num0,Num2,1)
         else:
             break
     return Strl
