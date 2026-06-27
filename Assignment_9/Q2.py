# WAP which contains one function chkGreater() which accepts two numbers from user and returns greater number.

def chkGreator(no1, no2):
    ans = 0
    if no1 > no2:
        return no1
    else:
        return no2 

def main():
    value1 = int(input("Enter 1st no: "))
    value2 = int(input("Enter 2nd no: "))

    ret = chkGreator(value1, value2)
    print("Greator number is :", ret)

if __name__ == "__main__":
    main()