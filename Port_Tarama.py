#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os 

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet PORT TARAMA")

print("""
Port Tarama Programına Hoş Geldiniz.
-------------------------------------------------------------------
--------------------1)Standart Tarama------------------------------
--------------------2)Servis ve Versiyon Bilgisi-------------------
--------------------3)İşletim Sistemi Bilgisi----------------------
--------------------4)Agresif tarama-------------------------------
--------------------5)Güvenlik Duvarı Tespiti----------------------
--------------------6)Hızlı Tarama---------------------------------
-------------------------------------------------------------------
-------------------------------------------------------------------
-------------------------*Ferhat SARA*-----------------------------
-------------------------------------------------------------------
-------------------------------------------------------------------


""")

islemno=raw_input("İşlem Numarası Girin: ")

if(islemno=="1"):
	hedefip=raw_input("Hedef İp Girin:  ")
	os.system("nmap " + hedefip)
elif(islemno=="2"):
	hedefip=raw_input("Hedef İp Girin:  ")
	os.system("nmap -sS -sV " + hedefip)
elif (islemno=="3"):
	hedefip=raw_input("Hedef İp Girin:  ")
	os.system("nmap -O " + hedefip)
elif (islemno=="4"):
	hedefip=raw_input("Hedef İp Girin:  ")
	os.system("nmap -A " + hedefip)
elif (islemno=="5"):
	hedefip=raw_input("Hedef İp Girin:  ")
	os.system("nmap --script http-waf-detect " + hedefip)
elif (islemno=="6"):
	hedefip=raw_input("Hedef İp Girin:  ")
	os.system("nmap -F " + hedefip)
else:
	print("Hatalı Seçim Yaptınız. Program Kapatılıyor.")
