import RPi.GPIO as GPIO
import pyowm
import schedule
import time
import datetime
import waterformula


def write_log(duration):
    f1 = open('/home/pi/dev/ElectroGarden/waterlog.txt', 'a')
    f1.write('%is @ %s\n' % (duration, datetime.datetime.now().strftime('%Y%m%d-%H:%M')))
    f1.close()


def calc_E():
    owm = pyowm.OWM('e95b492d3c977db6b58b95f097683036')
    w = owm.weather_at_coords(59.914009, 16.321638).get_weather()

    T = w.get_temperature(unit='celsius')['temp']  # Temperature
    c = w.get_clouds()/100  # cloud coverage
    h = w.get_humidity()/100  # humidity
    E = waterformula.calc(T, c, h)
    return E


def toggle_valve():
    duration = calc_E()
    write_log(duration)

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    GPIO.output(12, 0)  # new relay is on when 0
    time.sleep(duration)
    GPIO.output(12, 1)   # new relay is off when 1
    GPIO.cleanup(12)


if __name__ == '__main__':
    mytimes = ['00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00']

    for i in range(8):
        schedule.every().day.at(mytimes[i]).do(toggle_valve)

    while True:
        schedule.run_pending()
        time.sleep(1)
