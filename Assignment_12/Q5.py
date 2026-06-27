# WAP which accepts one number and print that many numbers in reverse order.

def printNumbersReversed(no):
    for i in range(no, 0, -1):
        print(i, end=" ")

def main():
    val = int(input("Enter no: "))
    printNumbersReversed(val)

if __name__ == "__main__":
    main()