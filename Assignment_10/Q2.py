# WAP which accepts one number and prints sum of first n natural numbers.

def sumOfNaturalNumbers(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
    
    return sum 

    # sum = (n * (n+1)) // 2
    # return sum 

def main():
    n = int(input("Enter n: "))

    ans = sumOfNaturalNumbers(n)
    print(f"Sum of first {n} natural numbers is: {ans}")

if __name__== "__main__":
    main()