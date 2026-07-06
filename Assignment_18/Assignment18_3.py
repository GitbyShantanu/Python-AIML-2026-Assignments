# WAP which accepts N numbers and stores in list. Return minimum

def Minimum(arr):
    min = arr[0]

    for no in arr:
        if no < min:
            min = no
        
    return min 

def main():
    size = int(input("Number of elements: "))
    Data = []

    for i in range(size):
        no = int(input("Enter element: "))
        Data.append(no)

    # Data = [13,5,45,7]
    print("List : ", Data)
    
    Ret = Minimum(Data)
    print("Minimum is : ", Ret)

if __name__ == "__main__":
    main()