# Write a lambda function using reduce() which accepts a list of numbers and returns Maximum.

from functools import reduce

Maximum = lambda No1, No2 : No1 if No1 > No2 else No2

def main():
    Data = [1, 2, 3, 4, 5]
    print("Data: ", Data)
    
    rData = reduce(Maximum, Data)
    print("Data after reduce: ", rData)

if __name__ == "__main__":
    main()