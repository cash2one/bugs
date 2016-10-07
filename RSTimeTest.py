#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import datetime

try:
    user_agent  = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    # user_agent  = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0"
    headers     = { 'User-Agent' : user_agent }
    # apiUrl      = "https://api.coinmarketcap.com/v1/ticker/"
    apiUrl      = "http://yun.baidu.com/pcloud/friend/getfollowlist?query_uk=1327787586&limit=25&start=0"
    start = ""
    end = ""
    tdiff = ""
    status_code = 200
    diff_max = ""
    diff_min = ""
    r = ""
    
    # r = requests.get(apiUrl,headers = headers)
    # print r.status_code

    while 1:
        start = datetime.datetime.now()
        status_code = 0
        while status_code <> 200:
            r = requests.get(apiUrl,headers = headers)
            status_code = r.status_code
            
            end = datetime.datetime.now()
            # tdiff = str(end - start)
            tdiff = (end - start).total_seconds()

            print status_code,start, end, tdiff

            if diff_max == "" :
                diff_max = tdiff
            if diff_min == "" :
                diff_min = tdiff
            if tdiff > diff_max:
                diff_max = tdiff
            if tdiff < diff_min:
                diff_min = tdiff

except:
    print("ERROR!")
    print("status_code = "), r.status_code
    print "diff_max: " , diff_max
    print "diff_min: " , diff_min
