#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os 

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet VPN Kontrol")
print("""
-------------------------------------------------------------------
---------------VPN Kontrol Programına Hoşgeldiniz------------------
-------------------------------------------------------------------
-------------------------*Ferhat SARA*-----------------------------
-------------------------------------------------------------------

""")

hedefip=raw_input("Hedef İp Girin:  ")
os.system("ike-scan "+hedefip)