# WAP which accepts N numbers and stores in list. 
# Accept another number from user and find its frequency in the list

def CntFrequency(Arr, k):
    cnt = 0
    for no in Arr:
        if no == k:
            cnt += 1
    
    return cnt

def main():
    size = int(input("Number of elements: "))
    Data = []

    for i in range(size):
        no = int(input("Enter element: "))
        Data.append(no)

    # Data = [13,5,45,7,4,56,5,34,2,5,65]
    print("List : ", Data)

    k = int(input("Element to Search : "))
    
    Ret = CntFrequency(Data, k)
    print(f"Count of {k} is :", Ret)

if __name__ == "__main__":
    main()