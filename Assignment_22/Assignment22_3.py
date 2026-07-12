# For every number in given list:
# count how many prime numbers exist between 1 to N using multiprocessing Pool
# Display total prime count for each number

import multiprocessing
import os


def ChkPrime(no):
    if no < 2:
        return False
    
    for i in range(2, no//2+1):
        if no % i == 0:
            return False
    return True


def countPrime(n):
    cnt = 0
    for i in range(1, n+1):
        if ChkPrime(i) == True: 
            cnt = cnt + 1

    print(f"Total prime count from 1 to {n} is : {cnt}")
    return cnt


def main():
    Data = [10000, 20000, 30000, 40000]
    print("Input List : ",Data)

    Result = []

    pobj = multiprocessing.Pool()
    Result = pobj.map(countPrime, Data)

    pobj.close()
    pobj.join()

    print(f"\nResult is : {Result}")

if __name__ == "__main__":
    main()

