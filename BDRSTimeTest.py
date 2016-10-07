#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import datetime
import time

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
    r_errno = 0
    
    # r = requests.get(apiUrl,headers = headers)
    # print r.status_code
    # print r.json()["errno"]

    while 1:
        start = datetime.datetime.now()
        status_code = 0
        r_errno = -1
        while status_code <> 200 and r_errno <> 0 :
            time.sleep(0.3)
            r = requests.get(apiUrl, headers = headers, timeout=None)
            status_code = r.status_code
            r_errno = r.json()["errno"]            
            
            end = datetime.datetime.now()
            # tdiff = str(end - start)
            tdiff = (end - start).total_seconds()

            print status_code, r_errno, start, end, tdiff
            if r_errno == -55:
                time.sleep(60)

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
