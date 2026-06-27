# WAP which accepts a number and prints cube of that number

def cube(no):
    return no ** 3

def main():
    val = int(input("Enter no: "))
    
    ans = cube(val)
    print("Cube is: ",ans)

if __name__ == "__main__":
    main()