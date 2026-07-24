# WAP that prints current time and date after every 1 minutes

import schedule
import datetime
import time


def Display():
    now = datetime.datetime.now()
    print(f"Current Date and Time: {now.strftime("%d-%m-%Y %I:%M:%S %p")}")

def main():
    schedule.every(1).minutes.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)
        

if __name__ == "__main__":
    main()