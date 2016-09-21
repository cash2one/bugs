# -*- coding: utf-8 -*-

import pandas
from pandas.io import data 
import matplotlib.pyplot as plt

stockcode = ["000881.sz","600802.ss","600200.ss"]
beginday  = "2016/01/01"

for i in stockcode:
    #print "\n" , i
    stockvalue = pandas.io.data.DataReader(i,"yahoo", start=beginday)
    #print stockvalue.tail(5)
    plt.plot(stockvalue.index, stockvalue["Close"])
    
    #print stockvalue.tail(-1)
    #print stockvalue.index
    #print stockvalue["Close"].tail(1)
    #print type(stockvalue["Close"])

plt.show()
print "end"