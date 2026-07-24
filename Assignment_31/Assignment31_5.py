# WAP that accepts a dirName from user and counts the number of files inside it every 5 minutes 
# Write result into DirectoryCountLog.txt. 
# Each entry should contain: Dir Path, Number of files, Date and time 

import schedule
from datetime import datetime
import os
import time

def countFiles(dirName):
    cnt = 0
    for FolderName, Subfolder, fileName in os.walk(dirName):
        for fname in fileName:
            cnt += 1
    
    fobj = open("DirectoryCountLog.txt", "a")
    fobj.write("Directory Path: " + dirName + "\n")
    fobj.write("Number of files: " + str(cnt) + "\n")
    fobj.write("Date and time: " + datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") + "\n\n")
    
    fobj.close()
    print("Log file created successfully!")


def main():
    dirName = input("Enter the directory name: ")

    if os.path.exists(dirName) == False:
        print("Directory does not exist!")
        return

    if os.path.isdir(dirName) == False:
        print("Path is not a directory!")
        return

    schedule.every(5).seconds.do(countFiles, dirName)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
    

