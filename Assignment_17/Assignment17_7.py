# WAP which accepts one number and displays below pattern
# Input: 5
# Output:
"""
1       2       3       4       5
1       2       3       4       5
1       2       3       4       5
1       2       3       4       5
1       2       3       4       5
"""

def Display(n):
    for i in range(n):
        for j in range(1, n+1):
            print(j, end="\t")
        print()

def main():
    val = int(input("Enter number: "))
    Display(val)
    
if __name__ == "__main__":
    main()