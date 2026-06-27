# WAP which accepts one number and prints all even numbers till that number.

def printEvenNumbers(no):
    for i in range(2, no+1, 2):
        print(i, end=" ")

def main():
    no = int(input("Enter no: "))
    printEvenNumbers(no)

if __name__== "__main__":
    main()