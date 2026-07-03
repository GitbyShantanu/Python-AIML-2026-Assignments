# Write a lambda function using filter() which accepts a list of numbers and returns a list of odd numbers.

chkOdd = lambda No : No % 2 != 0 

def main():
    Data = [1, 2, 3, 4, 5]
    print("Data: ", Data)
    
    fData = list(filter(chkOdd, Data))
    print("Data after filter: ", fData)

if __name__ == "__main__":
    main()