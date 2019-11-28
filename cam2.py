import time
import picamera
with picamera.PiCamera() as camera:
    camera.resolution=(1024,648)
    camera.start_preview()
    time.sleep(5)
    camera.capture('image4.jpg')
    
