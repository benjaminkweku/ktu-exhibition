import RPi.GPIO as GPIO
from gpiozero import AngularServo,DistanceSensor,LED,Buzzer
import time,os
import picamera
#import sqlite3
#conn = sqlite3.connect('mydb.db')
#c = conn.cursor()

GPIO.setmode(GPIO.BCM)                
GPIO.setwarnings(False)

TRIG = 15                                
ECHO = 14                               

print ("Distance measurement in progress")

##pin setup for camera motor
GPIO.setup(17,GPIO.OUT)  # Sets up pin 11 to an output (instead of an input)
p = GPIO.PWM(17, 50)     # Sets up pin 11 as a PWM pin
p.start(0)               # Starts running PWM on the pin and sets it to 0




##pin setup for the ultra sonic sensor
GPIO.setup(TRIG,GPIO.OUT)                 
GPIO.setup(ECHO,GPIO.IN)


##pin setup for proximity sensor
GPIO.setup(4,GPIO.IN)
#pin setup for the buzzer
buzzer=Buzzer(2)
#Servo_motor=AngularServo(17,min_angle=0,max_angle=90)
led_red=LED(16)
led_amber=LED(19)
led_green=LED(26)
try:
    while True:
      sensor=GPIO.input(4)
      GPIO.output(TRIG, False)                
      print ("Waitng For Sensor To Settle")
      time.sleep(0.1)                            

      GPIO.output(TRIG, True)                 
      time.sleep(0.00001)                     
      GPIO.output(TRIG, False)                 

      while GPIO.input(ECHO)==0:               
        pulse_start = time.time()
      while GPIO.input(ECHO)==1:               
        pulse_end = time.time()                

      pulse_duration = pulse_end - pulse_start 
      distance = pulse_duration * 17150        
      distance = round(distance, 2)            

      if distance <=20 :
        led_amber.on()  
        buzzer.beep(0.2,0.2,1)
        led_green.off()
        with picamera.PiCamera() as camera:
            camera.resolution=(1024,648)
            camera.start_preview()
            time.sleep(0.01)
            #images=['image1.jpg','image2.jpg','image3.jpg','image4.jpg','image5.jpg']
            #for i in images:
            camera.capture('images.jpg')
                #c.executemany('INSERT INTO img VALUES (?,?)',image)
                #conn.commit()
                #conn.close()
                #for row in c.execute('SELECT * FROM img'):
                    #print(row)

                
        p.ChangeDutyCycle(1)
        time.sleep(6)
        p.ChangeDutyCycle(13)
        led_red.off()
        print("motion in range")
        print ("Distance:",distance ,"cm"  )
      # led_green.off()
          #led_amber.on()
          #p.ChangeDutyCycle(13)
          #print("motion out of range")
      
          
    
         

      elif sensor==0:
        print("bin full")
        led_red.on()
        led_amber.off()
        led_green.off()
        os.system('/home/pi/Desktop/dev/pushbullet.sh "alert dustbin full location:KTU campus"')
      
#        Servo_motor.angle=0
        
        #GPIO.output(2,GPIO.HIGH)
        
      elif sensor==1:
        print("more space")
        led_green.off()
        led_amber.on()
        led_red.off()
        #GPIO.output(2,GPIO.LOW)
#        Servo_motor.angle=90
        
           
                            
            
      else:
          led_red.off()
          led_amber.off()
          led_green.off()
          
          print ("Out Of Range")                  

       
except:
    GPIO.cleanup()
