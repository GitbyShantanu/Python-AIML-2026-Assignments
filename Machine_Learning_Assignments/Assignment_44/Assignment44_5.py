import pandas as pd

border = "-" * 50
df = None

def EditData(): #Replace pooja with puja 
    global df

    # Option A : Directly update the 'Name' column across the entire dataframe
    df["Name"] = df["Name"].replace("Pooja", "Puja")
    
    # Option B : df.loc[condition, column_to_change] = new_value
    # df.loc[(df["Name"] == "Pooja"), "Name"] = "Puja"

    # Manual way : avoid iterrows() whenever possible. 
    # work on whole columns directly rather than looping line by line. 
    # for index, row in df.iterrows():
    #     if row["Name"] == "Pooja": #index = 2
    #         df["Name"][index] = "Puja" # df['name] gives "Name" col as series, so Name[index=2] is the value "Pooja". 

    print(df)

            
def main():
    data = {
        "Name" : ["Amit", "Sagar", "Pooja"],
        "Math" : [85, 90, 78],
        "Science" : [92, 88, 95],
        "English" : [75, 85, 82]
    }    

    global df
    df = pd.DataFrame(data)
    EditData()

if __name__ == "__main__":
    main()