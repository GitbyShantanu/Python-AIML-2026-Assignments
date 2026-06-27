# WAP which accepts one number and prints square of that number

def square(no):
    return no ** 2

def main():
    val = int(input("Enter no: "))
    
    ans = square(val)
    print("Square is :",ans)

if __name__ == "__main__":
    main()