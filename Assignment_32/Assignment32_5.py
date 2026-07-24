# WAP that deletes all empty files from specified directory every hour.
# Program should: 
# Scan the directory recursively 
# Detects files whose size is zero bytes 
# Delete the empty files 
# Store deleted file paths in a log file
# Handle permissions errors 
# Test the program only on sample directory

import schedule
import time
from datetime import datetime
import os 
import sys

def deleteEmptyFiles(dirname = "Test_src"):
    if os.path.exists(dirname) == False:
        print(f"Directory '{dirname}' does not exist.")
        return
        
    if os.path.isdir(dirname) == False:
        print(f"Path '{dirname}' is not a directory.")
        return

    if os.access(dirname, os.R_OK) == False:
        print(f"Permission denied for directory '{dirname}'.")
        return

    if os.access(dirname, os.W_OK) == False:
        print(f"Permission denied for directory '{dirname}'.")
        return
        
    logFile = "DeleteLog.txt"
    fobj = open(logFile, "a")   
    print(f"Log file created with name {logFile}")    
    
    
    now = datetime.now()
    fobj.write("="*70 + "\n")
    fobj.write(f"Scan started at {now}\n") 
    fobj.write("-"*70 + "\n")

    totalCnt = 0
    deletedCnt = 0

    for foldername, subfolders, filenames in os.walk(dirname):
        for fname in filenames:
            totalCnt += 1
            
            filePath = os.path.join(foldername, fname)
            if os.path.getsize(filePath) == 0:
                os.remove(filePath)
                fobj.write(f"File {fname} deleted\n")
                deletedCnt += 1

    if deletedCnt == 0:
        fobj.write("No empty files found\n")

    fobj.write("-"*70 + "\n")

    fobj.write(f"Scan completed at {now}\nReport: \n") 
    fobj.write(f"Total files scanned: {totalCnt}\n")
    fobj.write(f"Total Empty files deleted: {deletedCnt}\n")
    fobj.write("#"*70 + "\n\n")    
    fobj.close()

    print("-"*70)
    print(f"Total files scanned: {totalCnt}")
    print(f"Total files deleted: {deletedCnt}")
    print("-"*70)


def main():
    if len(sys.argv) != 2:
        print("Error: Invalid arguments passed") 
        print("Usage: python Assignment32_5.py directoryName")
        return 

    directory = sys.argv[1]

    deleteEmptyFiles(directory)
    schedule.every(1).hour.do(deleteEmptyFiles, directory)
    
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Program terminated by user")

if __name__ == "__main__":
    main()