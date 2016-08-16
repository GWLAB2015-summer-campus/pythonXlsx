#!/usr/bin/python

import json
import getpass
import hashlib

DEFAULT_HOST = '192.168.0.236'
DEFAULT_USER = 'pms'
DEFAULT_NAME = 'pmsdb'

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



while True:
 print "DATABASE_PASSWD"
 data['DATABASE_PASSWD'] = getpass.getpass()
 if(data['DATABASE_PASSWD'] != ""):
  SHA = hashlib.sha512()
  SHA.update(data['DATABASE_PASSWD'])
  sha512 = SHA.hexdigest()
  data['DATABASE_PASSWD'] = sha512.upper()
  break
 else:
  print "Must input a password"




file = open("config.json",'w')
file.write(json.dumps(data, sort_keys=True, indent=4))


