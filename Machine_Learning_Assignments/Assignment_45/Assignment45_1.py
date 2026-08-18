import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

border = "-" * 50
df = None

# Normalise 'Math' scores using min - max scaling
def MinMaxScaling():
    global df
    print("Original Dataset : ")
    print(df)
    print(border)

    # Min - Max Scaling
    df["Scaled_Math"] = (df["Math"] - df["Math"].min()) / (df["Math"].max() - df["Math"].min())
    print("Dataset after Min - Max Scaling of 'Math' column : ")
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
    MinMaxScaling()
    
if __name__ == "__main__":
    main()