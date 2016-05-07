# -*- coding: utf8 -*-

import sys
from Fetch.fetch_pre import fetch_pre
from Fetch.fetch_data import fetch_data
from Fetch.amount_drawn import amount_drawn
from Fetch.distinct import distinct

reload(sys)
sys.setdefaultencoding("utf8")

test_data = r'D:\Documents\CCF_panjuewenshu\testdata\sampledata.csv'
data = r'D:\Documents\CCF_panjuewenshu\data\newdata.csv'

filename = data

file_afterpre = filename[:-4] + '_afterpre.txt'
file_afterfetch = filename[:-4] + '_afterfetch.txt'
consequence_file = filename[:-4] + '_consequence.csv'


fetch_pre(filename, file_afterpre)
fetch_data(file_afterpre, file_afterfetch)
amount_drawn(file_afterfetch, consequence_file)

# final_file = filename[:-4] + '_finaloutput.csv'
# distinct(consequence_file, final_file)
