#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os 

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet WORDPRESS TARAMA")

print("""
---------------------------------------------------------------------------------------------------------
------------------------Wordpress Tarama Programına Hoşgeldiniz.-----------------------------------------
---------------------------------------------------------------------------------------------------------
-----------------------1) Hızlı Tarama-------------------------------------------------------------------
-----------------------2) Eklenti Tarama-----------------------------------------------------------------
-----------------------3) Tema Tarama--------------------------------------------------------------------
-----------------------4) Yönetici Kullanıcı Adı Tarama--------------------------------------------------
---------------------------------------------------------------------------------------------------------
-------------------------------------Ferhat Sara---------------------------------------------------------
---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------
""")

number=raw_input("İşlem Numarası Girin:  ")

if(number=="1"):
 	site=raw_input("Hedef Site Girin: ")
	os.system("wpscan --url "+site)
elif(number=="2"):
 	site=raw_input("Hedef Site Girin: ")
	os.system("wpscan --url "+site+" --enumerate p")
elif(number=="3"):
 	site=raw_input("Hedef Site Girin: ")
	os.system("wpscan --url "+site+" --enumerate t")
elif(number=="4"):
 	site=raw_input("Hedef Site Girin: ")
	os.system("wpscan --url "+site+" --enumerate u")
else:
	print("Hatalı Seçim Yaptınız. Program Kapatılıyor.")
