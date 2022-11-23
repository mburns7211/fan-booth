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
import logging

logger = logging.Logger(__name__)

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def isValid(email):
    logger.info(f'Validating email: {email}')
    return re.fullmatch(regex, email)

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

c = 0

window = Tk()
# TODO revert
# window.attributes('-fullscreen',True)

window.title("The Branson Blower")

# using full screen and relx/rely
window.geometry("1360x768")

window.configure(bg = "#275199")

letsgo_img_file = PhotoImage(
        file=relative_to_assets("letsgo.png"))

max_height = window.winfo_screenheight()
max_width = window.winfo_screenwidth()

logger.info(f'Max Width: {max_width}\nMax Height: {max_height}')



canvas = Canvas(
    window,
    bg = "#275199",
    height = max_height,
    width = max_width,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

canvas.place(relx = 0, rely = 0)



# TODO generate image sizes

def generate_title_font_size(factor):
    global max_height

    font_ratio = factor / 760 
    font_in_pixels = font_ratio * max_height
    return int(font_in_pixels * -1)

canvas.create_rectangle(
    0.0,
    0.0,
    max_height,
    max_width,
    fill="#275199",
    outline="")


canvas.create_text(
    0.4*max_width,
    0.15*max_height,
    anchor="nw",
    text="THE\nBRANSON\nBLOWER",
    justify="center",
    fill="#FFFFFF",
    font=("JollyLodger", generate_title_font_size(85))
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
    0.07*max_width,
    0.13*max_height,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    .925*max_width,
    .125*max_height,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    .955*max_width,
    .855*max_height,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    .07*max_width,
    .88*max_height,
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
    width=.17*max_width,
    height=.0855*max_height
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
    max_height,
    max_width,
    fill="#275199",
    outline="")


    canvas.create_text(
        0.4*max_width,
        0.15*max_height,
        anchor="nw",
        text="THE\nBRANSON\nBLOWER",
        justify="center",
        fill="#FFFFFF",
        font=("JollyLodger", generate_title_font_size())
    )

    
    button_1.configure(command=lambda: ready(), image=button_image_1)
    button_1.place(
        relx=0.4,
        rely=0.8,
        width=.17*max_width,
        height=.0855*max_height
    )
    # TODO potentiall remove if unused and unecessary
    # image_1 = canvas.create_image(
    #     100.0,
    #     100.0,
    #     image=image_image_1
    # )

   
    # image_2 = canvas.create_image(
    #     1258,
    #     96,
    #     image=image_image_2
    # )

    
    # image_3 = canvas.create_image(
    #     1300.0,
    #     650.0,
    #     image=image_image_3
    # )

    # image_4 = canvas.create_image(
    #     100.0,
    #     675.0,
    #     image=image_image_4
    # )

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
        max_width,
        max_height,
        fill="#275199",
        outline="")

    canvas.create_text(
        .386 * max_width,
        .313 * max_height,
        anchor="nw",
        text="Email Sent!",
        fill="#FFFFFF",
        font=("JollyLodger", generate_title_font_size(105))
    )

    # TODO unused?
    # image_1 = canvas.create_image(
    #     680.0,
    #     600.0,
    #     image=image_image_1
    # )


    canvas.after(3000, lambda: home())


def alldone(fail=False):
    global window
    global canvas
    global button_1
    
    canvas.delete('all')

    canvas.create_rectangle(
        0.0,
        0.0,
        max_width,
        max_height,
        fill="#275199",
        outline="")

    # todo if fail, add button to home
    email_tx = "Input your best email and receive your video"
    if fail:
        email_tx = "Please enter a valid email"
        canvas.create_text(
	   .257 * max_width,
	   .253 * max_height,
	   anchor="nw",
	   text=email_tx,
	   fill="#FFFFFF",
	   font=("Inter", generate_title_font_size(50))
        )
    else:
        canvas.create_text(
            .074 * max_width,
	        .253 * max_height,
            anchor="nw",
            text=email_tx,
            fill="#FFFFFF",
            font=("Inter", generate_title_font_size(50))
        )


    # todo grab text from entry
    inputtxt = Text(canvas, bg='white', font=("Arial", generate_title_font_size(-30)), fg='black', height=1, width=25)
    inputtxt.place(
        relx=.294,
        rely=.362)

    p = subprocess.Popen(['matchbox-keyboard'])


    # on enter/return go to submit
    inputtxt.bind('<Return>', lambda _: send_email(inputtxt.get(1.0, "end-1c"), inputtxt, p))

    # block the following keys to have no action
    inputtxt.bind('<space>', lambda _:'break')
    
    button_1.configure(
        command = lambda: send_email(inputtxt.get(1.0, "end-1c"), inputtxt, p),
        image=button_image_submit
    )

    button_1.place(
        x=0.404 * max_width,
        y=.441 * max_height,
        width=.172 * max_width,
        height=.086 * max_height
    )


    canvas.create_text(
        .371 * max_width,
        .109 * max_height,
        anchor="nw",
        text="ALL DONE!",
        fill="#FFFFFF",
        font=("JollyLodger", generate_title_font_size(105))
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
