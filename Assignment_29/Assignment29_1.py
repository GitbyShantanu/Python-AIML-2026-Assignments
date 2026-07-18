# WAP which accepts file name and checks whether file exists in current dir or not. 
# Input: Demo.txt

import os


def main():
    FileName = input("Enter the file name: ")

    if os.path.exists(FileName) == True:
        print(f"{FileName} exists in current directory")        
    else:
        print(f"{FileName} does not exist")
   
if __name__ == "__main__":
    main()
