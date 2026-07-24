# WAP that monitors size of specifies file every 30 seconds. 
# Write the following details into FileSizeLog.txt
#  1. File Path
#  2. File Size in bytes
#  3. Date & Time 
# Handle the situation where the file does not exist

import schedule
from datetime import datetime
import time
import os

def monitorFileSize(filename):
    size = os.path.getsize(filename)
    
    now = datetime.now()
    fobj = open("FileSizeLog.txt", "a")
    
    fobj.write("=" * 70 + "\n")
    fobj.write(f"File Path: {os.path.relpath(filename)}\n")
    fobj.write(f"File Size: {size} bytes\n")
    fobj.write(f"Date & Time: {now}\n")
    fobj.write("=" * 70 + "\n")

    fobj.close() 
    print("File size logged successfully...") 

def main():
    filename = input("Enter file name: ")
    
    if os.path.exists(filename) == False:
        print("File does not exist")        

    schedule.every(30).seconds.do(monitorFileSize, filename)

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Program terminated by user")


if __name__ == "__main__":
    main()

    