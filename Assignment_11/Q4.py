# WAP which accepts one number and prints reverse of that number 

def printReverse(no):
    reversed = 0
    digit = 0

    while no > 0:
        digit = no % 10
        reversed = (reversed * 10) + digit
        no = no // 10
    
    return reversed

def main():
    no = int(input("Enter no: "))
    
    ans = printReverse(no)
    print(f"Reverse of {no} is {ans}.")

if __name__== "__main__":
    main()