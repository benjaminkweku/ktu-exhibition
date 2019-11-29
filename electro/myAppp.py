#from flask import Flask, render_template, redirect, url_for
from flask import Flask, render_template

# from gpiozero import LED

app=Flask(__name__)


@app.route('/',methods=["GET","POST"])
def light_on():
    if request.method=="POST":
            search_on=request.form['box1']
            if search_on=="light on" or "on" or "on light":
               text="The light is on"
               return redirect(url_for("https://169.254.203.24:5000/on"))
            elif search_on=="light off" or "off light" or "off":
                return redirect(url_for("https://192.168.43.224:5000/off"))
            else:
                results="invalid syntax.please try again"
                return results
  
    return render_template('index.html')

#step2
@app.route('/off')
def light_off():
    #elif search_on=="light off" or "off light" or "off":
                #return redirect(url_for("https://192.168.43.224:5000/off"))
            #else:
                #results="invalid syntax.please try again"
                #return results
    return 'Ghana'

#step3
@app.route('/foo')
def foo(name):
    return render_template('foo.html')



if __name__=='__main__':
    
    app.run(debug=True,host='0.0.0.0')