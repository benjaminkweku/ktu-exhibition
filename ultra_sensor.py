import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Trigg=15
Echo=14

GPIO.setup(Trigg,GPIO.OUT)
GPIO.setup(Echo,GPIO.IN)

while True:
    GPIO.output(Trigg,False)
    time.sleep(0.1)
    GPIO.output(Trigg,True)
    time.sleep(0.00001)
    GPIO.output(Trigg,False)
    
    while GPIO.input(Echo)==0:
        start_time=time.time()
    while GPIO.input(Echo)==1:
        stop_time=time.time()
    
    duration=stop_time - start_time
    distance=duration * 17150
    distance=round(distance,2)
    
    if (distance >10 and distance<15):
        print("less than ten")
    elif distance <10:
        print("greater than ten")
    else:
        print("out of range")
        
        GPIO.cleanup()