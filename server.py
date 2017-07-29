import os.path
import cherrypy
import RPi.GPIO as GPIO
import time
import htmlsnippets as hs
from datetime import datetime


class HomePage:
    def __init__(self):
        self.valve1 = PinObject(29)

    @cherrypy.expose
    def index(self):
        yield hs.myheader()

        yield '<div class="row">'
        yield hs.mygreeting(getlog())

        yield hs.begincard()
        # yield hs.myswitch(name='s1', action='toggle_valve1', label='<b>Valve1</b>', enabled=1, checked=self.valve1.on)
        yield hs.myswitch(name='s1', action='toggle_valve1', label=switchlabel, enabled=1, checked=self.valve1.on)
        yield hs.endcard()

        yield '</div>'

        yield hs.myfooter()

    @cherrypy.expose
    def toggle_valve1(self):
        self.valve1.toggle()
        time.sleep(duration)
        self.valve1.toggle()
        write_log()
        raise cherrypy.HTTPRedirect("./")


class PinObject(object):
    def __init__(self, pin):
        self._on = 0
        self._pin = pin

    @property
    def on(self):
        return self._on

    def toggle(self):
        if self._on:
            GPIO.output(self._pin, 0)
            self._on = 0
            GPIO.cleanup(self._pin)
        else:
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(self._pin, GPIO.OUT)
            GPIO.output(self._pin, 1)
            self._on = 1


def write_log():
    f1 = open('waterlog.txt', 'a')
    f1.write(datetime.now().strftime('%H:%M') + ' (e)<br>')
    f1.close()


def getlog():
    f1 = open('waterlog.txt', "r")
    oneline = f1.read()[-13*4:]
    f1.close()
    text = '<p>(a)uto water at:<br>08:30<br>12:00<br>20:30</p>history:<br>' + oneline
    return text

if __name__ == '__main__':
    duration = 2
    switchlabel = '<b>(e)xtra water now'
    config_path = '/home/pi/dev/ElectroGarden/myconf.conf'
    cherrypy.quickstart(HomePage(), config=config_path)
