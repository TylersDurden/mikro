import time, sys, os, RPi.GPIO as GPIO


class Motion:
    Vx = 0
    Vy = 0
    TAP = False

    def __index__(self, A1, A2, A3):
        self.Vx = A1
        self.Vy = A2
        self.TAP = A3


def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(27, GPIO.IN)
    GPIO.setup(26, GPIO.IN)
    GPIO.setup(12, GPIO.IN)
    nsteps = 100000
    step = 0
    while step < nsteps:
        A = GPIO.input(27)
        B = GPIO.input(26)
        C = GPIO.input(12)
        step += 1
        time.sleep(0.5)
    GPIO.cleanup()


if __name__ == '__main__':
    main()
