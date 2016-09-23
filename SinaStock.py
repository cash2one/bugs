# -*- coding: utf-8 -*-

import urllib

'''
http://hq.sinajs.cn/list=sh601003,sh601001

index --> values
0：”大秦铁路”，股票名字；
1：”27.55″，今日开盘价；
2：”27.25″，昨日收盘价；
3：”26.91″，当前价格；
4：”27.55″，今日最高价；
5：”26.20″，今日最低价；
6：”26.91″，竞买价，即“买一”报价；
7：”26.92″，竞卖价，即“卖一”报价；
8：”22114263″，成交的股票数，由于股票交易以一百股为基本单位，所以在使用时，通常把该值除以一百；
9：”589824680″，成交金额，单位为“元”，为了一目了然，通常以“万元”为成交金额的单位，所以通常把该值除以一万；
10：”4695″，“买一”申请4695股，即47手；
11：”26.91″，“买一”报价；
12：”57590″，“买二”
13：”26.90″，“买二”
14：”14700″，“买三”
15：”26.89″，“买三”
16：”14300″，“买四”
17：”26.88″，“买四”
18：”15100″，“买五”
19：”26.87″，“买五”
20：”3100″，“卖一”申报3100股，即31手；
21：”26.92″，“卖一”报价
(22, 23), (24, 25), (26,27), (28, 29)分别为“卖二”至“卖四的情况”
30：”2008-01-11″，日期；
31：”15:05:32″，时间；

查看日K线图
http://image.sinajs.cn/newchart/daily/n/sh601006.gif

分时线的查询：
http://image.sinajs.cn/newchart/min/n/sh000001.gif

日K线查询：
http://image.sinajs.cn/newchart/daily/n/sh000001.gif

周K线查询：
http://image.sinajs.cn/newchart/weekly/n/sh000001.gif

月K线查询：
http://image.sinajs.cn/newchart/monthly/n/sh000001.gif
'''
stockList = [ \
            "sh000001",
            "sz399001",
            "sh000300",
            "sz000881",
            "sh600802",
            "sh600200"
            ];

strStockList = ""
for i in range(len(stockList)):
    if strStockList == "" :
        strStockList += stockList[i]
    else :
        strStockList += "," + stockList[i]

# print strStockList

stockURL = "http://hq.sinajs.cn/list=%s" % strStockList

# print "stockURL:\n" ,stockURL
    
socket = urllib.urlopen(stockURL)
readSocket = socket.read()
socket.close()
# print readSocket

stockValueList = readSocket.strip().split('\n')

# print "Symbol    LastPrice       Open        Now   Change      %       Hith        Low       Volume         TotalPrice"
# print "----------------------------------------------------------------------------------------------------------------"

print "Symbol    LastPrice       Open        Now   Change      %       Hith        Low"
print "-------------------------------------------------------------------------------"

for i in range(len(stockValueList)):
    # i.strip()
    listInfo = stockValueList[i]
    listInfo = listInfo[21:-2]
    # print listInfo
    listInfo = listInfo.split(",")
    # print len(listInfo)
    
    change = ((float(listInfo[3])-float(listInfo[2]))/float(listInfo[3]))*100
    
    # print "%-8s %+10s %+10s %+10s %+8.2f %+6.2f %+10s %+10s %12s %18s" % (stockList[i],(listInfo[2]),(listInfo[1]),listInfo[3],float(listInfo[3])-float(listInfo[1]),change,listInfo[4],listInfo[5],listInfo[8],listInfo[9])
    print "%-8s %+10s %+10s %+10s %+8.2f %+6.2f %+10s %+10s" % (stockList[i],(listInfo[2]),(listInfo[1]),listInfo[3],float(listInfo[3])-float(listInfo[2]),change,listInfo[4],listInfo[5])
