# Please follow these rules while designing automation script as: 
# 1. Accept input through command line or thorugh file
# 2. Display any message in log file instead of console.
# 3. For seperate task define seperate function. 
# 4. For rubustness handle every expected exception
# 5. Perform validations before taking any action
# 6. Create user defined modules to store the functionality. 

# Q1. Design automation script which accepts process name and displays info of running processes as its name, PID, username. 
# Usage : ProcInfo.py Notepad

import psutil
import sys
import ProcUtil as ProcUtil
import os

def main():
    if len(sys.argv) != 2:
        print("Error: Please provide a process name as a command-line argument.")
        print("Usage: python Assignment34_2.py <ProcessName>")
        sys.exit(1)

    procName = sys.argv[1]
    
    ProcList = ProcUtil.get_process_name_info(procName)
    if len(ProcList) == 0:
        print(f"No process found with name '{procName}'.")
        return
    
    err = ProcUtil.log_process(ProcList)
    if err:
        print(f"Error logging process information: {err}")
        return

if __name__ == "__main__":
    main()