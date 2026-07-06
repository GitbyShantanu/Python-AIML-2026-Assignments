# WAP which accepts N numbers and stores in list. 
# Return Addition of all prime numbers from list. 
# Main python file accepts N numbers and pass each number to chkPrime() which is part of user defined module MarvellousNum
# Name of function from main python file should be ListPrime(). 

from MarvellousNum import ChkPrime

def PrimeAddition(Arr):
    sum = 0
    for no in Arr:
        sum += no

    return sum 

def ListPrime(Arr):
    primeData = []
    for no in Arr:
        if ChkPrime(no) == True:
            primeData.append(no)        
    
    return primeData

def main():
    size = int(input("Number of elements: "))
    Data = []

    for i in range(size):
        no = int(input("Enter element: "))
        Data.append(no)

    # Data = [13,5,45,7,4,56,10,34,2,5,8]
    print("List : ", Data)

    primeData = ListPrime(Data)
    print("primeData : ",primeData)
    
    Ret = PrimeAddition(primeData)
    print("Addition of prime elements is : ",Ret)


if __name__ == "__main__":
    main()