# Write a lambda function using map() which accepts a list of numbers and returns a list with the square of each number.

squares = lambda no : no * no

def main():
    Data = [1, 2, 3, 4, 5]
    print("Data before Map: ", Data)
    
    mData = list(map(squares, Data))
    print("Data after Map: ",mData)

if __name__ == "__main__":
    main()