# Design python app that creates 2 threads named Thread1 & Thread2
# Thread1 should display numbers from 1 to 50.
# Thread2 should display numbers from 50 to 1 in reverse order.
# Ensure Thread2 starts excecution after Thread1 has completed
# Use proper thread synchronization

import threading

def Display(n):
    print("Numbers from 1 to 50 : ")
    print(list(range(1, n+1)))
    

def DisplayRev(n):
    print("\nNumbers from 50 to 1 : ")
    print(list(range(n, 0, -1)))
    

def main():
    t1 = threading.Thread(target= Display, name="Thread1", args=(50,))
    t2 = threading.Thread(target= DisplayRev, name="Thread2", args=(50,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

if __name__ == "__main__":
    main()
