'''
Python script to disable power from GPIO board to light ring
'''

try:
    import RPi.GPIO as GPIO
except ModuleNotFoundError as e:
    print(e)

def disable():
    # Disable warnings 
    GPIO.setwarnings(False)

    GPIO.setmode(GPIO.BOARD)

    # Power channel 7 -> 7th header on board
    GPIO.setup(7, GPIO.OUT)

    # Setting output to 'LOW' turns off
    GPIO.output(7, GPIO.LOW)

disable()
