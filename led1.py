from gpiozero import LED,Buzzer
from time import sleep

led_blue=LED(20)
buzzer=Buzzer(2)

while(True):
    led_blue.on()
    buzzer.beep(0.2,0.2,2)
    sleep(3)
    led_blue.off()
    sleep(3)
    