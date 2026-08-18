import pandas as pd
import matplotlib.pyplot as plt


border = "-" * 50
df = None

def CreateLineChart():
    global df

    # 1. Get X-axis labels (all column names except 'Name')
    Subjects = df.drop("Name", axis=1).columns.tolist()
    print("Subject names : ",Subjects)

    # 2. Get Y-axis values:
    # df[...]                     -> Bool expression finds Amit's row 
    # [Subjects]                  -> Picks the mark columns
    # .values[0]                  -> extract row 0 as plain list [85, 92, 75]
    Amit_Marks = df[df["Name"] == "Amit"][Subjects].values[0] 
    print("Amit Marks :", Amit_Marks)

    plt.figure(figsize=(8, 6))
    plt.plot(Subjects, Amit_Marks, label="Amit Subject Marks", marker="o", linestyle="-") 

    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.title("Marks of Amit")
    
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
    CreateLineChart()



if __name__ == "__main__":
    main()