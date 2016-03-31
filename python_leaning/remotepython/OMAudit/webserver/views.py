#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
import MySQLdb
import socket
from webserver.models import *
import time
from django.shortcuts import render_to_response


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

def searchdb(string,T):
    db =MySQLdb.connect(host="192.168.5.46",user="root",passwd="123456",db="test",charset="utf8")
    cursor = db.cursor()    # 使用cursor()方法获取操作游标
    sql = "SELECT * from history where history_datetime>\'"+T+"\' ORDER BY history_datetime limit 100"
    htmlstring = string + "<table>"
    try:
        cursor.execute(sql)            #执行sql语句
        results = cursor.fetchall()     #获取所有记录列表
        for row in results:
            id = str(row[0])
            ip = str(row[1])
            user = str(row[2])
            datetime = str(row[3])
            command = str(row[4])
            htmlstring += "<tr><td>"+id+"</td><td>"+ip+"</td><td>"+user+"</td><td>"+datetime+"</td><td>"+command+"</td></tr>"

            #print id,ip,user,datetime,command
        #htmlstring += "</table>"
        return htmlstring
    except:
        db.rollback()
        htmlstring = "search mysql filed"
        return htmlstring
    db.close()                           #关闭数据库连接

def searchmysql(string,host,Time,command):
    db =MySQLdb.connect(host="192.168.5.46",user="root",passwd="123456",db="test",charset="utf8")
    cursor = db.cursor()    # 使用cursor()方法获取操作游标
    sql = "SELECT * from history where history_datetime like \'%"+Time+"%\' and history_ip like \'%"+host+"%\' and history_command like  \'%"+command+"%\'ORDER BY history_datetime  "
    htmlstring = string + "<table><tr><td>ID</td><td>HOST</td><td>USER</td><td>TIME</td><td>COMMAND</td></tr>"
    try:
        cursor.execute(sql)            #执行sql语句
        results = cursor.fetchall()     #获取所有记录列表
        for row in results:
            id = str(row[0])
            ip = str(row[1])
            user = str(row[2])
            datetime = str(row[3])
            command = str(row[4])
            htmlstring += "<tr><td>"+id+"</td><td>"+ip+"</td><td>"+user+"</td><td>"+datetime+"</td><td>"+command+"</td></tr>"

            #print id,ip,user,datetime,command
        #htmlstring += "</table>"
        return htmlstring
    except:
        db.rollback()
        htmlstring = "search mysql filed"
        return htmlstring
    db.close()                           #关闭数据库连接

def omaudit_run(request):
    T = time.strftime("%Y-%m-%d")
    host = request.GET.get('T_0', 'default value')
    Time = request.GET.get('T_1', 'default value')
    cmd = request.GET.get('T_2', 'default value')
    serverweb = """<html>
<head>
<script type="text/javascript">
   function searchtime(){
		val = document.getElementById("aa").value;
		document.getElementById("testid").innerText = val;
		return true;
   }
</script>
</head>
<body>
<h1 id="testid">请输入查询条件：</h1>
<form id="formid" action="" method="get">
  Host:
  <input type="text" id="T_0" name="T_0"/>
   Time :
  <input type="text" id="T_1" name="T_1"/>
    Command:
  <input type="text" id="T_2" name="T_2"/>
  <input type="submit" value="Submit" onclick="searchtime();"/>
</form>
</body>
</html>"""
#    serverstring=searchdb(serverweb,Time)
    serverstring=searchmysql(serverweb,host,Time,cmd)
    return HttpResponse(serverstring)

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
