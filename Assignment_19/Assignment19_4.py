# WAP which contains filter(), map() and reduce(). Contains one list of numbers accepted from user.
# Filter should filter out numbers which are even. 
# Map will calculate square. 
# Reduce will return addition of all that numbers

from functools import reduce

def main():
    size = int(input("Number of elements: "))
    Data = []

    for i in range(size):
        no = int(input("Enter element: "))
        Data.append(no)

    # Data = [5,2,3,4,3,4,1,2,8,10]
    print("Input List : ",Data)

    fData = list(filter(lambda n: (n % 2 == 0), Data))
    print("List after filter : ",fData)

    mData = list(map(lambda n: n**2, fData))
    print("List after map : ",mData)

    rData = reduce(lambda a, b: a + b, mData)
    print("Output of reduce : ",rData)


if __name__ == "__main__":
    main()