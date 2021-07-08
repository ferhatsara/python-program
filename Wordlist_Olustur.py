#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Wordlist Olustur")

print("""

-------------------------------------------------------------------
------------Wordlist Oluşturma Programına Hoşgeldiniz.-------------
-------------------------------------------------------------------
-------------------------*Ferhat SARA*-----------------------------
-------------------------------------------------------------------
-------------------------------------------------------------------


""")

mincharacter=raw_input("Minumum Karakter Sayısı Girin:  ")
maxcharacter=raw_input("Max Karakter Sayısı Girin:  ")
character=raw_input("İstediğiniz Karakterleri Girin:  ")
storage=raw_input("Kaydedilecek Yeri Girin:  (Example: /root/Desktop/wordlist.txt")

os.system("crunch "+mincharacter+" "+maxcharacter+" "+character+" -o "+storage)

print("İşlem Başarıyla Tamamlandı.")
