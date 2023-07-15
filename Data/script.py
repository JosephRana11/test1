import schedule
import time

def do_nothing():
    print("Hello world")

schedule.every(5).seconds.do(do_nothing)

while True :
    schedule.run_pending()
    time.sleep(1)