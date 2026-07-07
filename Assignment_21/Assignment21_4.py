# Design Python app that creates 2 threads 
# Thread1 calculates sum of elements from the list
# Thread2 calculates products from the list

import threading as th


def Addition(Arr):
    total = 0
    for no in Arr:
        total += no
    print("Sum is :",total)

def Multiplication(Arr):
    prod = 1
    for no in Arr:
        prod *= no
    print("Product is :",prod)


def main():
    Data = [13, 10, 3, 12]
    print("Input List: ",Data)

    t1 = th.Thread(target=Addition, name="Thread1", args=(Data,))
    t2 = th.Thread(target=Multiplication, name="Thread2", args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main() 