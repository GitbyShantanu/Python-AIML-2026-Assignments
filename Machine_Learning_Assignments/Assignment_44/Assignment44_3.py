import pandas as pd

border = "-" * 50

def AddNewColumn(df):
    df["Total"] = df["Math"] + df["Science"] + df["English"]
    print(df)


def main():

    data = {
        "Name" : ["Amit", "Sagar", "Pooja"],
        "Math" : [85, 90, 78],
        "Science" : [92, 88, 95],
        "English" : [75, 85, 82]
    }    

    df = pd.DataFrame(data)
    AddNewColumn(df)

if __name__ == "__main__":
    main()