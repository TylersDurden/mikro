import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)
GPIO.setup(17, GPIO.IN)
GPIO.setup(5, GPIO.IN)
GPIO.setup(23, GPIO.IN)
try:
    while True:
        bit1 = GPIO.input(4)
        bit2 = GPIO.input(17)
        bit3 = GPIO.input(5)
        bit4 = GPIO.input(23)
        print "|"+str(bit1)+"|"+str(bit2)+"|"+str(bit3)+"|"+str(bit4)+"|"
except KeyboardInterrupt:
    GPIO.cleanup()
    exit(0)
#EOF
