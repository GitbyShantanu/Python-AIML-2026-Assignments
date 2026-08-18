import pandas as pd
import matplotlib.pyplot as plt


border = "-" * 50
df = None

def CreateBarPlot():
    global df

    df["Total"] = df["Math"] + df["Science"] + df["English"]

    plt.figure(figsize=(8, 6))
    plt.bar(df["Name"], df["Total"], width=0.5, label="Total Marks")

    plt.xlabel("Names of student")
    plt.ylabel("Total marks")
    plt.title("Total marks of students")
    
    plt.grid(True)
    plt.legend()
    plt.show()

            
def main():
    data = {
        "Name" : ["Amit", "Sagar", "Pooja"],
        "Math" : [85, 90, 78],
        "Science" : [92, 88, 95],
        "English" : [75, 85, 82]
    }    

    global df
    df = pd.DataFrame(data)
    CreateBarPlot()



if __name__ == "__main__":
    main()