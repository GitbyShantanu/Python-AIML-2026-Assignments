# WAP which accepts N numbers and stores in list. Return addition of all list elements.

def Addition(Arr):
    sum = 0
    for no in Arr:
        sum = sum + no

    return sum

def main():
    size = int(input("Number of elements: "))
    Data = []

    for i in range(size):
        no = int(input("Enter element: "))
        Data.append(no)

    # Data = [13,5,45,7,4,56]
    print("List: ", Data)
    
    Ret = Addition(Data)
    print("Addition is: ", Ret)

if __name__ == "__main__":
    main()