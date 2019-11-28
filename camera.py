from picamera import PiCamera
from time import sleep

camera=PiCamera()
camera.led=False
camera.resolution=(640,480)
camera.framerate=5
camera.sharpness=0
