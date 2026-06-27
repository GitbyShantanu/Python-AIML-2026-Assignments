# WAP which accepts one number and prints binary equivalent

def convertToBinary(no): #6
    bin = ""
    while no > 0:
        bin = str(no % 2) + bin
        no = no // 2
    
    return bin

def main():
    val = int(input("Enter no: "))

    ans = convertToBinary(val)
    print(f"Binary equivalent of {val} is : {ans}")

if __name__ == "__main__":
    main()