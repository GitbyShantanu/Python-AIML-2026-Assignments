# WAP which accepts one number and prints multiplication table of that number.

def printTable(no):
    for i in range(no, no*10+1, no):
        print(i, end=" ")
    
def main():
    val = int(input("Enter no: "))
    printTable(val)

if __name__== "__main__":
    main()