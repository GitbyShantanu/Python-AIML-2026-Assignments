import numpy as np
from sklearn.preprocessing import StandardScaler 


def main():
    dataset = [
        [25000],
        [30000],
        [35000]
    ]

    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(dataset)

    print("Scaled Dataset is : ",scaled_data)

if __name__ == "__main__":
    main()