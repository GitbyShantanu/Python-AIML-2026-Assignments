# WAP which Display first 10 even numbers on console.

def Display(No):
    for i in range(2, No*2+1, 2):
        print(i, end=" ")

def main():
    Display(10)

if __name__ == "__main__":
    main()  