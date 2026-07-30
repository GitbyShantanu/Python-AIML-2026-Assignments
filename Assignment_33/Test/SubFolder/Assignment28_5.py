# WAP accepts file name and word from user and check whether word is present in file or not. 
# Input: Demo.txt,  Marvellous
# Output: Marvellous is present in Demo.txt

import os


def main():
    FileName = input("Enter the file name: ")
    word = input("Enter the word: ")

    if os.path.exists(FileName) == True:

        fobj = open(FileName, "r")
        
        content = fobj.read()

        if word in content:
            print(f"{word} is present in {FileName}")
        else:
            print(f"{word} is not present in {FileName}")
        
        fobj.close()
    else:
        print("File does not exist")
   
if __name__ == "__main__":
    main()
