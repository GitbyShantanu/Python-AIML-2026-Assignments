# WAP that calculates factorials of multiple numbers simultaneously using Pool.map().
# Display PID, Input Number, Factorial

import multiprocessing
import os


def factorial(no):
    fact = 1
    for i in range(1, no+1):
        fact = fact * i

    print(f"PID : {os.getpid()}, Input No : {no}, Factorial : {fact}")
    return fact

def main():
    Data = [10, 15, 20, 25]
    print("Input List : ",Data)

    Result = []

    pobj = multiprocessing.Pool()
    Result = pobj.map(factorial, Data)

    pobj.close()
    pobj.join()

    print(f"\nResult is : \n{Result}")

if __name__ == "__main__":
    main()

