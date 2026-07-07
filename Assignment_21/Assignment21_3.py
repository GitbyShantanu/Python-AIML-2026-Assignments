# Design Python app where multiple threads update a shared variable
# Use a lock to avoid race conditions.
# Each thread should increment the shared counter multiple times
# Display the final value of the counter after all threads complete execution

import threading 

counter = 0
lock = threading.Lock()


def increment_counter():
    global counter
    for _ in range(100):
        lock.acquire() # Acquire the lock
        counter += 1
        lock.release() # Release the lock


def main():
    t1 = threading.Thread(target=increment_counter, name="Thread1")
    t2 = threading.Thread(target=increment_counter, name="Thread2")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Final counter value:", counter)


if __name__ == "__main__":
    main()