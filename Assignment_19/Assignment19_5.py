# WAP which contains filter(), map() and reduce(). Contains one list of numbers accepted from user.
# Filter should filter out prime numbers. 
# Map will multiply each number by 2. 
# Reduce will return Maximum of all that numbers

from functools import reduce

def ChkPrime(No):
    for i in range(2, No//2 + 1):
        if No % i == 0:
            return False
    return True

def Maximum(arr):
    max = arr[0]
    for no in arr:
        if no > max:
            max = no
    return max

def main():
    size = int(input("Number of elements: "))
    Data = []

    for i in range(size):
        no = int(input("Enter element: "))
        Data.append(no)

    # Data = [2,70,11,10,17,23,31,77]
    print("Input List : ",Data)

    fData = list(filter(ChkPrime, Data))
    print("List after filter : ",fData)

    mData = list(map(lambda n: n*2, fData))
    print("List after map : ",mData)

    rData = reduce(Maximum, mData)
    print("Output of reduce : ",rData)

if __name__ == "__main__":
    main()