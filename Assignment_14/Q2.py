# Write a lambda function which accepts one number and returns its square.

cube = lambda n: n ** 3

def main():
    val = int(input("Enter nummber: "))
    Ret = cube(val)
    print("Cube is :", Ret)

if __name__ == "__main__":
    main()