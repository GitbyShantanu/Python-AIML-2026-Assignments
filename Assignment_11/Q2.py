# WAP which accepts one number and prints count of digits in that number

def countDigits(no):
    cnt = 0
    while no > 0:
        cnt += 1
        no = no // 10

    return cnt

def main():
    no = int(input("Enter no: "))
    
    ans = countDigits(no)
    print(f"Count of digits in {no} is: {ans}")

if __name__== "__main__":
    main()