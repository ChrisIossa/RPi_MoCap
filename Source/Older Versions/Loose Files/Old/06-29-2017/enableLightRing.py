try:
    import RPi.GPIO as GPIO
except ModuleNotFoundError as e:
    print(e)

def enable():
    

    GPIO.setwarnings(False)


    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)

    GPIO.output(7, GPIO.HIGH)
