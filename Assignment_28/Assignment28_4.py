# WAP which accepts 2 file names from user 1) Existing file, 2) New File 
# Copy all content from existing file to new file
# Input: ABC.txt, Demo.txt

import os


def main():
    existingFileName = input("Enter the existing file name: ")

    if os.path.exists(existingFileName) == True:
        newFileName = input("Enter the new file name: ")

        fobj1 = open(existingFileName, "r")
        fobj2 = open(newFileName, "w")
        
        content = fobj1.read()
        fobj2.write(content)
        print(f"Contents of {existingFileName} copied to {newFileName} successfully")
        
        fobj1.close()
        fobj2.close()
    else:
        print("File does not exist")
   
if __name__ == "__main__":
    main()
