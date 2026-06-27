# WAP which accepts one number and checks it is perfect number or not

def chkPerfect(no):
    factSum = 0
    for i in range(1, no):
        if no % i == 0:
            factSum = factSum + i 
    
    return factSum == no
    

def main():
    val = int(input("Enter no: "))
    ans = chkPerfect(val)
    if ans:
        print(f"{val} is Perfect Number")
    else:
        print("Not Perfect number")

if __name__ == "__main__":
    main()