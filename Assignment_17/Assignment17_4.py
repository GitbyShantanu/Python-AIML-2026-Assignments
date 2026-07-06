# WAP which accpets 1 no return its addition of factors
# Input: 12
# Output: 16 (1 + 2 + 3 + 4 + 6)

def FactorSum(No):
    sum = 0
    for i in range(1, No//2 + 1):
        if No % i == 0:
            sum = sum + i
    
    return sum 

def main():
    val = int(input("Enter number: "))

    Ret = FactorSum(val)
    print(f"Addition of factors of {val} is: {Ret}")

if __name__ == "__main__":
    main()