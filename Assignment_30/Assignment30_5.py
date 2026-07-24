# Schedule a task that executes every 5 minutes.
# The task should write the current date and time into a file named: Marvellous.txt
# New entries should be appended instead of removing previus entries.

import schedule
import time
import datetime


def logDatetime(fname):
    fobj = open(fname, "a")

    timestamp = datetime.datetime.now()
    timestamp = timestamp.strftime("%d-%m-%y %I:%M:%S %p")
    print(timestamp)

    fobj.write(str(timestamp) + "\n")
    fobj.close()

def main():
    fname = "Marvellous.txt"
    schedule.every(5).minutes.do(logDatetime, fname)
    logDatetime(fname)

    while True:
        schedule.run_pending()
        time.sleep(10)
        

if __name__ == "__main__":
    main()