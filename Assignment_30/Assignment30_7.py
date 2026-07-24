# Write a Python program that performs a file backup every hour
# The program should:
#   1. Accept the source file path. 
#   2. Accept the destination directory path. 
#   3. Copy the source file to the destination directory. 
#   4. Add the current date and time to the backup file name. 
#   5. Write the backup operation details into backup_log.txt 
# Use the shutil module for file copying.  

import os
import shutil
import datetime
import time
import schedule


def backupFile(sourceFile, destinationDir):
    if os.path.exists(sourceFile) == False:
        print("Source file does not exist.")
        return

    if os.path.exists(destinationDir) == False:
        print("Destination directory does not exist.")
        return

    if os.path.isdir(destinationDir) == False:
        print("Destination path is not a directory.")
        return

    timestamp = datetime.datetime.now()

    backupFileName = f"Data {timestamp.strftime("%d_%m_%Y %H_%M_%S")}.txt"
    backupFileName = backupFileName.replace(" ", "_")
    print("Backup File Name: ",backupFileName)

    backupFilePath = os.path.join(destinationDir, backupFileName)

    shutil.copy(sourceFile, backupFilePath)
    print("Source file is copied at destination")

    print(f"Backup completed successfully at {timestamp.strftime("%d-%m-%Y %I:%M:%S %p")}")


def main():
    sourceFile = input("Enter source file path: ")
    destinationDir = input("Enter destination directory path: ")

    schedule.every(1).hour.do(backupFile, sourceFile, destinationDir)

    print("\nStarting hourly backup. Press Ctrl+C to stop.")
    while True:
        schedule.run_pending()
        time.sleep(500)

if __name__ == "__main__":
    main()