# WAP which accepts existing file name through command line args.
# Creates new file Demo.txt and copies all contents from existing file into Demo.txt

import os
import sys


def main():
    FileName = sys.argv[1]

    if os.path.exists(FileName) == True:
        fobj1 = open(FileName, "r")
        fobj2 = open("Demo.txt", "w")
        
        content = fobj1.read()
        fobj2.write(content)
        print(f"Created Demo.txt file. \nCopied contents of {sys.argv[1]} into Demo.txt successfully")
        
        fobj1.close()
        fobj2.close()
    else:
        print("File does not exist")
   
if __name__ == "__main__":
    main()
