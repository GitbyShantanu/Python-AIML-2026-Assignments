# WAP which accepts one number and print that many numbers starting from 1.

def printNumbers(no):
    for i in range(1, no+1):
        print(i, end=" ")

def main():
    val = int(input("Enter no: "))
    printNumbers(val)

if __name__ == "__main__":
    main()