import datetime
import requests
import os
from tkinter import *

def get_vul_site_list():
    response = requests.get("https://www.usom.gov.tr/url-list.txt")
    dosya = open("usom.txt", "w")
    dosya.write(response.text)
    dosya.close()

    msg=usom_txt_kontrol()


def kontrol_et():
    dosya = open("usom.txt", "r")
    contents = dosya.read()
    dosya.close()

    ip = entry1.get()
    ip = str(ip).strip()
    today = datetime.datetime.now()
    zararliMi = False
    contents = contents.split("\n")
    
    for x in contents:
        if x == ip:
            zararliMi = True
            break
    
    if zararliMi:
        dosya = open("log.txt", "a")
        yazi = ip + " Zararlıdır!\n" + "Tarih: " + str(today) + "\n"
        dosya.write(yazi)
        dosya.close()
        v.set("Zararlıdır!")
    else:
        dosya = open("log.txt", "a")
        yazi = ip + " Zararlı değildir.\n" + "Tarih: " + str(today) + "\n"
        dosya.write(yazi)
        dosya.close()
        v.set("Zararlı değildir.")


def usom_txt_kontrol():
    if os.path.isfile("usom.txt"):
        g.set("Usom Listesi Güncelle")
    else:
        g.set("Usom Listesi İndir")
    

pencere=Tk()
pencere.title("USOM Kontrol Uygulaması")

g=StringVar()
usom_txt_kontrol()

btn0=Button(pencere, textvariable=g,command=get_vul_site_list)
btn0.place(x=50,y=10)
btn0.pack()

label0=Label(pencere,text="Kontrol Edilecek URL")
label0.place(x=50,y=80)
label0.pack()

entry1= Entry(pencere)
entry1.place(x=50,y=100)
entry1.pack()

label1= Label(pencere,text="Sonuç")
label1.place(x=50,y=120)
label1.pack()

v=StringVar()
entry2= Entry(pencere,textvariable=v)
entry2.place(x=50,y=130)
entry2.pack()

btn1= Button(pencere,text="Kontrol Et",command=kontrol_et)
btn1.place(x=50,y=140)
btn1.pack()


pencere.mainloop()