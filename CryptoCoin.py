# -*- coding: utf-8 -*-

import requests
import json
import time

'''
    CoinMarketCap JSON API Documentation
    http://coinmarketcap.com/api/
    
    
    Ticker
    --------------------------
    Endpoint: /ticker/
    Method: GET
    Optional parameters:
        (int) limit - only returns the top limit results.
    Example: https://api.coinmarketcap.com/v1/ticker/
    Example: https://api.coinmarketcap.com/v1/ticker?limit=10
    Sample Response:
    [
        {
            "id": "bitcoin", 
            "name": "Bitcoin", 
            "symbol": "BTC", 
            "rank": "1", 
            "price_usd": "573.137", 
            "price_btc": "1.0", 
            "24h_volume_usd": "72855700.0", 
            "market_cap_usd": "9080883500.0", 
            "available_supply": "15844176.0", 
            "total_supply": "15844176.0", 
            "percent_change_1h": "0.04", 
            "percent_change_24h": "-0.3", 
            "percent_change_7d": "-0.57", 
            "last_updated": "1472762067"
        }, 
        {
            "id": "ethereum", 
            "name": "Ethereum", 
            "symbol": "ETH", 
            "rank": "2", 
            "price_usd": "12.1844", 
            "price_btc": "0.021262", 
            "24h_volume_usd": "24085900.0", 
            "market_cap_usd": "1018098455.0", 
            "available_supply": "83557537.0", 
            "total_supply": "83557537.0", 
            "percent_change_1h": "-0.58", 
            "percent_change_24h": "6.34", 
            "percent_change_7d": "8.59", 
            "last_updated": "1472762062"
        }, 
        ...
    ]	
          
           
    Ticker (Specific Currency)
    --------------------------
    Endpoint: /ticker/{id}/
    Method: GET
    Example: https://api.coinmarketcap.com/v1/ticker/bitcoin/
    Sample Response: 
    [
        {
            "id": "bitcoin", 
            "name": "Bitcoin", 
            "symbol": "BTC", 
            "rank": "1", 
            "price_usd": "573.137", 
            "price_btc": "1.0", 
            "24h_volume_usd": "72855700.0", 
            "market_cap_usd": "9080883500.0", 
            "available_supply": "15844176.0", 
            "total_supply": "15844176.0", 
            "percent_change_1h": "0.04", 
            "percent_change_24h": "-0.3", 
            "percent_change_7d": "-0.57", 
            "last_updated": "1472762067"
        }
    ]			

    Limits
    --------------------------
    Please limit requests to no more than 10 per minute.
    Endpoints update every 5 minutes.
	
'''

# url = 'http://coinmarketcap.com'
# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# headers = { 'User-Agent' : user_agent }
try:
    # user_agent  = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    # headers     = { 'User-Agent' : user_agent }
    apiUrl      = "https://api.coinmarketcap.com/v1/ticker/"
    limitCount  = 50
    apiUrlLimit = apiUrl + "?limit=%s" % limitCount
    spCoinList  = ["Bitcoin","Litecoin","BlackCoin","DigiByte","Dogecoin"]
    apiUrlSp    = apiUrl

    # rs = requests.get(apiUrlLimit, headers =headers )
    r = requests.get(apiUrlLimit)
    # r = requests.get(apiUrl) 
    
    print " NO SYMBOL NAME                PRICE   24H_VOLUME     MARKET_CAP    AVAILABLE        TOTAL  CHG_1H CHG_24H  CHG_7D  LAST_UPDATED" 
    print "-"*135
    for coinDict in r.json():
        if int(coinDict["rank"]) <= 5 or \
        coinDict["name"] in spCoinList:
            print "%+3s %-6s %-16s %8.4f %+12s %+14s %12.0f %12.0f %+7.2f %+7.2f %+7.2f %+20s " % (
                coinDict["rank"], 
                coinDict["symbol"],
                coinDict["name"],
                float(coinDict["price_usd"]),
                coinDict["24h_volume_usd"],
                coinDict["market_cap_usd"],
                float(coinDict["available_supply"]),
                float(coinDict["total_supply"]),
                float(coinDict["percent_change_1h"]),
                float(coinDict["percent_change_24h"]),
                float(coinDict["percent_change_7d"]),
                time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(coinDict["last_updated"])))
                )
    
    '''
    spCoinList  = ["BlackCoin","DigiByte","Dogecoin"]
    apiUrlSp    = apiUrl
    '''
    # print len(spCoinList)
    # apiUrlSp = apiUrl + spCoinList[0]
    # print apiUrlSp
    '''
    for i in range(len(spCoinList)):
        apiUrlSp = apiUrl + spCoinList[i]
        # print apiUrlSp
        r = requests.get(apiUrl + spCoinList[i])
        coinDict = r.json()
        # print coinDict
        for coinDict in r.json():
        pass
    '''
except:
    print("error!")
#    if hasattr(e,"code"):
#        print e.code
#    if hasattr(e,"reason"):
#        print e.reason


