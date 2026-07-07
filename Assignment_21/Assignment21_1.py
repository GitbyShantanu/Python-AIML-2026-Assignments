# Design Python app that creates 2 threads named Prime and NonPrime
# Both accept list of integers
# Prime thread display all prime numbers from the list
# NonPrime thread display all non-prime numbers from the list

import threading as th


def isPrime(no):
    for i in range(2, no//2+1):
        if no % i == 0:
            return False
    return True


def ChkPrime(arr):
    print("Prime Numbers:")
    for no in arr:
        if isPrime(no) == True:
            print(no, end=" ")
    print()


def ChkNonPrime(arr):
    print("Non Prime Numbers:")
    for no in arr:
        if isPrime(no) == False:
            print(no, end=" ")
    print()


def main():
    Data = [23, 13, 33, 12, 7, 60, 24, 50, 73]

    t1 = th.Thread(target=ChkPrime, name="Prime", args=(Data,))
    t2 = th.Thread(target=ChkNonPrime, name="NonPrime", args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()