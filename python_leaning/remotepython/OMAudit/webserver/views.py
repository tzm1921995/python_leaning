#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
import MySQLdb
import socket
from webserver.models import *

def index(request):
    return HttpResponse(u'welcome')

def intodb(id,ip,user,datetime,command):
    db = MySQLdb.connect(host="192.168.5.46",user="root",passwd="123456",db="test",charset="utf8")
    cursor = db.cursor()    # 使用cursor()方法获取操作游标
    sql = "INSERT INTO history(history_id,history_ip,history_user,history_datetime,history_command) VALUES ("+ "'"+ id+"'"+","+"'"+ip+"'"+","+"'"+user+"'"+","+"'"+datetime+"'"+","+"'"+command+"'"+")"
    try:
        cursor.execute(sql)            #执行sql语句
        db.commit()                    #提交到数据库执行
        print "已存入数据库"
    except:
        db.rollback()
        print "存入数据库失败"
    db.close()                      #关闭数据库连接


#def omaudit_run(request):
#    if not 'LastID' in request.GET:
#        LastID=""
#    else:
#        LastID=request.GET['LastID']
#    if not 'hosts' in request.GET:
#        Hosts=""
#    else:
#        Hosts=request.GET['hosts']
#    ServerHistory_string=""
#    host_array=str(Hosts).split(';')

#    if LastID=="0":
#        if Hosts=="":
#            ServerHistoryObj = ServerHistory.objects.order_by('-id')[:5]
#        else:
#            ServerHistoryObj = ServerHistory.objects.filter(history_ip__in=host_array).order_by('-id')[:5]

#    else:
#       if Hosts=="":
#            print LastID
#            ServerHistoryObj = ServerHistory.objects.filter(id__gt=LastID).order_by('-id')
#        else:
#            ServerHistoryObj = ServerHistory.objects.filter(id__gt=LastID,history_ip__in=host_array).order_by('-id')

#    lastid=""
#    i=0
#    for e in ServerHistoryObj:
#        if i==0:
#            lastid=e.id
#        ServerHistory_string+="<fcnt color=#cccccc>"+e.history_ip+"</font>&nbsp;&nbsp;\t"+e.history_user+"&nbsp;&nbsp;\t"+str(e.db_datetime)+"\t # <font color=#ffffff>"+e.history_command+"</font>*"
#        i+=1

#    ServerHistory_string+="@@"+str(lastid)
#    return HttpResponse(ServerHistory_string)

def omaudit_run(request):


    ServerHistory_string="<fcnt color=#cccccc>"+request.history_id
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
        history_command=history_command.replace('\'','*')
        history_command=history_command.replace('\"','**')

        try:
            intodb(history_id,history_ip,history_user,history_datetime,history_command)
            omaudit_run(history_id)
        except Exception,e:
            return HttpResponse("入库失败"+str(e))
            print "入库失败"

        Response_result="OK"
        return HttpResponse(Response_result)
    else:
        return HttpResponse("非法提交！")

# Create your views here.
