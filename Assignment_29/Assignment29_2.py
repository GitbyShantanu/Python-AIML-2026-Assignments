# WAP which accepts file name, open that file and display entire content on console. 
# Input: Demo.txt

import os


def main():
    FileName = input("Enter the file name: ")

    if os.path.exists(FileName) == True:
        fobj = open(FileName, "r")
        
        content = fobj.read()
        print(content)
        
        fobj.close()
    else:
        print("File does not exist")
   
if __name__ == "__main__":
    main()
