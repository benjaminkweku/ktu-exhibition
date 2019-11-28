from gpiozero import AngularServo
from time import sleep
servo_motor=AngularServo(3,min_angle=0,max_angle=90)

while(True):
    servo_motor.angle=45
    sleep(2)
    servo_motor.angle=0
    sleep(2)
    
   