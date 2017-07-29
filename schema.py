import RPi.GPIO as GPIO
import time
import schedule
from datetime import datetime


def write_log():
    f1 = open('waterlog.txt', 'a')
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
    duration = [2, 2, 2, 2, 2, 2, 2]
    mytimes = ['08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '23:00']

    for i in range(len(duration)):
        schedule.every().day.at(mytimes[i]).do(job, i)


    # schedule.every().day.at(mytimes[0]).do(job0)
    # schedule.every().day.at(mytimes[1]).do(job1)
    # schedule.every().day.at(mytimes[2]).do(job2)

    while True:
        schedule.run_pending()
        time.sleep(1)
