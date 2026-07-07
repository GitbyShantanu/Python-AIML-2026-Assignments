# Design a Python application that create 2 seperate threads named EvenList & OddList
# Both should accept list of integers as input
# EvenList thread should extract even elements from list, Calculate and display their sum.
# OddList thread should extract odd elements from list, Calculate and display their sum.
# Threads should run concurrently

import threading

def ChkEven(Arr):
    evenList = []
    total = 0
    for no in Arr:
        if no % 2 == 0:
            evenList.append(no)
            total += no
    print("Even numbers: ",evenList)
    print("Sum of even numbers: ",total)


def ChkOdd(Arr):
    oddList = []
    total = 0
    for no in Arr:
        if no % 2 != 0:
            oddList.append(no)
            total += no
    print("Odd numbers: ",oddList)
    print("Sum of odd numbers: ",total)


def main():
    Data = [4,31,33,76,68]
    print("Input List : ",Data)

    t1 = threading.Thread(target=ChkEven, name="EvenList", args=(Data,))
    t2 = threading.Thread(target=ChkOdd, name="OddList", args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()