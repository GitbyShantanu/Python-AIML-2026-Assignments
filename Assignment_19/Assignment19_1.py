# WAP which contains one lambda function which accepts one parameter and return power of two. 

Square = lambda n : n ** 2 

def main():
    val = int(input("Enter number: "))

    Ret = Square(val)
    print(Ret)

if __name__ == "__main__":
    main()