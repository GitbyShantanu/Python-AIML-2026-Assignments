# Write a lambda function using reduce() which accepts a list of numbers and returns product of all numbers.

from functools import reduce

Product = lambda No1, No2 : No1 * No2

def main():
    Data = [1, 2, 3, 4, 5]
    print("Data: ", Data)
    
    rData = reduce(Product, Data)
    print("Data after reduce: ", rData) 

if __name__ == "__main__":
    main()