# WAP which accepts 1 no and display below pattern
# Input: 5
# Output:
"""
*       *       *       *       *
*       *       *       *       *
*       *       *       *       *
*       *       *       *       *
*       *       *       *       *
"""

def Display(n):
    for i in range(n):
        for j in range(n):
            print("*", end="\t")
        print()

def main():
    val = int(input("Enter number: "))

    Display(val)

if __name__ == "__main__":
    main()