# WAP that scans specified directory every minute. Task should display: 
# Directory name, No of files, No of subdirectories, Date and time of scanning 
# Use the os module. 

# Output: 
# Directory Scanned: E:/Data
# Total Files: 15
# Total Subdirectories: 4
# Scan time: 25-07-2026 03:18:00 PM

import schedule
import os 
import schedule
import time
from datetime import datetime

def scanDirectory(directory):
    files = 0
    subfolders = 0

    for FolderName, Subfolder, fileName in os.walk(directory):
        for subf in Subfolder:
            subfolders += 1
        
        for fname in fileName:
            files += 1
    
    print("Directory Scanned: ", directory)
    print("Total Files: ", files)
    print("Total Subdirectories: ", subfolders)
    print("Scan time: ", datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))


def main():
    dirName = input("Enter the directory name: ")
    if os.path.exists(dirName) == False:
        print("Directory does not exist!")
        return

    if os.path.isdir(dirName) == False:
        print("Path is not a directory!")
        return

    schedule.every(1).minutes.do(scanDirectory, dirName)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()