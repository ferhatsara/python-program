#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("apt-get install macchanger")
os.system("clear")
os.system("figlet MAC Degistirme")

print("""
MAC Adres Değiştirme Programına Hoşgeldiniz.

1)MAC Adresi Random Belirleme
2)MAC Adresi Elle Belirle 
3)MAC Adresi Orjinale Döndür
""")

islemno=raw_input("İşlem No Girin:  ")

if(islemno=="1"):
	print("""



	1)eth0
	2)wlan0


	""")

	device=raw_input("Aygıt seçin:  ")

	if(device=="1"):
		os.system("ifconfig eth0 down")
		os.system("macchanger -r eth0")
		os.system("ifconfig eth0 up")
		print("\033[92mYeni MAC Adresi Random Belirlendi")
	if(device=="2"):
		os.system("ifconfig wlan0 down")
		os.system("macchanger -r wlan0")
		os.system("ifconfig wlan0 up")
		print("\033[92mYeni MAC Adresi Random Belirlendi")

if(islemno=="2"):
	print("""



	1)eth0
	2)wlan0


	""")

	device=raw_input("Aygıt seçin:  ")

	if(device=="1"):
		macadres=raw_input("Yeni MAC Adresi Girin:  ")
		os.system("ifconfig eth0 down")
		os.system("macchanger --mac " + macadres +" eth0")
		os.system("ifconfig eth0 up")
		print("\033[92mYeni MAC Adresi Manuel Belirlendi")
	if(device=="2"):
		macadres=raw_input("Yeni MAC Adresi Girin:  ")
		os.system("ifconfig wlan0 down")
		os.system("macchanger --mac " + macadres+" eth0")
		os.system("ifconfig wlan0 up")
		print("\033[92mYeni MAC Adresi Manuel Belirlendi")

if(islemno=="3"):
	print("""



	1)eth0
	2)wlan0


	""")

	device=raw_input("Aygıt seçin:  ")

	if(device=="1"):		
		os.system("ifconfig eth0 down")
		os.system("macchanger -p eth0")
		os.system("ifconfig eth0 up")
		print("\033[92mYeni MAC Adresi Orjinale Döndürüldü")
	if(device=="2"):
		os.system("ifconfig wlan0 down")
		os.system("macchanger -p wlan0")
		os.system("ifconfig wlan0 up")
		print("\033[92mYeni MAC Adresi Orjinale Döndürüldü")

