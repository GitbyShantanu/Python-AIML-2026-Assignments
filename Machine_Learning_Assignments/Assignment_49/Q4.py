import numpy as np
import math 
from sklearn.preprocessing import StandardScaler 


def main():
    dataset = [
        [25000, 25],
        [30000, 30],
        [35000, 55]
    ]

    p1 = dataset[0]
    p2 = dataset[1]

    print(f"Euclidean distance between {p1} and {p2} before feature scaling : {math.dist(p1, p2):.2f}")

    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(dataset)

    p1 = scaled_data[0]
    p2 = scaled_data[1]

    print(f"Euclidean distance after feature scaling is : {math.dist(p1,p2):.2f}")

if __name__ == "__main__":
    main()