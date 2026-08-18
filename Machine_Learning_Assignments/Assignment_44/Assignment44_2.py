import pandas as pd

border = "-" * 50

def DisplayDatasetStatistics(df):
    print("Dataset statistics : ")
    print(df.describe())
    print(border)


def main():

    data = {
        "Name" : ["Amit", "Sagar", "Pooja"],
        "Math" : [85, 90, 78],
        "Science" : [92, 88, 95],
        "English" : [75, 85, 82]
    }    

    df = pd.DataFrame(data)
    DisplayDatasetStatistics(df)

if __name__ == "__main__":
    main()