#!/usr/bin/env python
from tkinter import *
import time
import re
import smtplib
import os
import hardware_util
import email_util

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

sender = 'mburns7211@gmail.com'

root = Tk()

# Define size of screen
root.geometry("800x400")
root.config(bg='black')

count = 1
btn_shoot = None
btn_email = None
btn_home = None
inputtxt = None

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def isValid(email):
    return re.fullmatch(regex, email)

def update(c):
    global btn_email
    global btn_shoot
    global inputtxt
    global btn_home
    if c <= 3:
        print(c)
        main_screen.config(text=c)
        c+=1
        main_screen.after(1000, lambda: update(c))
    elif c == 4:
        print(c)
        main_screen.config(text="Fan On")
        hardware_util.turn_on_fan()
        c+=1
        main_screen.after(1000, lambda: update(c))
    elif c == 5:
        print(c)
        main_screen.config(text="Shooting")
        hardware_util.take_video()
        hardware_util.turn_off_fan()
        c += 1
        main_screen.after(1000, lambda: update(c))
    elif c == 6:
        print(c)
        main_screen.config(text="Enter Your Email")
        btn_shoot.pack_forget() if btn_shoot else None
        
        inputtxt = Text(root, width=20, height = 1)
        inputtxt.pack()
        btn_email = Button(root, background = 'black',foreground = 'white', text="Send", command = lambda: send_email(inputtxt.get(1.0, "end-1c")))
        btn_email.pack()

        # todo fix
        # import subprocess
        # import os
        # path = os.path.dirname(os.path.abspath(__file__))
        # path = os.path.join(path, 'keyboard-ssh.sh')
        # shellscript = subprocess.Popen([path], stdin=subprocess.PIPE)

        print("Bye! Now it's your responsibility to close new process :0")

# Todo tigger call to email button and submit then call update(7) and remove c+=1
    elif c == 7:
        print(c)
        btn_shoot.pack_forget() if btn_shoot else None
        btn_email.pack_forget() if btn_email else None
        inputtxt.pack_forget() if inputtxt else None
        btn_home.pack_forget() if btn_home else None
        btn_shoot_text = 'Shoot'
        btn_shoot = Button(root, background = 'black',foreground = 'white', text=btn_shoot_text, command = lambda: update(count))
        btn_shoot.pack()
        main_screen.config(text="Fan Video")
    elif c == 8:
        btn_shoot.pack_forget() if btn_shoot else None
        btn_email.pack_forget() if btn_email else None
        inputtxt.pack_forget() if inputtxt else None
        btn_home.pack_forget() if btn_home else None
        inputtxt.pack_forget() if inputtxt else None
        main_screen.config(text="Email Sent!")
        main_screen.after(5000, lambda: update(7))
    elif c == 9:
        btn_home.pack_forget() if btn_home else None
        main_screen.config(text="Invalid Email, Try Again")
        btn_home = Button(root, background = 'black',foreground = 'white', text="Go Home", command = lambda: update(7))
        btn_home.pack()

        
    
def send_email(addr):
    print(addr)
    if isValid(addr):
        receivers = [addr]

        message = """From: From Person <from@fromdomain.com>
        To: To Person <to@todomain.com>
        Subject: Test Video App

        This is a test e-mail message from the fan booth app.
        """

        try:
           # todo add attachment file
           email_util.send_email(to=addr) 
           print("Successfully sent email")
        except Exception as e:
           print(e)
           print("Error: unable to send email")
        
        update(8)
    else:
        update(9)
    
  
main_screen = Label(root, background = 'black',foreground = 'white', font = ('arial', 40, 'bold'))
main_screen.config(text="Fan Video")
main_screen.pack()

btn_shoot_text = 'Shoot'
btn_shoot = Button(root, background = 'black',foreground = 'white', text=btn_shoot_text, command = lambda: update(count))
btn_shoot.pack()

root.title('Fan Booth')
root.mainloop()
