# Design a Python application that create 2 seperate threads named Even & Odd
# Even thread should display first 10 even numbers
# Odd thread should display first 10 odd numbers 

import threading

def PrintNEven(No):
    evenList = []
    for i in range(2, No*2+1, 2):
        evenList.append(i)
    print("Even Numbers : ",evenList)

def PrintNOdd(No):
    oddList = []
    for i in range(1, No*2+1, 2):
        oddList.append(i)
    print("Odd Numbers : ",oddList)

def main():
    t1 = threading.Thread(target=PrintNEven, name="Even", args=(10,))
    t2 = threading.Thread(target=PrintNOdd, name="Odd", args=(10,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()