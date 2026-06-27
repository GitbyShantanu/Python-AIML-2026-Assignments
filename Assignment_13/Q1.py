# WAP which accepts length, width of rectangle and print area.

def calculateArea(length, width):
    area = 0
    area = length * width
    return area

def main():
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))

    ans = calculateArea(length, width)
    print(f"Area of rectangle is : {ans}")

if __name__ == "__main__":
    main()