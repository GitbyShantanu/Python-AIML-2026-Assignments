# WAP that creates a new log file after every 10 minutes.

# The filename should contain current date and time. 
#   Example: MarvellousLog_25_07_2026_16_30_00.txt

# The file should contain: 
#   Log file created successfully
#   Creation time: 25-07-2026 04:30:00 PM 

import schedule
import time
from datetime import datetime


def createLogFile():
    timestamp = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    fileName = f"MarvellousLog_{timestamp}.txt"
    
    fobj = open(fileName, "w")
    fobj.write("Log file created successfully\n")
    fobj.write("Creation time: " + datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))
    fobj.close()
    
    print("Log file created successfully: ", fileName)


def main():
    schedule.every(10).minutes.do(createLogFile)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()