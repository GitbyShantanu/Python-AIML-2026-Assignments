# Please follow these rules while designing automation script as: 
# 1. Accept input through command line or thorugh file
# 2. Display any message in log file instead of console.
# 3. For seperate task define seperate function. 
# 4. For rubustness handle every expected exception
# 5. Perform validations before taking any action
# 6. Create user defined modules to store the functionality. 

# Q1. Design automation script which accepts Directory name and create log file in that directory that displays info of running processes as its name, PID, username. 
# Usage : ProcInfo.py Demo

import sys
import os
import ProcUtil


def main():
    DirectoryName = sys.argv[1]

    if os.path.exists(DirectoryName) == False:
        os.mkdir(DirectoryName)
    else:
        if os.path.isdir(DirectoryName) == False:
            print(f"{DirectoryName} exists, but it is not a directory.")
            return

    ProcList = ProcUtil.get_process_info()

    err = ProcUtil.log_process(ProcList, DirectoryName)
    if err:
        print(err)


if __name__ == "__main__":
    main()