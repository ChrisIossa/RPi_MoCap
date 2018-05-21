import RPi.GPIO as GPIO

def disable():
    

    GPIO.setwarnings(False)


    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)

    GPIO.output(7, GPIO.LOW)
