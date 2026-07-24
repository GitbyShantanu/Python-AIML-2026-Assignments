# WAP that reads and displays contents of a specified text file every minute. 
# Handle the following conditions: 
#  1. File does not exist 
#  2. File is empty 
#  3. Permission is denied
#  4. File cannot be opened

import schedule
import schedule
from datetime import datetime
import time
import os

def displayFile(fileName = "CopyLog.txt"):
    if os.path.exists(fileName) == False:
        print("File does not exist")
        return

    if os.path.getsize(fileName) == 0:
        print("File is empty")
        return 

    if os.access(fileName, os.R_OK) == False:
        print("Permission denied")
        return

    if os.access(fileName, os.W_OK) == False:
        print("File cannot be opened")
        return

    fobj = open(fileName, "r")
    content = fobj.read()
    print(content)
    fobj.close()
    

def main():
    fileName = input("Enter file name: ")
    
    # displayFile(fileName) 
    schedule.every(1).minute.do(displayFile, fileName)

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Program terminated by user")
    
if __name__ == "__main__":
    main()

    