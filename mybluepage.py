# -*- coding: utf-8 -*-

import requests
import json
import time
import ctypes,sys
import os
 
STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12
 
# 字体颜色定义 ,关键在于颜色编码，由2位十六进制组成，分别取0~f，前一位指的是背景色，后一位指的是字体色
#由于该函数的限制，应该是只有这16种，可以前景色与背景色组合。也可以几种颜色通过或运算组合，组合后还是在这16种颜色中
 
# Windows CMD命令行 字体颜色定义 text colors
FOREGROUND_BLACK = 0x00 # black.
FOREGROUND_DARKBLUE = 0x01 # dark blue.
FOREGROUND_DARKGREEN = 0x02 # dark green.
FOREGROUND_DARKSKYBLUE = 0x03 # dark skyblue.
FOREGROUND_DARKRED = 0x04 # dark red.
FOREGROUND_DARKPINK = 0x05 # dark pink.
FOREGROUND_DARKYELLOW = 0x06 # dark yellow.
FOREGROUND_DARKWHITE = 0x07 # dark white.
FOREGROUND_DARKGRAY = 0x08 # dark gray.
FOREGROUND_BLUE = 0x09 # blue.
FOREGROUND_GREEN = 0x0a # green.
FOREGROUND_SKYBLUE = 0x0b # skyblue.
FOREGROUND_RED = 0x0c # red.
FOREGROUND_PINK = 0x0d # pink.
FOREGROUND_YELLOW = 0x0e # yellow.
FOREGROUND_WHITE = 0x0f # white.
 
 
# Windows CMD命令行 背景颜色定义 background colors
BACKGROUND_BLUE = 0x10 # dark blue.
BACKGROUND_GREEN = 0x20 # dark green.
BACKGROUND_DARKSKYBLUE = 0x30 # dark skyblue.
BACKGROUND_DARKRED = 0x40 # dark red.
BACKGROUND_DARKPINK = 0x50 # dark pink.
BACKGROUND_DARKYELLOW = 0x60 # dark yellow.
BACKGROUND_DARKWHITE = 0x70 # dark white.
BACKGROUND_DARKGRAY = 0x80 # dark gray.
BACKGROUND_BLUE = 0x90 # blue.
BACKGROUND_GREEN = 0xa0 # green.
BACKGROUND_SKYBLUE = 0xb0 # skyblue.
BACKGROUND_RED = 0xc0 # red.
BACKGROUND_PINK = 0xd0 # pink.
BACKGROUND_YELLOW = 0xe0 # yellow.
BACKGROUND_WHITE = 0xf0 # white.
 
 
 
# get handle
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
 
def set_cmd_text_color(color, handle=std_out_handle):
    Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return Bool
 
#reset white
def resetColor():
    set_cmd_text_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)
 
###############################################################
 
#暗蓝色
#dark blue
def printDarkBlue(mess):
    set_cmd_text_color(FOREGROUND_DARKBLUE)
    sys.stdout.write(mess)
    resetColor()
 
#暗绿色
#dark green
def printDarkGreen(mess):
    set_cmd_text_color(FOREGROUND_DARKGREEN)
    sys.stdout.write(mess)
    resetColor()
 
#暗天蓝色
#dark sky blue
def printDarkSkyBlue(mess):
    set_cmd_text_color(FOREGROUND_DARKSKYBLUE)
    sys.stdout.write(mess)
    resetColor()
 
#暗红色
#dark red
def printDarkRed(mess):
    set_cmd_text_color(FOREGROUND_DARKRED)
    sys.stdout.write(mess)
    resetColor()
 
#暗粉红色
#dark pink
def printDarkPink(mess):
    set_cmd_text_color(FOREGROUND_DARKPINK)
    sys.stdout.write(mess)
    resetColor()
 
#暗黄色
#dark yellow
def printDarkYellow(mess):
    set_cmd_text_color(FOREGROUND_DARKYELLOW)
    sys.stdout.write(mess)
    resetColor()
 
#暗白色
#dark white
def printDarkWhite(mess):
    set_cmd_text_color(FOREGROUND_DARKWHITE)
    sys.stdout.write(mess)
    resetColor()
 
#暗灰色
#dark gray
def printDarkGray(mess):
    set_cmd_text_color(FOREGROUND_DARKGRAY)
    sys.stdout.write(mess)
    resetColor()
 
#蓝色
#blue
def printBlue(mess):
    set_cmd_text_color(FOREGROUND_BLUE)
    sys.stdout.write(mess)
    resetColor()
 
#绿色
#green
def printGreen(mess):
    set_cmd_text_color(FOREGROUND_GREEN)
    sys.stdout.write(mess)
    resetColor()
 
#天蓝色
#sky blue
def printSkyBlue(mess):
    set_cmd_text_color(FOREGROUND_SKYBLUE)
    sys.stdout.write(mess)
    resetColor()
 
#红色
#red
def printRed(mess):
    set_cmd_text_color(FOREGROUND_RED)
    sys.stdout.write(mess)
    resetColor()
 
#粉红色
#pink
def printPink(mess):
    set_cmd_text_color(FOREGROUND_PINK)
    sys.stdout.write(mess)
    resetColor()
 
#黄色
#yellow
def printYellow(mess):
    set_cmd_text_color(FOREGROUND_YELLOW)
    sys.stdout.write(mess)
    resetColor()
 
#白色
#white
def printWhite(mess):
    set_cmd_text_color(FOREGROUND_WHITE)
    sys.stdout.write(mess)
    resetColor()
 
##################################################
 
#白底黑字
#white bkground and black text
def printWhiteBlack(mess):
    set_cmd_text_color(FOREGROUND_BLACK | BACKGROUND_WHITE)
    sys.stdout.write(mess)
    resetColor()
 
#白底黑字
#white bkground and black text
def printWhiteBlack_2(mess):
    set_cmd_text_color(0xf0)
    sys.stdout.write(mess)
    resetColor()
 
 
#黄底蓝字
#white bkground and black text
def printYellowRed(mess):
    set_cmd_text_color(BACKGROUND_YELLOW | FOREGROUND_RED)
    sys.stdout.write(mess)
    resetColor()
 
 
##############################################################
try:

    printGreen("================================================================================\n")
    printGreen("This Tool is Writed By Chen Yong,Use For Getting BluePages Infomation\n")
    printGreen("If you have any questions, Please Contact me. Cheers!!!\n")
    printGreen("Notes  : Yong VO Chen/China/IBM\n")
    printGreen("E-mail : sucy@cn.ibm.com\n")
    printGreen("Mobile : (+86)13912614611\n\n")
    printGreen("================================================================================\n")
    printPink("Please Input The Query Key. ")
    printPink("For Example: ")
    printRed("NOTES ID OR INTRANET ID ->>>\n")
    
    query = raw_input()
    print ""
    
    
    nf = open("./mybluepages.txt","w")
    # nf.writelines("This is a file")
    
    
    apiUrl = "http://w3-services1.w3-969.ibm.com/myw3/unified-profile/v1/search/user?searchConfig=optimized_search&rows=24&timeout=2000&query=%s" % query   
    # print apiUrl
    apiURLTeam = "http://w3-services1.w3-969.ibm.com/myw3/unified-profile/v1/docs/instances/teamInfoResolved/"
        
    r = requests.get(apiUrl)
    # print dict(r.json())["results"][0]["uid"]
  
    # print dict(r.json())["results"][0]
    nf.writelines("************************\n") 
    nf.writelines("  PERSON INFORMATAION\n") 
    nf.writelines("************************\n")
    
    nf.writelines("CALLUPNAME          :" + dict(r.json())["results"][0]["callupName"].encode("utf8") + "\n") 
    # print "RESULTLEVEL         :",dict(r.json())["results"][0]["resultLevel"]
    nf.writelines("NAMEFULL            :" + dict(r.json())["results"][0]["nameFull"] + "\n") 
    nf.writelines("CO                  :" + dict(r.json())["results"][0]["co"] + "\n")  
    nf.writelines("UID                 :" + dict(r.json())["results"][0]["uid"] + "\n")  
    if dict(r.json())["results"][0].has_key("telephone_office") :
        nf.writelines("TELEPHONE_OFFICE    :" + dict(r.json())["results"][0]["telephone_office"] + "\n") 
    else:
        nf.writelines("TELEPHONE_OFFICE    : ****" + "\n") 

    nf.writelines("ORG_TITLE           :" + dict(r.json())["results"][0]["org_title"] + "\n") 
    nf.writelines("DEPT_CODE           :" + dict(r.json())["results"][0]["dept_code"] + "\n") 
    nf.writelines("ID                  :" + dict(r.json())["results"][0]["id"] + "\n") 
    nf.writelines("PREFERREDIDENTITY   :" + dict(r.json())["results"][0]["preferredIdentity"] + "\n") 
    # print "SCORE               :",dict(r.json())["results"][0]["score"]
    if dict(r.json())["results"][0].has_key("role") :
        nf.writelines("ROLE                :" + dict(r.json())["results"][0]["role"] + "\n") 
    else:
        nf.writelines("ROLE                : ****" + "\n") 
        
    nf.writelines("MAIL                :" + dict(r.json())["results"][0]["mail"][0] + "\n")  
    nf.writelines("HRORGANIZATIONCODE  :" + dict(r.json())["results"][0]["hrOrganizationCode"] + "\n") 
    nf.writelines("SERIAL              :" + dict(r.json())["results"][0]["serial"] + "\n") 
    nf.writelines("NOTESEMAIL          :" + dict(r.json())["results"][0]["notesEmail"] + "\n") 
    
    apiURLTeam = apiURLTeam + dict(r.json())["results"][0]["uid"]
    # print apiURLTeam
    
    rAll = requests.get(apiURLTeam)
    # print rAll.json()["doc"]["content"]
    # print rAll.json()
        
    nf.writelines("******************************************\n") 
    nf.writelines("  THE SAME TOWER MEMBERS(" + str(len(dict(rAll.json())["doc"]["content"]["incountry"]["peers"])) + ") - INCOUNTRY" + "\n")  
    nf.writelines("******************************************\n") 
    for detail in dict(rAll.json())["doc"]["content"]["incountry"]["peers"]:
        '''
        Mail
        '''   
        if  detail.has_key("preferredIdentity"):
            mail = detail["preferredIdentity"] 
        else:
            mail = "*******@**.ibm.com"
            
        '''
        Rol Title
        '''     
        if  detail.has_key("role"):
            rol = detail["role"].encode("utf8") 
        else:
            rol = "********"
            
            
        nf.writelines( detail["uid"] + " -" + \
        mail  + " -" + \
        detail["name"]["first"].encode("utf8") + " " +detail["name"]["last"].encode("utf8")  + " -" + \
        rol + "\n") 
    
    nf.writelines("************************************\n") 
    nf.writelines("  REPORT MANAGERS(" + str(len(dict(rAll.json())["doc"]["content"]["incountry"]["leadership"])) + ") - INCOUNTRY"  + "\n")  
    nf.writelines("************************************\n") 
    for detail in dict(rAll.json())["doc"]["content"]["incountry"]["leadership"]:
        '''
        Mail
        '''
        if  detail.has_key("preferredIdentity"):
            mail = detail["preferredIdentity"] 
        else:
            mail = "*******@**.ibm.com"
        
        '''
        rol Title
        '''     
        if  detail.has_key("role"):
            rol = detail["role"].encode("utf8")
        else:
            rol = "********"
       
        
        nf.writelines( detail["uid"] + " -" + \
        mail + " -" + \
        detail["name"]["first"].encode("utf8") + " " +detail["name"]["last"].encode("utf8")  + " -"  + \
        rol + "\n") 

    nf.close()
    
    printGreen("OK!!!\n")
    os.system("notepad ./mybluepages.txt")
except:
    print("Sorry,No Result!")



