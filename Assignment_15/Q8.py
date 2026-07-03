# Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers which are divisible by 3 and 5.

ChkDivisible = lambda No: (No % 3 == 0) and (No % 5 == 0)

def main(): 

    Data = [5, 10, 15, 45, 50, 60, 75]
    print("Data: ", Data)

    fData = list(filter(ChkDivisible, Data))   
    print("Data after filter: ", fData)  

if __name__ == "__main__":
    main()