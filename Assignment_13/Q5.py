# WAP which accepts marks and display grades

def displayGrade(marks):
    if marks > 100 or marks < 0:
        print("Invalid marks")
        return 

    if marks >= 75:
        print("Distinction")
    elif marks >= 60:   
        print("First Class")
    elif marks >= 50:
        print("Second Class")
    else:
        print("Fail")

def main():
    marks = int(input("Enter marks: "))
    displayGrade(marks)

if __name__ == "__main__":
    main()