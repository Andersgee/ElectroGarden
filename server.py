import os.path
import cherrypy
import RPi.GPIO as GPIO
import time
import htmlsnippets as hs
import datetime
import pyowm
import waterformula


def querydate(d, h):
    q = d + datetime.timedelta(hours=h+(3-d.hour % 3))
    q = q.replace(minute=0, second=0, microsecond=0)
    return q


def write_log():
    f1 = open('/home/pi/dev/ElectroGarden/waterlog.txt', 'a')
    f1.write('%is @ %s MANUAL\n' % (duration, datetime.datetime.now().strftime('%Y%m%d-%H:%M')))
    f1.close()


class HomePage:
    def __init__(self):
        self.valve1 = PinObject(12)

    @cherrypy.expose
    def index(self):
        yield hs.start_html()

        yield hs.start_card()
        yield hs.start_table()

        owm = pyowm.OWM('e95b492d3c977db6b58b95f097683036')
        f = owm.three_hours_forecast_at_coords(59.914009, 16.321638)
        d = datetime.datetime.now()
        for n in range(9):
            q = querydate(d, 3*n)
            w = f.get_weather_at(q)
            T = w.get_temperature(unit='celsius')['temp']  # Temperature
            c = w.get_clouds()/100  # cloud coverage
            h = w.get_humidity()/100  # humidity
            E = waterformula.calc(T, c, h)
            # E = max(0, T - 2*c - 3*h)  # Effective water evaporation.. ish?
            yield hs.tablerow(E, q.strftime('%H:00 %a'), T, c, h)

        yield hs.end_table()
        yield hs.end_card()

        yield hs.start_card2()
        yield hs.myswitch(name='s1', action='toggle_valve1', label=switchlabel, enabled=1, checked=self.valve1.on)
        yield hs.end_card()

        yield hs.end_html()

    @cherrypy.expose
    def toggle_valve1(self):
        write_log()
        self.valve1.toggle()
        time.sleep(duration)
        self.valve1.toggle()
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
            GPIO.output(self._pin, 1)   # new relay is off when 1
            GPIO.cleanup(self._pin)
            self._on = 0
        else:
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(self._pin, GPIO.OUT)
            GPIO.output(self._pin, 0)  # new relay is on when 0
            self._on = 1


if __name__ == '__main__':
    duration = 5
    switchlabel = '<h6><b>Water now (%i ml)</b></h6>' % (duration*14)
    config_path = '/home/pi/dev/ElectroGarden/myconf.conf'
    cherrypy.quickstart(HomePage(), config=config_path)
