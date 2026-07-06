# WAP which accept name from user and display length of its name

def Display(s):
    return len(s)

def main():
    name = input("Enter your name: ")

    Ret = Display(name)
    print("Length of your name is:", Ret)

if __name__ == "__main__":
    main()  