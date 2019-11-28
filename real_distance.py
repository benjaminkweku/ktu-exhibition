import RPi.GPIO as GPIO
from gpiozero import AngularServo,DistanceSensor,LED,Buzzer
import time,os                        
GPIO.setmode(GPIO.BCM)                
   
GPIO.setwarnings(False)


##first sensor for distance pins
TRIG = 15                                
ECHO = 14

##empty sensor for distance pins
TRIG_2 = 24                               
ECHO_2=23

##middle sensor for distance pins
TRIG_3= 8                               
ECHO_3= 25

##full sensor for distance pins
TRIG_1= 26                                
ECHO_1= 19    

print ("Distance measurement in progress")
GPIO.setup(17,GPIO.OUT)  # Sets up pin 11 to an output (instead of an input)
p = GPIO.PWM(17, 50)     # Sets up pin 11 as a PWM pin
p.start(0)               # Starts running PWM on the pin and sets it to 0

##first sensor for distance pins
GPIO.setup(TRIG,GPIO.OUT)                 
GPIO.setup(ECHO,GPIO.IN)

##emptysensor for distance pins
GPIO.setup(TRIG_1,GPIO.OUT)                 
GPIO.setup(ECHO_1,GPIO.IN)

##middle sensor for distance pins
GPIO.setup(TRIG_2,GPIO.OUT)                 
GPIO.setup(ECHO_2,GPIO.IN)

##full sensor for distance pins
GPIO.setup(TRIG_3,GPIO.OUT)                 
GPIO.setup(ECHO_3,GPIO.IN)

buzzer=Buzzer(2)
#Servo_motor=AngularServo(17,min_angle=0,max_angle=90)
led_red=LED(27)
led_amber=LED(22)
led_green=LED(10)
try:
    while True:
     
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
      
      
      
      GPIO.output(TRIG_1, False)                
      time.sleep(0.1)
      GPIO.output(TRIG_1, True)                 
      time.sleep(0.00001)                     
      GPIO.output(TRIG_1, False)
      while GPIO.input(ECHO_1)==0:               
        pulse_start_empty = time.time()
      while GPIO.input(ECHO_1)==1:               
        pulse_end_empty= time.time()                

      pulse_duration_empty= pulse_end_empty- pulse_start_empty
      distance_empty= pulse_duration_empty* 17150        
      distance_empty= round(distance_empty, 2)
      
      
      GPIO.output(TRIG_2, False)                
      time.sleep(0.1)
      GPIO.output(TRIG_2, True)                 
      time.sleep(0.00001)                     
      GPIO.output(TRIG_2, False)
      while GPIO.input(ECHO_2)==0:               
        pulse_start_middle= time.time()
      while GPIO.input(ECHO)==1:               
        pulse_end_middle= time.time()                

      pulse_duration_middle= pulse_end_middle - pulse_start_middle 
      distance_middle = pulse_duration_middle * 17150        
      distance_middle = round(distance_middle, 2)
      
      
      GPIO.output(TRIG_3, False)                
      time.sleep(0.1)           
      GPIO.output(TRIG_3, True)                 
      time.sleep(0.00001)                     
      GPIO.output(TRIG_3, False)
      while GPIO.input(ECHO_3)==0:               
        pulse_start_full = time.time()
      while GPIO.input(ECHO_3)==1:               
        pulse_end_full = time.time()                

      pulse_duration_full = pulse_end_full - pulse_start_full 
      distance_full = pulse_duration_full * 17150        
      distance_full = round(distance_full, 2)            

       
      
     
      
      
      


      if distance_full <=10 :
        buzzer.beep(0.2,0.2,1)
        led_green.on()
        led_amber.off()
        led_red.off()
        print ("Distance:",distance ,"cm"  )
        os.system('/home/pi/Desktop/dev/pushbullet.sh "Alert dustbin is full"')
      if distance_middle >=20 and distance_middle <=30 :
          led_green.off()
          led_red.off()
          led_amber.on()
          print("halve")
      if distance_empty ==50 :
          led_red.on()
          led_amber.off()
          led_green.off()
          print("empty")
          
      
         

      if distance<=20 :
        print("motion detected")
        led_red.on()
        led_amber.off()
#        Servo_motor.angle=0
        p.ChangeDutyCycle(1)
        
        time.sleep(12)
        #GPIO.output(2,GPIO.HIGH)
        
      elif distance>=20 :
        print("no motion detected")
        led_amber.on()
        led_red.off()
        #GPIO.output(2,GPIO.LOW)
#        Servo_motor.angle=90
        p.ChangeDutyCycle(13)
           
                            
            
      else:
          led_red.off()
          led_amber.off()
          led_green.off()
          print ("Out Of Range")                  

       
except:
    GPIO.cleanup()
