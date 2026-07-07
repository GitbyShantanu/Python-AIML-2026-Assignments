# Design a Python application that create 2 seperate threads named EvenFactor & OddFactor
# Both thread should accept one integer as parameter
# EvenFactor thread should identify all even factors of given no. Calculate and display sum of even factors.
# OddFactor thread should identify all odd factors of given no. Calculate and display sum of odd factors.

import threading

def EvenFactors(No):
    factors = []
    sum = 0
    for i in range(2, No + 1):
        if No % i == 0 and i % 2 == 0:
            factors.append(i)
            sum += i 

    print("Even Factors :", factors)
    print("Sum of even factors :", sum) 

def OddFactors(No):
    factors = []
    sum = 0
    for i in range(1, No + 1):
        if No % i == 0 and i % 2 != 0:
            factors.append(i)
            sum += i

    print("Odd Factors :", factors)
    print("Sum of odd factors :", sum)

def main():
    t1 = threading.Thread(target=EvenFactors, name="EvenFactors", args=(20,))
    t2 = threading.Thread(target=OddFactors, name="OddFactors", args=(30,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()