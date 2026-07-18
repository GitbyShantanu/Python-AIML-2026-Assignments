# WAP which accepts file name from user and counts how many words are present in the file. 
# Input: Demo.txt
# Output: Total number of words in Demo.txt

import os


def main():
    # FileName = input("Enter the file name: ")
    FileName = "Demo.txt"
    
    if os.path.exists(FileName) == True:
        fobj = open(FileName, "r")
        
        content = fobj.read()
        wordsList = content.split()
        print(f"Total number of words in {FileName} is: {len(wordsList)}")  

        fobj.close()
    else:
        print("File does not exist")
   
if __name__ == "__main__":
    main()
