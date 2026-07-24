# WAP that prints Jay Ganesh every 2 seconds 

import schedule
import time

def Display():
    print("Jay Ganesh...")


def main():
    schedule.every(2).seconds.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(0.5)


if __name__ == "__main__":
    main()