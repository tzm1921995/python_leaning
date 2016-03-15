import smtplib
import string
HOST = "smtp.163.com"  #定义smtp服务器
SUBJECT = "Test email from Python"   #定义邮件主题
TO = "tzm1921995@foxmail.com"       #定义收件人
FROM = "tzm1921995@163.com"         #发件人
text = "Python rules then all!"         #邮件内容
BODY = string.join((
    "From: %s" % FROM,
    "To: %s" % TO,
    "Subject: %s" % SUBJECT,
    "",
    text
), "\r\n")
server = smtplib.SMTP()
server.connect(HOST,"25")
server.starttls()
server.login("tzm1921995@163.com","*****")
server.sendmail(FROM,[TO],BODY)
server.quit()