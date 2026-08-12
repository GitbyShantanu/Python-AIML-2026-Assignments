from sklearn.model_selection import train_test_split

from CustomKNNClassifier import KNNClassifier
import pandas as pd

border = "-"*60

def main():
    # 1. Load Dataset
    DataPath = "ColorPoints.csv"
    df = pd.read_csv(DataPath)

    # 2. Seperate Dependent and Independent variables     
    X = df.drop(columns=['label', 'point'])
    Y = df['label']

    # 3. Split dataset for training and testing
    X_train = X
    Y_train = Y

    new_x = int(input("Enter X Co-ordinate for testing : "))
    new_y = int(input("Enter Y Co-ordinate for testing : "))
    new_point = {'X' : new_x, 'Y' : new_y}

    # 4. Hyper Parameter Tuning with different K values
    print(border)
    print("Hyper Parameter Tuning with different K values")
    print("Prediction Results : ")
    print(border)

    neighbors = [1,3,5]
    for k in neighbors:
        model = KNNClassifier(n_neighbors=k)
        model.fit(X_train, Y_train)

        Y_pred = model.predict(X_test=new_point)
        print(f"K = {k} -> {Y_pred}")

    print(border)

if __name__ == "__main__":
    main()