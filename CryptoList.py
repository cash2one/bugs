# -*- coding: utf-8 -*-

import urllib
import urllib2
import re

#去除img标签,7位长空格
removeImg = re.compile('<img.*?>| {7}|')
#删除超链接标签
removeAddr = re.compile('<a.*?>|</a>')
#把换行的标签换为\n
replaceLine = re.compile('<tr>|<div>|</div>|</p>')
#将表格制表<td>替换为\t
replaceTD= re.compile('<td>')
#把段落开头换为\n加空两格
replacePara = re.compile('<p.*?>')
#将换行符或双换行符替换为\n
replaceBR = re.compile('<br><br>|<br>')
#将空格替换为空
replaceSpace = re.compile(' ')
#将多个空行替换为1个
replaceLine = re.compile('\n\n')
#将其余标签剔除
removeExtraTag = re.compile('<.*?>')
def replace(x):
    x = re.sub(removeImg,"",x)
    x = re.sub(removeAddr,"",x)
    x = re.sub(replaceLine,"",x)
    x = re.sub(replaceTD,"",x)
    x = re.sub(replacePara,"",x)
    x = re.sub(replaceBR,"",x)
    x = re.sub(replaceSpace,"",x)
    x = re.sub(removeExtraTag,"",x)
    x = re.sub("\*","",x)

    x = re.sub(replaceLine,"\n",x)
    x = re.sub(replaceLine,"\n",x)
    x = re.sub(replaceLine,"\n",x)
    x = re.sub("\n","\t",x)

    #strip()将前后多余内容删除
    return x.strip()

url = 'http://coinmarketcap.com'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    
    pattern = re.compile('<tr id="id-.*?<td.*?<td.*?<td.*?<td.*?<td.*?<td.*?<td.*?<td.*?</tr>',re.S)
    items = re.findall(pattern,content)
    
    print "#   Name           Market Cap      Price         Available       Name2     Volume (24h)  % Change (24h)	"
    print "-------------------------------------------------------------------------------------------------------"
    for item in items:
        item = replace(item)
        itemdetail = item.split()
        print ('%-4s%-15s%-16s%-14s%-16s%-10s%-14s%-10s' % (itemdetail[0],itemdetail[1],itemdetail[2],itemdetail[3],itemdetail[4],itemdetail[5],itemdetail[6],itemdetail[7]))
#        print item
    
except urllib2.URLError, e:
    print("error!")
#    if hasattr(e,"code"):
#        print e.code
#    if hasattr(e,"reason"):
#        print e.reason


