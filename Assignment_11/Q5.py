# WAP which accepts one number and prints reverse of that number 

def chkPallindrome(no):
    copy = no 
    reversed = 0
    digit = 0

    while no > 0:
        digit = no % 10
        reversed = (reversed * 10) + digit
        no = no // 10

    return copy == reversed

def main():
    no = int(input("Enter no: "))
    
    ans = chkPallindrome(no)
    if ans:
        print(f"{no} is Pallindrome")
    else:
        print(f"{no} is not Pallindrome")

if __name__== "__main__":
    main()