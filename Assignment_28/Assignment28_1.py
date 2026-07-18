# WAP which accepts file name and counts how many lines are present in the file. 
# Input: Demo.txt
# Output: Total number of lines in Demo.txt is : <cnt>

import os


def main():
    FileName = input("Enter the file name: ")

    if os.path.exists(FileName) == True:
        fobj = open(FileName, "r")
        
        linesList = fobj.readlines()
        print(f"Total number of lines in {FileName} is: {len(linesList)}")
        
        fobj.close()
    else:
        print("File does not exist")
   
if __name__ == "__main__":
    main()
