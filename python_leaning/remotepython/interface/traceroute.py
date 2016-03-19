#!/usr/local/bin/ipython
#coding: utf-8
import os,sys,time,subprocess
import warnings,logging
warnings.filterwarnings("ignore", category=DeprecationWarning)  #屏蔽scapy无用告警信息
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)      #屏蔽模块IPV6多余警告
from scapy.all import traceroute
domains = raw_input('Please input one or more IP/domain:')      #输入ip或域名
target = domains.split(' ')
dport = [80]                                                    #扫描的端口列表

if len(target) >= 1 and target[0]!='':
    res,unans = traceroute(target,dport=dport,retry=-2)         #启动路由跟踪
    res.graph(target="> test.svg")                              #生成svg矢量图形
    time.sleep(1)
    subprocess.Popen("/usr/bin/convert test.svg test.png", shell=True) #svg转png
else:
    print "IP/domain number of errors,exit"