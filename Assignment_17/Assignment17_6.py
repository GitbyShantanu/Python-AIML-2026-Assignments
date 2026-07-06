# WAP which accepts one number and displays below pattern
# Input: 5
# Output:
"""
*       *       *       *       *
*       *       *       *       
*       *       *       
*       *
*
"""

def Display(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end="\t")
        print()


def main():
    val = int(input("Enter number: "))
    Display(val)
    
if __name__ == "__main__":
    main()