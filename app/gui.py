
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer
import tkinter as tk
import pyglet, os
from tkinter import *

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import time

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

c = 0

window = Tk()

window.title("The Branson Blower")

window.geometry("800x400")
window.configure(bg = "#275199")

letsgo_img_file = PhotoImage(
        file=relative_to_assets("letsgo.png"))

canvas = Canvas(
    window,
    bg = "#275199",
    height = 400,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

canvas.place(x = 0, y = 0)

canvas.create_rectangle(
    0.0,
    0.0,
    800.0,
    400.0,
    fill="#275199",
    outline="")

canvas.create_text(
    286.0,
    10.0,
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

button_1 = Button(
    window,
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: ready(),
    relief="flat"
)
button_1.place(
    x=286.0,
    y=325.0,
    width=234.0,
    height=65.0
)

inputtxt = None

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    86.0,
    61.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    740,
    50,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    750.0,
    350.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    50.0,
    375.0,
    image=image_image_4
)

def home():
    global window
    global canvas
    global button_1
    global image_image_1
    global image_image_2
    global image_image_3
    global image_image_4


    canvas.delete('all')
    canvas.place(x = 0, y = 0)

    canvas.create_rectangle(
        0.0,
        0.0,
        800.0,
        400.0,
        fill="#275199",
        outline="")

    canvas.create_text(
        286.0,
        10.0,
        anchor="nw",
        text="THE\nBRANSON\nBLOWER",
        justify="center",
        fill="#FFFFFF",
        font=("JollyLodger", 85 * -1)
    )

    
    button_1.configure(command=lambda: ready(), image=button_image_1)
    button_1.place(
        x=286.0,
        y=325.0,
        width=234.0,
        height=65.0
    )

    image_1 = canvas.create_image(
        86.0,
        61.0,
        image=image_image_1
    )

   
    image_2 = canvas.create_image(
        740,
        50,
        image=image_image_2
    )

    
    image_3 = canvas.create_image(
        750.0,
        350.0,
        image=image_image_3
    )

    image_4 = canvas.create_image(
        50.0,
        375.0,
        image=image_image_4
    )

def emailsent():
    global window
    global canvas
    global button_1
    global image_image_1
    global inputtxt

    inputtxt.place_forget()

    button_1.place_forget()

    canvas.delete('all')

    canvas.create_rectangle(
        0.0,
        0.0,
        800.0,
        400.0,
        fill="#275199",
        outline="")

    canvas.create_text(
        212.0,
        124.0,
        anchor="nw",
        text="Email Sent!",
        fill="#FFFFFF",
        font=("JollyLodger", 105 * -1)
    )

    image_1 = canvas.create_image(
        400.0,
        290.0,
        image=image_image_1
    )


    canvas.after(3000, lambda: home())


def alldone():
    global window
    global canvas
    global button_1
    global inputtxt

    canvas.delete('all')

    canvas.create_rectangle(
        0.0,
        0.0,
        800.0,
        400.0,
        fill="#275199",
        outline="")

    canvas.create_text(
        200,
        200,
        anchor="nw",
        text="Input your best email and receive your video",
        fill="#FFFFFF",
        font=("Inter", 24 * -1)
    )


    # todo grab text from entry
    inputtxt = Text(canvas, bg='white', font=("Arial", 20), fg='black', height=2)
    inputtxt.place(x=211.5,
        y=260.0,
        width=376.0,
        height=30.0)

    button_1.configure(
        command=lambda: emailsent(),
        image=button_image_submit)

    button_1.place(
        x=286.0,
        y=325.0,
        width=234.0,
        height=65.0
    )


    canvas.create_text(
        238.0,
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
        400.0,
        175.0,
        image=letsgo_img_file
    )

    canvas.create_text(
        300.0,
        75.0,
        anchor="nw",
        text="LET’S \nGO!!!",
        fill="#000000",
        font=("JollyLodger", 120 * -1)
    )

    # todo change to 10000
    canvas.after(1000, lambda: alldone())


def one():
    print("1")
    global window
    global canvas

    canvas.delete('all')
    canvas.configure(bg='#EAD943')
    canvas.create_text(
        375,
        75,
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
        375,
        75,
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
        375,
        75,
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
        230.0,
        150.0,
        anchor="nw",
        text="GET READY...",
        fill="#FFFFFF",
        font=("JollyLodger", 105 * -1)
    )

    canvas.after(1500, lambda: three())  


window.resizable(False, False)
window.mainloop()
