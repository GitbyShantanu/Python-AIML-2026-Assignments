# Write a lambda function using filter() which accepts a list of strings and returns a list of strings which have length greater than 5.

ChkLength = lambda str: len(str) > 5

def main(): 
    Data = ["Python", "Programming", "Assignment", "Lambda", "AI", "ML"]
    print("Data: ", Data)

    fData = list(filter(ChkLength, Data))   
    print("Data after filter: ", fData)  

if __name__ == "__main__":
    main()