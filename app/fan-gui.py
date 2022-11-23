import os
from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess
from pathlib import Path
import re
import os
import glob
import hardware_util
import email_util

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def isValid(email):
    return re.fullmatch(regex, email)

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

c = 0

window = Tk()

window.title("The Branson Blower")

window.geometry("1360x768")
#window.attributes('-fullscreen',True)
window.configure(bg = "#275199")

letsgo_img_file = PhotoImage(
        file=relative_to_assets("letsgo.png"))

canvas = Canvas(
    window,
    bg = "#275199",
    height = 768,
    width = 1360,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

canvas.place(x = 0, y = 0)

canvas.create_rectangle(
    0.0,
    0.0,
    1360.0,
    768.0,
    fill="#275199",
    outline="")

canvas.create_text(
    535.0,
    100.0,
    anchor="nw",
    text="THE\nBRANSON\nBLOWER",
    justify="center",
    fill="#FFFFFF",
    font=("JollyLodger", 85 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_done.png"))

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))

button_image_submit = PhotoImage(
    file=relative_to_assets("submit.png"))

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    100.0,
    100.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    1258,
    96,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    1300.0,
    650.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    100.0,
    675.0,
    image=image_image_4
)

button_1 = Button(
    window,
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: ready(),
    relief="flat"
    )
button_1.place(
    relx=0.4,
    rely=0.8,
    width=234.0,
    height=65.0
)

def home():
    global window
    global canvas
    global image_image_1
    global image_image_2
    global image_image_3
    global image_image_4
    global button_1
    
    print("in home")


    canvas.delete('all')
    canvas.place(x = 0, y = 0)

    canvas.create_rectangle(
        0.0,
        0.0,
        1360.0,
        768.0,
        fill="#275199",
        outline="")

    canvas.create_text(
        535.0,
        100.0,
        anchor="nw",
        text="THE\nBRANSON\nBLOWER",
        justify="center",
        fill="#FFFFFF",
        font=("JollyLodger", 85 * -1)
    )

    
    button_1.configure(command=lambda: ready(), image=button_image_1)
    button_1.place(
        relx=0.4,
        rely=0.8,
        width=234.0,
        height=65.0
    )

    image_1 = canvas.create_image(
        100.0,
        100.0,
        image=image_image_1
    )

   
    image_2 = canvas.create_image(
        1258,
        96,
        image=image_image_2
    )

    
    image_3 = canvas.create_image(
        1300.0,
        650.0,
        image=image_image_3
    )

    image_4 = canvas.create_image(
        100.0,
        675.0,
        image=image_image_4
    )

def emailsent():
    global window
    global canvas
    global button_1
    global image_image_1

    button_1.place_forget()

    canvas.delete('all')

    canvas.create_rectangle(
        0.0,
        0.0,
        1360.0,
        768.0,
        fill="#275199",
        outline="")

    canvas.create_text(
        525.0,
        238.0,
        anchor="nw",
        text="Email Sent!",
        fill="#FFFFFF",
        font=("JollyLodger", 105 * -1)
    )

    image_1 = canvas.create_image(
        680.0,
        600.0,
        image=image_image_1
    )


    canvas.after(3000, lambda: home())


def alldone(fail=False):
    global window
    global canvas
    global button_1
    
    canvas.delete('all')

    canvas.create_rectangle(
        0.0,
        0.0,
        1360.0,
        768.0,
        fill="#275199",
        outline="")

    # todo if fail, add button to home
    email_tx = "Input your best email and receive your video"
    if fail:
        email_tx = "Please enter a valid email"
        canvas.create_text(
	   350,
	   192,
	   anchor="nw",
	   text=email_tx,
	   fill="#FFFFFF",
	   font=("Inter", 50 * -1)
        )
    else:
        canvas.create_text(
	   100,
	   192,
	   anchor="nw",
	   text=email_tx,
	   fill="#FFFFFF",
	   font=("Inter", 50 * -1)
        )


    # todo grab text from entry
    inputtxt = Text(canvas, bg='white', font=("Arial", 30), fg='black', height=1, width=25)
    inputtxt.place(
        x=400.0,
        y=275.0)

    p = subprocess.Popen(['matchbox-keyboard'])


    # on enter/return go to submit
    inputtxt.bind('<Return>', lambda: send_email(inputtxt.get(1.0, "end-1c"), inputtxt, p))

    # block the following keys to have no action
    inputtxt.bind('<space>', lambda _:'break')
    
    button_1.configure(
        command = lambda: send_email(inputtxt.get(1.0, "end-1c"), inputtxt, p),
        image=button_image_submit
    )

    button_1.place(
        x=550.0,
        y=335.0,
        width=234.0,
        height=65.0
    )


    canvas.create_text(
        505.0,
        83.0,
        anchor="nw",
        text="ALL DONE!",
        fill="#FFFFFF",
        font=("JollyLodger", 105 * -1)
    )
    

def letsgo():
    # todo trigger this to stay open for 10 secs while camera is filming
    global letsgo_img_file
    global window
    global canvas
    global letsgo_in

    canvas.delete('all')
    canvas.configure(bg="#48D34E")

    letsgo_img = canvas.create_image(
        680.0,
        330.0,
        image=letsgo_img_file
    )

    canvas.create_text(
        590.0,
        225.0,
        anchor="nw",
        text="LET’S \nGO!!!",
        fill="#000000",
        font=("JollyLodger", 120 * -1)
    )
    canvas.update()

    hardware_util.turn_on_fan()
    hardware_util.take_video()
    hardware_util.turn_off_fan()
    
    canvas.after(0, lambda: alldone())


def one():
    print("1")
    global window
    global canvas

    canvas.delete('all')
    canvas.configure(bg='#EAD943')
    canvas.create_text(
        640,
        150,
        anchor="nw",
        text="1",
        fill="#FFFFFF",
        font=("JollyLodger", 220 * -1)
    )
    canvas.after(1000, lambda: letsgo())

def two():
    print("2")
    global window
    global canvas

    canvas.delete('all')
    canvas.configure(bg='#E9A82B')
    canvas.create_text(
        640,
        150,
        anchor="nw",
        text="2",
        fill="#FFFFFF",
        font=("JollyLodger", 220 * -1)
    )

    canvas.after(1000, lambda: one())

def three():
    print("3")
    global window
    global canvas
    

    canvas.delete('all')
    canvas.configure(bg='#D34848')
    canvas.create_text(
        640,
        150,
        anchor="nw",
        text="3",
        fill="#FFFFFF",
        font=("JollyLodger", 220 * -1)
    )
    canvas.after(1000, lambda: two())

def ready():
    button_1.place_forget()
    print("start clicked")
    global window
    global canvas

    canvas.delete('all')
    canvas.create_text(
        500.0,
        200.0,
        anchor="nw",
        text="GET READY...",
        fill="#FFFFFF",
        font=("JollyLodger", 105 * -1)
    )

    canvas.after(1500, lambda: three())  

def send_email(addr, inputtxt, p):
    global canvas
    global button_1
    button_1.place_forget()

    canvas.delete("all")
    canvas.create_rectangle(
        0.0,
        0.0,
        1360.0,
        768.0,
        fill="#275199",
        outline="")
    inputtxt.place_forget()
    p.kill()
    list_of_files = glob.glob('./*.mp4') # * means all if need specific format then *.mp4
    latest_file = max(list_of_files, key=os.path.getctime)
    print(latest_file)
    print(type(latest_file))
    print(addr)
    if isValid(addr):
        receivers = [addr]

        try:
           # todo add attachment file
           email_util.send_email(to=addr, attachment=latest_file) 
           print("Successfully sent email")
           os.remove(latest_file)
           print("file deleted")
        except Exception as e:
           print(e)
           print("Error: unable to send email")
        
        canvas.after(1000, lambda: emailsent())
    else:
        canvas.after(1500, lambda: alldone(fail=True))

window.resizable(False, False)
window.mainloop()


#if __name__ == "__main__":
#   alldone()
