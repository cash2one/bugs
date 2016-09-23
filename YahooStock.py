# -*- coding: utf-8 -*-
import urllib

'''
I dont's konw why SH data can't get from below code.
SZ's today data is normally get from request.
So,I wil try SINA StockAPI for data.

http://ichart.yahoo.com/table.csv?s=600000.SS&a=08&b=22&c=2016&d=08&e=23&f=2016&g=d
http://ichart.yahoo.com/table.csv?s=000881.SZ&a=08&b=22&c=2016&d=08&e=23&f=2016&g=d
'''
stockList = [ \
            "000001.ss",
            "399001.sz",
            "000300.ss",
            "000881.sz",
            "600802.ss",
            "600200.ss",
            "000882.sz"
            ];

strStockList = ""
for i in range(len(stockList)):
    if strStockList == "" :
        strStockList += stockList[i]
    else :
        strStockList += "+" + stockList[i]

# print strStockList

stockURL = "http://finance.yahoo.com/d/quotes.csv?s=%s&f=sl1d1t1c1ohgv&e=.csv" % strStockList

# print "stockURL:\n" ,stockURL
    
socket = urllib.urlopen(stockURL)
readSocket = socket.read()
socket.close()
# print readSocket

stockValueList = readSocket.strip().split('\n')
# print stockValueList

print "Symbol     LastPrice      Change       Open       High        Low       Volume"
for i in stockValueList:
    i.strip()
    listInfo = i.split(",")

    listInfo[0] = listInfo[0].replace("\"","")
    listInfo[0] = listInfo[0].replace(".ss","")
    listInfo[0] = listInfo[0].replace(".sz","")
    
    print "%-10s %+10s %+10s %+10s %+10s %+10s %12s" % (listInfo[0],listInfo[1],listInfo[4],listInfo[5],listInfo[6],listInfo[7],listInfo[8],)
