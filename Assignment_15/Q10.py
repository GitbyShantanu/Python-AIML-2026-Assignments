# Write a lambda function using filter() which accepts a list of numbers and returns a count of even numbers.

ChkEven = lambda No : No % 2 == 0

def main():
    Data = [23, 45, 67, 89, 90, 34, 12, 56]
    print("Data: ", Data)
    
    fData = list(filter(ChkEven, Data))
    print("Data after filter: ", fData)
    print("Count of even numbers: ", len(fData))

if __name__ == "__main__":
    main()