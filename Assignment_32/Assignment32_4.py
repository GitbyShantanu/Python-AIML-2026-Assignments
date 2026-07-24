# WAP that copies all .txt files from 1 dir to another every 10 minutes. 
# Program should: 
# 1. Accept source and destination directories
# 2. Validate both dirs 
# 3. Copy only .txt files 
# 4. Maintain log of copied files
# 5. Avoid terminating if one file cannot be copied 

import schedule
import schedule
from datetime import datetime
import time
import os
import shutil

def copyTxtFiles(sourceDir, destDir):
    if os.path.exists(sourceDir) == False:
        print("Source Directory does not exist")
        return

    if os.path.exists(destDir) == False:
        print("Destination Directory does not exist")
        return 

    if os.path.isdir(sourceDir) == False:
        print("Source Directory is not a directory")
        return

    if os.path.isdir(destDir) == False:
        print("Destination Directory is not a directory")
        return

    if os.access(sourceDir, os.R_OK) == False:
        print("Source Permission denied")
        return

    if os.access(destDir, os.W_OK) == False:
        print("Destination Permission denied")
        return

    fobj = open("CopyLog.txt", "a")
    fobj.write("#" * 70 + "\n")

    for foldername, subfolders, filenames in os.walk(sourceDir):
        for fname in filenames:
            if fname.endswith(".txt"):
                src = os.path.join(foldername, fname)
                dest = os.path.join(destDir, fname)
                shutil.copy(src, dest)
                fobj.write(f"File {fname} copied successfully\n")

    fobj.write(f"Source: {sourceDir}\n") 
    fobj.write(f"Destination: {destDir}\n")

    now = datetime.now()
    fobj.write(f"Date & Time: {now}\n") 
    fobj.write("#" * 70 + "\n\n")
    fobj.close()

    print("Copying completed....") 


def main():
    sourceDir = input("Enter Source Directory: ")
    destDir = input("Enter Destination Directory: ")

    # copyTxtFiles(sourceDir, destDir)
    schedule.every(10).minutes.do(copyTxtFiles, sourceDir, destDir)

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Program terminated by user")
    
if __name__ == "__main__":
    main()

    