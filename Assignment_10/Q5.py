# WAP which accepts one number and prints all odd numbers till that number.

def printOddNumbers(no):
    for i in range(1, no+1, 2):
        print(i, end=" ")

def main():
    no = int(input("Enter no: "))
    printOddNumbers(no)

if __name__== "__main__":
    main()