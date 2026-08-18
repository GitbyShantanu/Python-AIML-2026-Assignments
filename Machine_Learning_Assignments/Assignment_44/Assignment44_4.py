import pandas as pd

border = "-" * 50
df = None

def Displaystudents(): # scores > 85 in science. 
    global df

    print("Students having Science marks > 85 : ")
    for index, row in df.iterrows():
        if row["Science"] > 85:
            print(row["Name"], row["Science"])


def main():
    data = {
        "Name" : ["Amit", "Sagar", "Pooja"],
        "Math" : [85, 90, 78],
        "Science" : [92, 88, 95],
        "English" : [75, 85, 82]
    }    

    global df
    df = pd.DataFrame(data)
    Displaystudents()

if __name__ == "__main__":
    main()