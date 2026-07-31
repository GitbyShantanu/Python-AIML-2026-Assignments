# Please follow these rules while designing automation script as: 
# 1. Accept input through command line or thorugh file
# 2. Display any message in log file instead of console.
# 3. For seperate task define seperate function. 
# 4. For rubustness handle every expected exception
# 5. Perform validations before taking any action
# 6. Create user defined modules to store the functionality. 

# Q1. Design automation script which displays info of running processes as its name, PID, username. 
# Usage : ProcInfo.py

import psutil
import ProcUtil


def main():
    ProcList =ProcUtil.get_process_info()
    fobj = open("ProcInfoLogs.log", "w")

    i = 0
    for proc in ProcList:
        fobj.write(f"{i+1}. Process Name: {proc['name']}, PID: {proc['pid']}, Username: {proc['username']}\n")
        i += 1
    fobj.close()

if __name__ == "__main__":
    main()