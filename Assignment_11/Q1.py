# WAP which accepts one number and checks whether its prime or not.

def chkPrime(no):
    if no <= 1:
        return False
    
    for i in range(2, no//2+1):
        if no % i == 0:
            return False
        
    return True

def main():
    no = int(input("Enter no: "))
    ans = chkPrime(no)
    if ans:
        print(f"{no} is Prime Number")
    else:
        print(f"{no} is not Prime")

if __name__== "__main__":
    main()