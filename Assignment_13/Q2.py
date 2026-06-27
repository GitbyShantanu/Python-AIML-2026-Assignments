# WAP which accepts length, width of rectangle and print area.

def calculateArea(radius, PI = 3.14):
    area = 0
    area = PI * (radius * radius)
    return area

def main():
    radius = float(input("Enter radius of circle: "))
    
    ans = calculateArea(radius)
    print(f"Area of circle is : {ans}")

if __name__ == "__main__":
    main()