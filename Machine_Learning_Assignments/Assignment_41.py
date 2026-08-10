import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

df = None
X = None
Y = None

X_train = None
X_test = None
Y_train = None
Y_test = None

Y_pred = None

X_train_scaled = None
X_test_scaled = None

model = None
scaler = None

border = "-" * 50
def printHeader(title):
    print()
    print(border)
    print(title)
    print(border)


def LoadDataset(DataPath):
    printHeader("Step 1 : Load Dataset")
    global df
    df = pd.read_csv(DataPath)
    print("Dataset Loaded Successfully")


def CleanDataset():
    printHeader("Step 2 : Clean Dataset")
    global df
    df = df.dropna()  # Drop rows with missing values
    print("Dataset Cleaned Successfully")
    print("Shape of the dataset after cleaning: ", df.shape)


def PrepareData():
    printHeader("Step 3 : Prepare Data")
    global df, X, Y
    X = df.drop('Class', axis=1)
    Y = df['Class']
    print("X shape : ", X.shape)
    print("Y shape : ", Y.shape)


def SplitData():
    printHeader("Step 4 : Split Data")
    global X, Y
    global X_train, X_test, Y_train, Y_test

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5, random_state=42)
    print("X_train shape: ", X_train.shape)
    print("X_test shape: ", X_test.shape)
    print("Y_train shape: ", Y_train.shape)
    print("Y_test shape: ", Y_test.shape)
    

def ScaleData():
    printHeader("Step 5 : Scale Data")
    global X_train, X_test
    global X_train_scaled, X_test_scaled
    global scaler

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    print("Feature Scaling Done")


def ModelSelection():
    printHeader("Step 6 : Model Selection")
    global model
    model = KNeighborsClassifier(n_neighbors=9)
    print("KNN Classifier model selected Successfully")


def TrainModel():
    printHeader("Step 7 : Train Model")
    global model
    global X_train_scaled, Y_train

    model = model.fit(X_train_scaled, Y_train)
    print(f"{model} model Trained Successfully")


def TestModel():
    printHeader("Step 8 : Test Model")
    global model
    global X_test_scaled, Y_test, Y_pred

    Y_pred = model.predict(X_test_scaled)
    print("Model Predicted Successfully")


def CalculateAccuracy():
    printHeader("Step 9 : Calculate Accuracy")
    global Y_pred, Y_test
    accuracy = accuracy_score(Y_test, Y_pred)
    print(f"Accuracy : {accuracy * 100:.2f}%\n")


def WinePredictor(DataPath):
    printHeader("Wine Predictor")
    LoadDataset(DataPath)
    CleanDataset()
    PrepareData()
    SplitData()
    ScaleData()
    ModelSelection()
    TrainModel()
    TestModel()
    CalculateAccuracy()
    

def main():
    WinePredictor("WinePredictor.csv")


if __name__ == "__main__":
    main()