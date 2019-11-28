from flask import Flask ,render_template
import time
import picamera as camera


app=Flask(__name__)
@app.route('/take_a_picture')
def camera():
    with picamera.piCamera as camera:
        camera.resolution(1024,648)
        camera.start_preview()
        time.sleep(2)
        camera.capture('image.png')
        

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)
