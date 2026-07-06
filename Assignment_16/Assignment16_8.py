# WAP which accept one number from user print that number of '*' on screen. 
 
def Display(No):
    for i in range(No):
        print("*", end=" ")

def main():
    val = int(input("Enter number: "))
    Display(val)

if __name__ == "__main__":
    main()  