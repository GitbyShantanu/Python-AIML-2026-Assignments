# WAP which accepts 2 file names via command line args
# compares contents of both files. if same display Success, otherwise Failure. 

import os
import sys


def main():
    FileName1 = sys.argv[1]
    FileName2 = sys.argv[2]

    if (os.path.exists(FileName1) == True) and (os.path.exists(FileName2) == True):
        fobj1 = open(FileName1, "r")
        fobj2 = open(FileName2, "r")
        
        content1 = fobj1.read()
        content2 = fobj2.read()
        
        if content1 == content2:
            print("Success")
        else:
            print("Failure")
        
        fobj1.close()
        fobj2.close()
    else:
        print("File does not exist")


if __name__ == "__main__":
    main()
