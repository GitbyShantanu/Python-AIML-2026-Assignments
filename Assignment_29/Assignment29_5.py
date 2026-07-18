# WAP which accepts a file name and one string from user.
# Returns frequency of that string in file. 

import os
import sys


def main():
    FileName = sys.argv[1]
    Str = sys.argv[2]
    cnt = 0

    if os.path.exists(FileName) == True:
        fobj = open(FileName, "r")

        content = fobj.read()
        wordsList = content.split()

        for word in wordsList:
            if word == Str:
                cnt += 1

        print(f"Frequency of {Str} in {FileName} is: {cnt}")
        fobj.close()
    else:
        print("File does not exist")
   
if __name__ == "__main__":
    main()
