# WAP which accepts one number and checks whether it is divisible by 3 and 5. 

def chkDivisible(no):
    if no % 3 == 0 and no % 5 == 0:
        return True
    else: 
        return False
    
def main():
    val = int(input("Enter no: "))

    ans = chkDivisible(val)
    if ans:
        print(f"{val} is divisible by 3 and 5")
    else:
        print("Not divisible")

if __name__ == "__main__":
    main()
