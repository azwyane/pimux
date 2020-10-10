from flask import Flask,Response
from pimux import function
from pimux import Sensors
import subprocess

app=Flask(__name__)
f=function.misc()
s=Sensors.sensor()

@app.route('/')
def welcome():
    return '''
    <strong> Welcome to IOT</strong>
    <hr>
    Enter the url methods on your browser:
    <ul>
 <li>/vibrate</li>
    <li>/call/{phone number}</li>
<li>/torch/{on/off}</li>
<li>/brightness/{0-255}</li>
<li>/listsensors</li>
<li>/battery</li>
    </ul>
    '''
@app.route('/battery')
def battery():
    out=f.battery()
    return f'''
    <strong>Battery status</strong>
    <br>
    {out}
    '''

@app.route('/vibrate')
def vibrate():
    out=f.vibrate()
    return "Vibrating your phone"

@app.route('/call/<int:pnum>')
def call(pnum):
    out=f.telephonycall(pnum)
    return f"Making call to {pnum} for you"


@app.route('/torch/<string:state>')
def torch(state):
    if state=="on":
        out=f.torch(True)
        return "The torch on your phone is turned ON"
    elif state=="off":
        out=f.torch(False)
        return "The torch on your phone is turned OFF"


@app.route('/listsensors')
def listS():
    out=s.listSensor()
    return f'''
    The sensors available on your device are:
    {out}
    '''
@app.route('/brightness/<int:bval>')
def bright(bval):
    out=f.brightness(bval)
    return f'''
    Setting your device brightness to {bval}
    <hr>
    DONE
    '''

'''
#TODO:

from time import sleep

@app.route('/sensor/<string:sName>')
def sensordata(sName):
    def display_sensor(sensorN):
        proc = subprocess.Popen(
                s.specificSensors(sensorN),
                shell=True,
                stdout=subprocess.PIPE
                )

        for line in iter(proc.stdout.readline):
            sleep(1)
            yield line.rstrip() 

    return Response(s.specificSensors(sName),mimetype='text/html')  

'''


if __name__=="__main__":
    app.run(debug=False)
