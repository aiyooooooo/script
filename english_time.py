#-*- coding:utf-8 -*-

import sys
import requests
import re
import time
import logging

login_url = 'http://222.195.158.194/index.php'
temp_url = 'http://222.195.158.194/template/loggingajax.php?whichURL=/login/hponlinetime.php'

username = '16020031092'
password = 'aisa2012'
Input2 = '登 录'

login_data = { 'username' : username , 'password' : password , 'Input2' : Input2 }

s = requests.Session()

logging.info( '%s is login......' % username )
r = s.get( login_url )
r = s.post( login_url , data = login_data )
if r.status_code != 200:
	logging.warning( 'login error' )

while( 1 ):
	r = s.get( temp_url )
	if r.status_code != 200:
		logging.warning( 'error' )
	r = s.get ( 'http://222.195.158.194/login/hponlinetime.php' )
	if r.status_code != 200:
		logging.warning( 'error' )
	key =  r.content
	p1 = r" (.+?) </td><"
	pattern = re.compile(p1)
	matcher = re.findall(pattern,key)
	print matcher
	time.sleep(30)

