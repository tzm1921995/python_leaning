#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
import socket
from webserver.models import *

def index(request):
    return HttpResponse(u'welcome')

def omaudit_run(request):
    if not 'LastID' in request.GET:
        LastID=""
    else:
        LastID=request.GET['LastID']
    if not 'hosts' in request.GET:
        Hosts=""
    else:
        Hosts=request.GET['hosts']
    ServerHistory_string=""
    host_array=str(Hosts).split(';')

    if LastID=="0":
        if Hosts=="":
            ServerHistoryObj = ServerHistory.objects.order_by('-id')[:5]
        else:
            ServerHistoryObj = ServerHistory.objects.filter(history_ip__in=host_array).order_by('-id')[:5]

    else:
        if Hosts=="":
            print LastID
            ServerHistoryObj = ServerHistory.objects.filter(id__gt=LastID).order_by('-id')
        else:
            ServerHistoryObj = ServerHistory.objects.filter(id__gt=LastID,history_ip__in=host_array).order_by('-id')

    lastid=""
    i=0
    for e in ServerHistoryObj:
        if i==0:
            lastid=e.id
        ServerHistory_string+="<fcnt color=#cccccc>"+e.history_ip+"</font>&nbsp;&nbsp;\t"+e.history_user+"&nbsp;&nbsp;\t"+str(e.db_datetime)+"\t # <font color=#ffffff>"+e.history_command+"</font>*"
        i+=1

    ServerHistory_string+="@@"+str(lastid)
    return HttpResponse(ServerHistory_string)

def omaudit_pull(request):
    if request.method == 'GET':
        if not request.GET.get('history_id', ' '):
            return HttpResponse("history_id null")
        if not request.GET.get('history_ip', ' '):
            return HttpResponse("history_ip null")
        if not request.GET.get('history_user', ' '):
            return HttpResponse("history_user null")
        if not request.GET.get('history_datetime', ' '):
            return HttpResponse("history_datetime null")
        if not request.GET.get('history_command', ' '):
            return HttpResponse("history_command null")

        history_id=request.GET['history_id']
        history_ip=request.GET['history_ip']
        history_user=request.GET['history_user']
        history_datetime=request.GET['history_datetime']
        history_command=request.GET['history_command']

        historyobj = ServerHistory(history_id=history_id,history_ip=history_ip,history_user=history_user,history_datetime=history_datetime,history_command=history_command)
        try:
            print history_id
            print history_ip
            print history_user
            print history_datetime
            print history_command
            historyobj.save()
            print 'sucessful'
        except Exception,e:
            return HttpResponse("入库失败"+str(e))
            print "入库失败"

        Response_result="OK"
        print "22222222222222222222"
        return HttpResponse(Response_result)
    else:
        return HttpResponse("非法提交！")

# Create your views here.
