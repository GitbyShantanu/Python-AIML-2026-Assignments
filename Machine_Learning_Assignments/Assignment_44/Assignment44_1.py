import pandas as pd

border = "-" * 50

def DisplayDataset(df):
    print("Dataset : ")
    print(df)
    print(border)

    print("Shape of dataset : ", df.shape)
    print("Columns of dataset : ", df.columns.tolist())
    print("Datatype of dataset : ")
    print(df.dtypes)
    print(border)

def main():

    data = {
        "Name" : ["Amit", "Sagar", "Pooja"],
        "Math" : [85, 90, 78],
        "Science" : [92, 88, 95],
        "English" : [75, 85, 82]
    }    

    df = pd.DataFrame(data)

    DisplayDataset(df)


if __name__ == "__main__":
    main()