import os

is_pi = True

try:
    import RPi.GPIO as GPIO
except Exception as e:
    is_pi = False
import time

def take_video():
    if is_pi:
        name = "vid_{}".format(str(time.time()))

        # Capture 10 seconds of raw video at 640x480 and 150kBps bit rate into a pivideo.h264 file:
        os.system(f'raspivid -t 10000 -w 640 -h 480 -fps 25 -b 1200000 -p 0,0,640,480 -o {name}.h264')
        # Wrap the raw video with an MP4 container:

        os.system(f'MP4Box -add {name}.h264 {name}.mp4')
        # Remove the source raw file, leaving the remaining pivideo.mp4 file to play
        os.system(f'rm {name}.h264')
        # raspivid -o video.h264 -t 10000 todo determine how to edit save path
        print("done")
    else:
        print("not on pi")
def detect_ir_dist():
    pass
def turn_on_fan():
    if is_pi:

        relay_pin = 11
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(relay_pin, GPIO.OUT)
        
        print("turning fan on")
        GPIO.output(relay_pin, GPIO.HIGH)
        print("done")
    else:
        print("not on pi")
def turn_off_fan():
    if is_pi:
        relay_pin = 11
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(relay_pin, GPIO.OUT)
        GPIO.output(relay_pin, GPIO.LOW)
    else:
        print("not on pi")

if __name__ == "__main__":
    take_video()
