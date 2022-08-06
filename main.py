import RPi.GPIO as GPIO
import time


def main() -> None:
    GPIO.setmode(GPIO.board)

    m1_pins = (13, 15)

    GPIO.setup(m1_pins[0], GPIO.OUT)
    GPIO.setup(m1_pins[1], GPIO.OUT)

    while True:
        GPIO.output(m1_pins[0], GPIO.HIGH)
        GPIO.output(m1_pins[1], GPIO.LOW)
        time.sleep(1)
        GPIO.output(m1_pins[0], GPIO.LOW)
        GPIO.output(m1_pins[1], GPIO.HIGH)
        time.sleep(1)
        GPIO.output(m1_pins[0], GPIO.LOW)
        GPIO.output(m1_pins[1], GPIO.LOW)
        time.sleep(1)
