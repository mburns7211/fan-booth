import os
import RPi.GPIO as GPIO
import time

def take_video():
    # Capture 10 seconds of raw video at 640x480 and 150kBps bit rate into a pivideo.h264 file:
    os.system('raspivid -t 10000 -w 640 -h 480 -fps 25 -b 1200000 -p 0,0,640,480 -o pivideo.h264')
    # Wrap the raw video with an MP4 container:
    os.system('MP4Box -add pivideo.h264 video.mp4')
    # Remove the source raw file, leaving the remaining pivideo.mp4 file to play
    os.system('rm pivideo.h264')
    # raspivid -o video.h264 -t 10000 todo determine how to edit save path
    print("done")
def detect_ir_dist():
    pass
def turn_on_fan():
    relay_pin = 11
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(relay_pin, GPIO.OUT)
    
    print("turning fan on")
    GPIO.output(relay_pin, GPIO.HIGH)
    print("done")
def turn_off_fan():
    relay_pin = 11
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(relay_pin, GPIO.OUT)
    GPIO.output(relay_pin, GPIO.LOW)

if __name__ == "__main__":
    take_video()
