# WAP which accepts file name and display content line by line. 
# Input: Demo.txt

import os


def main():
    # FileName = input("Enter the file name: ")
    FileName = "Demo.txt"

    if os.path.exists(FileName) == True:
        fobj = open(FileName, "r")
        
        lines = fobj.readlines()
        for line in lines:
            print(line)
        
        fobj.close()
    else:
        print("File does not exist")
   
if __name__ == "__main__":
    main()
