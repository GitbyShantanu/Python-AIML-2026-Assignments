# WAP that calculates 1^5 + 2^5 + 3^5+ ... + N^5
# for multiple values of N simultaneously using pool
# Measure total execution time

import multiprocessing
import time


def calculatePowerSum(n):
    powerSum = 0
    for i in range(1, n+1):
        powerSum = powerSum + (i ** 5)
    return powerSum


def main():
    Data = [1000000, 2000000, 3000000, 4000000]
    print("Input List : ",Data)

    Result = []

    pobj = multiprocessing.Pool()

    start_time = time.perf_counter()
    
    Result = pobj.map(calculatePowerSum, Data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print(f"\nResult is : {Result}")
    print(f"Total Execution time is : {end_time - start_time:.3f} seconds")

if __name__ == "__main__":
    main()

