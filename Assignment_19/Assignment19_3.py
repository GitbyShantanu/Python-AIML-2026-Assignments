# WAP which contains filter(), map() and reduce(). Contains one list of numbers accepted from user.
# Filter should filter out numbers which are >= 70 and <= 90. 
# Map will increase each no by 10. 
# Reduce will return product of all that numbers

from functools import reduce

def main():
    size = int(input("Number of elements: "))
    Data = []

    for i in range(size):
        no = int(input("Enter element: "))
        Data.append(no)

    # Data = [4,34,36,76,68,24,89,23,86,90,45,70]
    print("Input List : ",Data)

    fData = list(filter(lambda n: (n >= 70 and n <= 90), Data))
    print("List after filter : ",fData)

    mData = list(map(lambda n: n + 10, fData))
    print("List after map : ",mData)

    rData = reduce(lambda a, b: a * b, mData)
    print("Output of reduce : ",rData)


if __name__ == "__main__":
    main()