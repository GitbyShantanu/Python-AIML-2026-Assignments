# WAP which accepts one number and checks prime or not

def ChkPrime(No):
    for i in range(2, No//2 +1):
        if No % i == 0:
            return False
    
    return True

def main():
    val = int(input("Enter number: "))

    Ret = ChkPrime(val)
    if Ret == True: 
        print(f"{val} is prime number")
    else:   
        print(f"{val} is not prime number")

if __name__ == "__main__":
    main()