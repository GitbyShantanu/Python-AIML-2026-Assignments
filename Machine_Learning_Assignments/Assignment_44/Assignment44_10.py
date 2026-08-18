import pandas as pd
import numpy as np

border = "-" * 50
df = None

def DropColumn():
    global df
    print("Original Dataset : ")
    print(df)
    print(border)

    df = df.drop("English", axis=1)
    print("Dataset after dropping 'English' column : ")
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
    DropColumn()
    
if __name__ == "__main__":
    main()