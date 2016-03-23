#!/usr/bin/python
import pexpect
import sys

child = pexpect.spawn('ssh ubuntu@192.168.5.47')
#child.sendline("yes")
fout = file('mylog.txt','w')
child.logfile = fout

child.expect("password:")
child.sendline("****")
child.expect('#')
child.sendline('ls /data')
child.expect('#')
