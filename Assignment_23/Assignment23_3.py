# WAP using multiprocessing .pool 
# Counts how many even numbers exist between 1 to N using Pool.map() 
# Display PID, Input, Even Number count

import multiprocessing
import os


def cntEven(no):
    cnt = 0
    for i in range(2, no+1, 2):
        cnt += 1

    print(f"\nProcess ID : {os.getpid()}")
    print(f"Input Number : {no}")
    print(f"Even Number Count : {cnt}")
    return cnt


def main():
    Data = [1000000, 2000000, 3000000, 4000000]
    print("Input List : ",Data)

    Result = []

    pobj = multiprocessing.Pool()    
    Result = pobj.map(cntEven, Data)

    pobj.close()
    pobj.join()

    print(f"\nResult is : {Result}")

if __name__ == "__main__":
    main()

