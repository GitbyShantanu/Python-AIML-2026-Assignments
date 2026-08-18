import pandas as pd

border = "-" * 50
df = None

def SortByTotalMarks():
    global df

    df["Total"] = df["Math"] + df["Science"] + df["English"]
    print("Dataset before sorting : ")
    print(df)
    print(border)

    df.sort_values("Total", ascending=False, inplace=True)

    print("Dataset after sorting by Total Marks : ")
    print(df)
    print(border)
            
def main():
    data = {
        "Name" : ["Amit", "Sagar", "Pooja"],
        "Math" : [85, 90, 78],
        "Science" : [92, 88, 95],
        "English" : [75, 85, 82]
    }    

    global df
    df = pd.DataFrame(data)
    SortByTotalMarks()


if __name__ == "__main__":
    main()