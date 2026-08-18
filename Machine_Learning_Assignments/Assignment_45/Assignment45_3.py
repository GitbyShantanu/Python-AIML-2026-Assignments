import pandas as pd
import numpy as np

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


def main():
    data = {
        "Name" : ["Amit", "Sagar", "Pooja"],
        "Math" : [85, 90, 78],
        "Science" : [92, 88, 95],
        "English" : [75, 85, 82]
    }    
    
    global df
    df = pd.DataFrame(data)
    MinMaxScaling()
    OneHotEncoding()
    GroupByGender()
    


if __name__ == "__main__":
    main()