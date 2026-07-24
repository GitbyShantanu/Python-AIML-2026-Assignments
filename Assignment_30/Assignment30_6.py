# Write a script that schedules the following tasks:
# print Lunch Time! every day at 1:00 PM.
# print Wrap up work every day at 6:00 PM.
# Both fn should be handled by seperate functions. 

import schedule
import time
import datetime


def lunchtimeDisplay():
    print("Lunch Time!")

def wrapUpDisplay():
    print("Wrap Up work")


def main():

    schedule.every(1).day.at("01:00").do(lunchtimeDisplay)
    schedule.every(1).day.at("06:00").do(wrapUpDisplay)

    while True:
        schedule.run_pending()
        time.sleep(100)
        

if __name__ == "__main__":
    main()