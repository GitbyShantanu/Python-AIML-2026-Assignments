import pandas as pd
import numpy as np

border = "-" * 50
df = None

def FillMissingWithMean():
    global df
    print("Original Dataset : ")
    print(df)

    mean_Math = df["Math"].mean()
    mean_Science = df["Science"].mean()

    df["Math"].fillna(mean_Math, inplace=True)
    df["Science"].fillna(value=mean_Science, inplace=True)

    print(df)

def main():
    data = {
        "Name" : ["Amit", "Sagar", "Pooja"],
        "Math" : [85, 90, 78],
        "Science" : [92, 88, 95],
        "English" : [75, 85, 82]
    }    

    data2 = {
        "Name" : ["Amit", "Sagar", "Pooja"],
        "Math" : [np.nan, 76, 88],
        "Science" : [91, np.nan, 85]
    }
    
    global df
    df = pd.DataFrame(data2)
    FillMissingWithMean()


if __name__ == "__main__":
    main()