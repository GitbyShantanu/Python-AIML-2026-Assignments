# WAP that creates a new text file every minutes. 
# The filename should contain the current timestamp. Example: File_25_07_2026_16_30_00.txt 
# Write the following info in the file: filename, creation date, creation time 

import schedule
from datetime import datetime
import time

def createFile():
    now = datetime.now()
    timestamp = now.strftime("%d_%m_%Y_%H_%M_%S")
    filename = f"File_{timestamp}.txt"

    fobj = open(filename, "w")
    fobj.write(f"Filename: {filename}\n")
    fobj.write(f"Creation Date: {now.strftime('%d_%m_%Y')}\n")
    fobj.write(f"Creation Time: {now.strftime('%H_%M_%S')}\n")
    
    fobj.close()
    print(f"File {filename} created successfully") 


def main():
    schedule.every(1).second.do(createFile)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()

    