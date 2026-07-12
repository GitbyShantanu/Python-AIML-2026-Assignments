# WAP using multiprocessing .pool 
# To calculate tbe sum of all Odd numbers from 1 to N for every number in the given list
# Display PID, Input Number, Sum of Odd numbers. 

import multiprocessing
import os


def sumOdd(no):
    Sum = 0
    for i in range(1, no+1, 2):
        Sum = Sum + i

    print(f"\nProcess ID : {os.getpid()}")
    print(f"Input Number : {no}")
    print(f"Sum of Odd Numbers : {Sum}")
    return Sum 


def main():
    Data = [1000000, 2000000, 3000000, 4000000]
    print("Input List : ",Data)

    Result = []

    pobj = multiprocessing.Pool()    
    Result = pobj.map(sumOdd, Data)

    pobj.close()
    pobj.join()

    print(f"\nResult is : {Result}")

if __name__ == "__main__":
    main()

