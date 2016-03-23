#!/usr/bin/python
import paramiko
import os,sys,time

blip = "192.168.5.87"
bluser = "ubuntu"
blpasswd = "Tzm192"

hostname = "192.168.5.21"
username = "root"
password = "Asto100"
cmd = "ifconfig"

port = 5000
passinfo = '\'s password:'
paramiko.util.log_to_file('syslogin.log')

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=blip,username=bluser,password=blpasswd)

channel=ssh.invoke_shell()
channel.settimeout(10)

buff='11111111'
resp=''
time.sleep(5)
channel.send('ssh '+'-p 5000 '+username+'@'+hostname+'\n')
#while not buff.endswith(passinfo):
#    try:
#        resp = channel.recv(9999)
#    except Exception, e:
#        print 'Error info:%s connection time.' % (str(e))
#        channel.close()
#        ssh.close()
#        sys.exit()
#    buff += resp
#    if not buff.find('yes/no') == -1:
#        channel.send('yes\n')
#        buff=''
resp = channel.recv(9999)
buff += resp
time.sleep(10)
channel.send(password+'\n')
#buff=''
#while not buff.endswith('# '):
#    resp = channel.recv(9999)
#    if not resp.find(passinfo) == -1:
#        print 'Error info: Authentication failed.'
#        channel.close()
#        ssh.close()
#        sys.exit()
#    buff += resp
resp = channel.recv(9999)
buff += resp
time.sleep(5)
#channel.send('ifconfig'+'\n')
channel.send(cmd+'\n')
#buff=''
#try:
#    while buff.find('# ') == -1:
#        resp=channel.recv(9999)
#        buff += resp
#time.sleep(5)
resp = channel.recv(9999)
buff += resp
#except Exception,e:
#    print "error info:"+str(e)

print buff
print resp
channel.close()
ssh.close()