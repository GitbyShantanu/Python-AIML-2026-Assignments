# WAP that accepts a list of integers 
# Uses Pool.map() to calculate sum of squares from 1 to N for every element in list.

import multiprocessing


def SumSquare(No):
    Sum = 0
    for i in range(1, No+1):
        Sum = Sum + (i*i)
    
    return Sum


def main():
    Data = [1000000, 2000000, 3000000, 4000000]
    print("Input List : ",Data)

    Result = []

    pobj = multiprocessing.Pool()
    Result = pobj.map(SumSquare, Data)

    pobj.close()
    pobj.join()

    print("Result is : \n",Result)

if __name__ == "__main__":
    main()

