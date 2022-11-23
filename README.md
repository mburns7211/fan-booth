# fan-booth
### *by Matt Burns*

## Goal
Design an application that can Display a camera feed the intiate a fan to turn on, video to start, then email to be sent to user provided input

## Tools
* Python
* Tkinter
* Conda
* SMTP
* Matchbox-KeyBoard

## Hardware Components
* Raspberry Pi v4
* Relay
* Raspberry Pi Camera
* Raspberry Pi Touchscreen
* LEDs

## Setup
1. Connect components
    * Plug keyboard in to PI (for setup only, optional for running fan booth)
    * Connect camera module to raspberry Pi (ribbon cable on camera to camera port on pi)
    * Connect touchscreen to pi (ribbon cable to port on pi, ground an 5V jumper cables touchscreen to pi)
    * Connect wires to pins 11 and any ground pin on pi then attach to terminals for relay
    * Plug LEDs into always on outlet on relay
    * Connect Fan to sometimes on outlet on relay
    * Plug relay and raspberry pi power cables into wall power
2. Raspberry pi should boot up.
3. Connect to wifi by following the following sub steps:
    1. Click the raspberry logo in the top left
    2. click accessories then keyboard.  this will launch a keyboard
    3. In the top right of the main desktop (not the keyboard window), click the wifi logo and select the correct network.  Using the keyboard, enter the password.
4.  Using the touch screen open Desktop->Development->fan-booth->app.  You can then double click fan booth and the Pi IDE will launch.  Hitting the play button will launch the app. 
(You can also start the app by simply opening the terminal and typing 'cd ~/fan-booth' and then 'python app/fan-booth.py'
4. This should launch the fan booth app. The program is now ready for fan videos.  To turn off simply unplug from power.

## Debug Mode
* Setup port forwarding following https://forums.raspberrypi.com/viewtopic.php?t=20826
1. To enter debug mode, double click the shortcut on desktop labelelled 'debug'.
2. When the black window pops up, simply copy the last values labelled 'IP address'
3. Send this to Matt or use it as the IP address in the following command
```ssh pi@IPADDRESS```
and using the password raspberry
