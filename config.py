#!/usr/bin/python

import json
DEFAULT_HOST = '192.168.0.236'
DEFAULT_USER = 'pms'
DEFAULT_NAME = 'pmsdb'
DEFAULT_PASSWD = 'pms'

data ={}
print "### DATABASE CONFIG ###\n"


print "DATABASE_HOST (default : "+DEFAULT_HOST+ ") : "
data['DATABASE_HOST'] = raw_input()
if(data['DATABASE_HOST'] == ""):
    data['DATABASE_HOST'] = DEFAULT_HOST;




print "DATABASE_USER (default : "+DEFAULT_USER+ ") :"
data['DATABASE_USER'] = raw_input()
if(data['DATABASE_USER'] == ""):
    data['DATABASE_USER'] = DEFAULT_USER;



print "DATABASE_NAME (default : "+DEFAULT_NAME+ ") :"
data['DATABASE_NAME'] = raw_input()
if(data['DATABASE_NAME'] == ""):
    data['DATABASE_NAME'] = DEFAULT_NAME;



print "DATABASE_PASSWD (default : "+DEFAULT_PASSWD+ ") :"
data['DATABASE_PASSWD'] = raw_input()
if(data['DATABASE_PASSWD'] == ""):
    data['DATABASE_PASSWD'] = DEFAULT_PASSWD;



file = open("config.json",'w')
file.write(json.dumps(data, sort_keys=True, indent=4))


