# WAP which accepts N numbers and stores in list. Return Maximum

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

    # Data = [13,5,45,7,4,56]
    print("List : ", Data)
    
    Ret = Maximum(Data)
    print("Maximum is : ", Ret)

if __name__ == "__main__":
    main()