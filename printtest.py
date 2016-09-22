# -*- coding: utf-8 -*-

stockList = [ \
            "000881.sz",
            "600802.ss",
            "600200.ss"
            ];

strStockList = ""
# print type(stockList)

for i in range(len(stockList)):
    if strStockList == "" :
        strStockList += stockList[i]
    else :
        strStockList += "+" + stockList[i]

print strStockList

stockURL = "http://finance.yahoo.com/d/quotes.csv?s=%s&f=sl1d1t1c1ohgv&e=.csv" % strStockList

print "stockURL:\n" ,stockURL
