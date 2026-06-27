# WAP which accepts 2 numbers and prints addition, subtraction, multiplication and division.

def calculate(no1, no2):
    addition = no1 + no2
    subtraction = no1 - no2
    multiplication = no1 * no2

    if no2 == 0:
        division = "Division by zero is not allowed"
        return addition, subtraction, multiplication, division
    
    division = no1 / no2

    return addition, subtraction, multiplication, division

def main():
    val1 = int(input("Enter first no: "))
    val2 = int(input("Enter second no: "))
    
    add, sub, mul, div = calculate(val1, val2)
    print(f"Addition is: {add}\nsubtraction is: {sub}\nmultiplication is: {mul}\ndivision is: {div}")
    
if __name__ == "__main__":
    main()