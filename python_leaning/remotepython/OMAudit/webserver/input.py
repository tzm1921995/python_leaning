#!/usr/bin/python
import cgi
form = cgi.FieldStorage()
print "date:" + form["T_2"].value