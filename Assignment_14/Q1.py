# Write a lambda function which accepts one number and returns its square.

square = lambda n: n ** 2 

def main():
    val = int(input("Enter nummber: "))
    Ret = square(val)
    print("Square is :", Ret)

if __name__ == "__main__":
    main()