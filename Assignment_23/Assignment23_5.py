# WAP using multiprocessing .pool 
# Calculates factorials of multiple numbers simultaneously for every N.

import multiprocessing
import os


def factorial(no):
    fact = 1
    for i in range(1, no+1):
        fact = fact * i

    print(f"\nProcess ID : {os.getpid()}")
    print(f"Input Number : {no}")
    print(f"Factorial : {fact}")
    return fact


def main():
    Data = [10, 15, 20, 25]
    print("Input List : ",Data)

    Result = []

    pobj = multiprocessing.Pool()
    Result = pobj.map(factorial, Data)

    pobj.close()
    pobj.join()

    print(f"\nResult is : {Result}")

if __name__ == "__main__":
    main()

