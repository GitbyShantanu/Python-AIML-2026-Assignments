import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

border = "-" * 60

df = None
X = None
Y = None

X_train = None
X_test = None
Y_train = None
Y_test = None

Model = None 
Y_pred = None
Accuracy = 0


def LoadDataSet(DataPath):
    PrintHeader("Step 1 : Load Dataset")
    global df

    df = pd.read_csv(DataPath)
    print("Dataset Loaded Successfully")

    print("First 5 records :")
    print(df.head(5))
    print(border)

    print("Last 5 records :")
    print(df.tail(5))
    print(border)

    print("Shape of dataset : ", df.shape)
    print(border)


def CleanDataset():
    PrintHeader("Step 2 : Clean Dataset")
    global df

    # Remove the extra unnamed index column
    df.drop("Unnamed: 0", axis=1, inplace=True)
    print("Dataset Cleaned Successfully")
    print("Shape of the dataset after cleaning: ", df.shape)


def FeaturesLabelsEncoding():
    PrintHeader("Step 3 : Features and Labels Encoding")
    global df
    
    LE = LabelEncoder()

    df['Wether_Encoded'] = LE.fit_transform(df['Wether'])
    df['Temperature_Encoded'] = LE.fit_transform(df['Temperature'])
    df['Play_Encoded'] = LE.fit_transform(df['Play'])

    # Weather: Overcast=0, Rainy=1, Sunny=2
    # Temperature: Cool=0, Hot=1, Mild=2
    # Play: No=0, Yes=1
    print("DataSet after encoding : ")
    print(df.head())
    print(border)


def PrepareData():
    PrintHeader("Step 4 : Features and Label seperation")
    global df, X, Y

    X = df[['Wether_Encoded', 'Temperature_Encoded']]
    Y = df['Play_Encoded']

    print("Features : ", X.columns.tolist())
    print("Target : ", Y.name)

    print("\nShape of X : ", X.shape)
    print("Shape of Y : ", Y.shape)
    print(border)


def SplitData():
    PrintHeader("Step 5 : Split Data for Training and Testing")
    global X, Y
    global X_train, X_test, Y_train, Y_test

    X_train = X # Give all dataset to training
    Y_train = Y 

    X_test = X[-5:] # last 5 items from X. 
    Y_test = Y[-5:] # last 5 items from Y.

    print("X_train shape: ", X_train.shape)
    print("X_test shape: ", X_test.shape)
    print("Y_train shape: ", Y_train.shape)
    print("Y_test shape: ", Y_test.shape)


def ModelSelection(k=5):
    PrintHeader("Step 6 : Model Selection")
    global Model

    Model = KNeighborsClassifier(n_neighbors=k)
    print(f"{Model} model selected Successfully")
    print(border)


def TrainModel():
    PrintHeader("Step 7 : Train Model")
    global Model, X_train, Y_train

    Model = Model.fit(X_train, Y_train)
    print(f"{Model} model Trained Successfully")


def TestModel():
    PrintHeader("Step 8 : Test Model")
    global Model, X_test, Y_test, Y_pred, Y_test

    Y_pred = Model.predict(X_test)
    print("Model Predicted Successfully")

    print("Actual Result : ", Y_test.values)
    print("Prediction Result : ", Y_pred)
    print(border)


def CheckAccuracy():
    PrintHeader("Step 9 : Check Accuracy")
    global X, Y

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5, random_state=42)
    print("X_train shape: ", X_train.shape)
    print("X_test shape: ", X_test.shape)
    print("Y_train shape: ", Y_train.shape)
    print("Y_test shape: ", Y_test.shape)
    print()

    k_values = range(1, 20, 2)
    for k in k_values:
        model = KNeighborsClassifier(n_neighbors=k)
        model = model.fit(X_train, Y_train)
        Y_pred = model.predict(X_test)
        accuracy = accuracy_score(Y_test, Y_pred)
        print(f"Accuracy for model with k = {k} is : {accuracy * 100:.2f}%")
    print(border)


def KNNPlayPredictor(DataPath):
    LoadDataSet(DataPath)
    CleanDataset()
    FeaturesLabelsEncoding() 
    PrepareData()
    SplitData()
    ModelSelection(k=3)
    TrainModel()
    TestModel()
    CheckAccuracy()


def PrintHeader(title):
    print()
    print(border)
    print(title)
    print(border)

def main():
    PrintHeader("Marvellous Infosystems Play Predictor Case Study")
    KNNPlayPredictor("MarvellousInfosystems_PlayPredictor.csv")

    
if __name__ == "__main__":
    main()