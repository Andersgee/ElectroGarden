import RPi.GPIO as GPIO
import time
import schedule
import numpy as np
from datetime import datetime


def write_log():
    f1 = open('/home/pi/dev/ElectroGarden/waterlog.txt', 'a')
    f1.write(datetime.now().strftime('%H:%M') + ' (a)<br>')
    f1.close()


def job(i):
    print('job: %i' % (i))
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pinnr, GPIO.OUT)
    GPIO.output(pinnr, 1)
    time.sleep(duration[i])
    GPIO.output(pinnr, 0)
    GPIO.cleanup(pinnr)
    write_log()

if __name__ == '__main__':
    pinnr = 29
    # [ml/s] (in each of the 10 pots):
    flowrate = 15.5
    # how many ml to water at each time:
    ml = np.array([200, 200, 200, 200])
    # when to water:
    mytimes = ['08:30', '12:00', '20:30', '15:50']

    duration = ml/flowrate  # [ml]/[ml/s]=[s]

    for i in range(len(duration)):
        schedule.every().day.at(mytimes[i]).do(job, i)

    while True:
        schedule.run_pending()
        time.sleep(1)
