import RPi.GPIO as GPIO
import time


def main() -> None:
    GPIO.setmode(GPIO.BOARD)

    m1_pins = (13, 15)

    GPIO.setup(m1_pins[0], GPIO.OUT)
    GPIO.setup(m1_pins[1], GPIO.OUT)

    for i in range(3):
        GPIO.output(m1_pins[0], GPIO.HIGH)
        GPIO.output(m1_pins[1], GPIO.LOW)
        time.sleep(1)
        GPIO.output(m1_pins[0], GPIO.LOW)
        GPIO.output(m1_pins[1], GPIO.HIGH)
        time.sleep(1)
        GPIO.output(m1_pins[0], GPIO.LOW)
        GPIO.output(m1_pins[1], GPIO.LOW)
        time.sleep(1)


if __name__ == "__main__":
    main()
    GPIO.cleanup()
    print("Done")
    exit(0)
    pass
