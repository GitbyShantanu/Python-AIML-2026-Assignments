# WAP using multiprocessing .pool 
# Counts how many Odd numbers exist between 1 to N using Pool.map() 
# Display PID, Input, Odd Number count

import multiprocessing
import os


def cntOdd(no):
    cnt = 0
    for i in range(1, no+1, 2):
        cnt += 1

    print(f"\nProcess ID : {os.getpid()}")
    print(f"Input Number : {no}")
    print(f"Odd Number Count : {cnt}")
    return cnt


def main():
    Data = [1000000, 2000000, 3000000, 4000000]
    print("Input List : ",Data)

    Result = []

    pobj = multiprocessing.Pool()
    Result = pobj.map(cntOdd, Data)

    pobj.close()
    pobj.join()

    print(f"\nResult is : {Result}")

if __name__ == "__main__":
    main()

