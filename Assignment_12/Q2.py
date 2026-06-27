# WAP which accepts one number and print its factors

def printFactors(no):
    for i in range(1, no+1):
        if no % i == 0:
            print(i, end=" ")

def main():
    val = int(input("Enter no: "))
    printFactors(val)

if __name__ == "__main__":
    main()