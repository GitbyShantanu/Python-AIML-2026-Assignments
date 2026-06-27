# WAP which accepts one number and prints sum of digits 

def printDigitsSum(no):
    digitSum = 0
    digit = 0

    while no > 0:
        digit = no % 10
        digitSum = digitSum + digit
        no = no // 10
    
    return digitSum

def main():
    no = int(input("Enter no: "))
    
    ans = printDigitsSum(no)
    print(f"Sum of digits of {no} is: {ans}")

if __name__== "__main__":
    main()