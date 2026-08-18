import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


border = "-" * 50
df = None

# Normalise 'Math' scores using min - max scaling
def MinMaxScaling():
    global df

    # Min - Max Scaling
    df["Scaled_Math"] = (df["Math"] - df["Math"].min()) / (df["Math"].max() - df["Math"].min())
    print("Dataset after Min - Max Scaling of 'Math' column : ")
    print(df)
    
    print(border)


# Create 'Gender' col and perform one hot encoding on it
def OneHotEncoding():
    global df

    df["Gender"] = ["Male", "Male", "Female"]
    print("Dataset after adding 'Gender' column : ")
    print(df)
    print(border)

    # One Hot Encoding
    df = pd.get_dummies(df, columns=["Gender"], dtype=int, drop_first=True)
    print("Dataset after One Hot Encoding of 'Gender' columns : ")
    print(df)
    print(border)


# Group students by 'Gender' and calculate average marks. 
def GroupByGender():
    global df

    # Group by 'Gender' and calculate average marks
    grouped = df.groupby("Gender_Male").mean(numeric_only=True)
    print("Average marks by gender : ")
    print(grouped[["Math", "Science", "English"]])
    print(border)


# Plot a pie chart of marks for "Sagar"
def PlotPieChart():
    global df

    print("Marks of Sagar : ")
    stud_name = "Sagar"
    subjects = ["Math", "Science", "English"]

    Sagar_marks = df[(df["Name"] == stud_name)][subjects].values[0]
    print(Sagar_marks)

    plt.figure(figsize=(6, 6))
    plt.pie(
        Sagar_marks, 
        labels=subjects, 
        colors=['r', 'b', 'g'],
        autopct='%1.1f%%'
    )

    plt.title("Marks of Sagar")
    plt.legend()
    plt.show()
    print(border)

def AddNewColumn():
    global df

    df["Total"] = df["Math"] + df["Science"] + df["English"]
    print("Dataset after adding 'Total' columns : ")
    print(df)
    print(border)

    df["Status"] = ["Pass" if m >= 250 else "Fail" for m in df["Total"]]
    print("Dataset after adding 'Status' columns : ")
    print(df)
    print(border)

def CountStatus():
    global df
    count = 0
    for std in df["Status"]:
        if std == "Pass":
            count += 1
    return count


def ExportDataframe():
    global df
    df.to_csv("StudentDataSet.csv")
    print("Data exported successfully to CSV")
    print(border)


def PlotHistogramMath():
    global df

    plt.hist(x=df["Math"], label="Math Marks")
    plt.xlabel("Math Marks")
    plt.ylabel("Frequency")
    plt.legend()
    plt.show()
    print(border)


def RenameMathsColumn():
    global df

    df.rename(columns={"Math" : "Mathematics"}, inplace=True)
    print("Dataset after renaming 'Math' Column : ")
    print(df)
    print(border)


def main():
    data = {
        "Name" : ["Amit", "Sagar", "Pooja"],
        "Math" : [85, 90, 78],
        "Science" : [92, 88, 95],
        "English" : [65, 85, 82]
    }    
    
    global df
    df = pd.DataFrame(data)  
    MinMaxScaling()
    OneHotEncoding()
    GroupByGender()
    PlotPieChart()   
    AddNewColumn()

    count = CountStatus()
    print("Count of passed student is : ", count, "out of 3")
    print(border)

    ExportDataframe()
    PlotHistogramMath()
    RenameMathsColumn()

if __name__ == "__main__":
    main()