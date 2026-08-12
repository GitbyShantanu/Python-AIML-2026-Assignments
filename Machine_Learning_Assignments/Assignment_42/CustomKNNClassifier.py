import math
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

border = "-"*60

class KNNClassifier:
    def __init__(self, n_neighbors=5, show_steps=False):
        self.n_neighbors = n_neighbors
        self.X_train = None 
        self.Y_train = None
        self.show_steps = show_steps


    @staticmethod
    def EuclideanDistance(features, train_point, test_point):  #eg. (1,2), (3,3)
        # Ans = math.sqrt((P1['X'] - P2['X'])**2 + (P1['Y'] - P2['Y'])**2)
        # Ans = sqrt((X1 - X2)**2 + (Y1 - Y2)**2)
        
        distance = 0
        for f in features:  # ['X', 'Y']
            diff = train_point[f] - test_point[f] # (X1 - X2), (Y1 - Y2)
            sq = diff ** 2            # (X1 - X2)**2, (Y1 - Y2)**2
            distance = distance + sq  # dist=0 --> dist = ((dist + X.sq) + Y.sq))
        return math.sqrt(distance)
            
    
    def fit(self, X_train, Y_train):    
        self.X_train = X_train # Dataframe
        self.Y_train = Y_train # Series
        self.features = X_train.columns.tolist()  # ['X', 'Y'] for EUC_dist
        return self
    

    def predict(self, X_test):  # X_test = {X:3, Y:3}
        test_point = X_test
        X_train_records = self.X_train.to_dict(orient='records') # list of dict
        Y_train_list = self.Y_train.tolist()

        # Calculate distance from test_point to every training point
        distances = []
        for i in range(len(X_train_records)):
            dist = self.EuclideanDistance(self.features, X_train_records[i], test_point)
            distances.append((dist, Y_train_list[i]))

        if self.show_steps:
            print(border)
            print("Distances of all points : ")
            for d in distances:
                print(f"Distance : {d[0]:.2f}, Label : {d[1]}")
            print(border)

        # Sort by distance and pick top k nearest neighbors
        k = self.n_neighbors
        sorted_distances = sorted(distances, key=lambda x: x[0])
        nearest_distances = sorted_distances[:k]

        if self.show_steps:
            print(f"Sorted nearest k={k} distances : ")
            for d in nearest_distances:
                print(f"Distance : {d[0]:.2f}, Label : {d[1]}")
            print(border)

        # Voting - count freq of each label among k nearest neighbors. 
        votes = {}
        for d in nearest_distances:
            label = d[1]
            votes[label] = votes.get(label, 0) + 1

        if self.show_steps:
            print(f"Voting Result is : ")
            for label in votes:
                print(f"Name : {label}, Number of votes : {votes[label]}")
            print(border)

        # Label with highest votes is the result. 
        prediction = max(votes, key= votes.get)
        if self.show_steps:
            print(f"Final Predicted Class : {prediction}")

        return prediction


def main():
    def PrintHeader(title):
        print()
        print(border)
        print(title)
        print(border)

    PrintHeader("Custom KNN Classifier Algorithm")

    # 1. Load Dataset
    PrintHeader("Step 1 : Load Dataset")
    DataPath = "ColorPoints.csv"
    df = pd.read_csv(DataPath)
    print(f"{DataPath} Dataset is loaded successfully")

    # 2. Seperate Dependent and Independent variables 
    PrintHeader("Step 2 : Seperate Dependent and Independent variables")
    
    X = df.drop(columns=['label', 'point'])
    Y = df['label']

    print("X Shape : ", X.shape)
    print("Y Shape : ", Y.shape)
    print("Input Columns : ", X.columns.tolist())
    print("Output Columns : ", list(Y)) 
    print(border) 

    # 3. Split dataset for training and testing
    PrintHeader("Step 3 : Split dataset for training and testing")
    # X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)
    X_train = X[:4]
    X_test = X[4:]
    Y_train = Y[:4]
    Y_test = Y[4:]
    
    print("Details of training and testing data : ")
    print("X_train shape: ", X_train.shape)
    print("X_test shape: ", X_test.shape)
    print("Y_train shape: ", Y_train.shape)
    print("Y_test shape: ", Y_test.shape)
    print(border)

    # 4. Model Selection
    PrintHeader("Step 4 : Model Selection")
    model = KNNClassifier(n_neighbors=3, show_steps=True)
    print("KNN Classifier model selected Successfully")

    # 5. Train the model
    PrintHeader("Step 5 : Train the model")
    model.fit(X_train, Y_train)
    print("Model Trained Successfully")

    # 6. Test the model
    PrintHeader("Step 6 : Test the model")
    new_x = int(input("Enter X Co-ordinate for testing : "))
    new_y = int(input("Enter Y Co-ordinate for testing : "))
    new_point = {'X' : new_x, 'Y' : new_y}
    # new_point = {'X' : 3, 'Y' : 3}

    Y_pred = model.predict(X_test=new_point)
    print("Model Predicted Successfully")
    print(border)

if __name__ == "__main__":
    main()