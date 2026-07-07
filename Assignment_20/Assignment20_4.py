# Design a Python application that creates 3 threads named Small, Capital and Digits. 
# All threads should accept a string as input
# Small thread should count and display no of lowercase characters. 
# Capital thread should count and display no of uppercase characters. 
# Digits thread should count and display no of numeric characters. 
# Each thread must also display: Thread ID, Thread Name.  

import threading


def CntSmall(s):
    t = threading.current_thread()
    print(f"Thread Name: {t.name}, Thread ID: {t.ident}")
    cnt = 0
    for ch in s:
        if ch >= 'a' and ch <= 'z':
            cnt += 1
    print(f"Count of small letters is : {cnt}")


def CntCapital(s):
    t = threading.current_thread()
    print(f"Thread Name: {t.name}, Thread ID: {t.ident}")
    cnt = 0
    for ch in s:
        if ch >= 'A' and ch <= 'Z':
            cnt += 1
    print(f"Count of Capital letters is : {cnt}")


def CntDigits(s):
    t = threading.current_thread()
    print(f"Thread Name: {t.name}, Thread ID: {t.ident}")
    cnt = 0
    for ch in s:
        if ch >= '0' and ch <= '9':
            cnt += 1
    print(f"Count of Digits is : {cnt}")


def main():
    name = input("Enter string: ")

    t1 = threading.Thread(target=CntSmall, name="Small", args=(name,))
    t2 = threading.Thread(target=CntCapital, name="Capital", args=(name,))
    t3 = threading.Thread(target=CntDigits, name="Digits", args=(name,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()