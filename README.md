# Mikro 
Pojects intented for deployment onto embedded systems. 
Some of these have completely different topics, platforms and languages. 
But they are related by being meant for running on IOT devices. 

# Arduino 
## IOT/ - Joystick - EEPromReader
** Playing with using the Arduino has the A/D converter 
as well as handle the logic for converting motion (and a
button click) on a joystick to either UP, DOWN, LEFT, RIGHT
and CLICK. 

Different motions create different LEDs to light up. These LEDs
are also connected in parallel to GPIO ports on the Raspberry PI. 
** TODO: Write something on the RPi for handling the input from
the joystick, and see if this real time input can be implemented in
games/programs as a source of user input! 

[Joystick Usage](https://drive.google.com/file/d/1FGiaLC9TFn_gdNJQfmulh9PAbnwjkbFd/view)

# Raspberry Pi 

## hip.py 
I want to create light weight Network Monitoring software to make 
the Pi a useful sort of ad hoc/automated Incident Detection System. 

## 3mergent.py
I need to work on code for sending and receiving commands/data to 
and from the Raspberry Pi wirelessly, for it to be used in any kind of
autonomous way. This is the program where I try and work on that 
communication protocol. 

# Crypto
IOT devices are notorious for their insecurity. Are there any easy ways to harden programs? 
I'm going to tinker with crypto libraries and see if I can establish some simple ways to implement
better security into IOT projects 

## Block Ciphers 
The first cipher I'm working with is AES, using CBC. It's not a great selection, but it was easy to 
put something very simple together. It will be instructive to attack this cipher later on, and see
where the trade offs for simplicity may breakdown! 

![AES_CBC](https://raw.githubusercontent.com/TylersDurden/mikro/master/AES_CBC.png)

One problem is that the message needs to be padded to make it a multiple of the cipher's block size.
The way I handled this was straightforward, but could end up compromising security in the end. I chose
to simply add 'x' characters to the end of the message, filling up until the message is an even multiple of
the block size. 

