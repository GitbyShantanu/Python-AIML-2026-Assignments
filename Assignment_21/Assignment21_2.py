# Design Python app that creates 2 threads 
# Thread1 calculates and display maximum from the list
# Thread2 calculates and display minimum from the list

import threading as th


def maximum(Arr):
    maxi = Arr[0]
    for no in Arr:
        if no > maxi:
            maxi = no 
    print(f"Maximum element : {maxi}")


def minimum(Arr):
    mini = Arr[0]
    for no in Arr:
        if no < mini:
            mini = no 
    print(f"Maximum element : {mini}")


def main():
    size = int(input("List size: "))
    Data = []

    for i in range(size):
        no = int(input("Enter element: "))
        Data.append(no)

    # Data = [23, 13, 33, 12, 7, 60, 24, 50, 73]
    print("Input List: ",Data)

    t1 = th.Thread(target=maximum, name="Thread1", args=(Data,))
    t2 = th.Thread(target=minimum, name="Thread2", args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()