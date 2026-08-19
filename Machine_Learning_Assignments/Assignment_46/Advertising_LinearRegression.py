import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, root_mean_squared_error, r2_score

border = "-" * 50

df = None

X = None
Y = None

X_train = None
X_test = None
Y_train = None
Y_test = None

model = None
Y_pred = None 

def PrintHeader(title):
    print(border)
    print(title)
    print(border)
    

def LoadData(Dataset):
    PrintHeader("Step 1 : Load the dataset")
    global df
    df = pd.read_csv(Dataset)
    print(df.head())


def CleanData():
    PrintHeader("Step 2 : Clean data")
    global df 
    if "Unnamed: 0" in df.columns:
        df = df.drop("Unnamed: 0", axis=1)
    print(df.head())

    print(border)
    print("Total Missing Values : ")
    print(df.isna().sum())


def SeperateData():
    PrintHeader("Step 3 : Seperate Independent and dependent variables")
    global df, X, Y 
    X = df.drop("sales", axis=1) 
    Y = df["sales"]   

    print("X : ",X.columns.tolist())
    print("Y : ", Y.name)
    print("Shape of X : ", X.shape)
    print("Shape of Y : ", Y.shape)


def SplitData():
    PrintHeader("Step 4 : Split features and labels into training and testing variables")
    global df
    global X, Y
    global X_train, X_test, Y_train, Y_test

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, 
        Y, 
        test_size=0.5, 
        random_state=42
    )

    print("Data splitted Successfully")
    print("X_train shape : ", X_train.shape)
    print("X_test shape : ", X_test.shape)
    print("Y_train shape : ", Y_train.shape)
    print("Y_test shape : ", Y_test.shape)


def TrainData():
    PrintHeader("Step 5 : Train the model")
    global df, model 
    global X_train, X_test, Y_train, Y_test
    model = LinearRegression() 
    print(f"{model} model created successfully")

    model = model.fit(X_train, Y_train)
    print("Model trained successfully")


def TestData():
    PrintHeader("Step 6 : Evaluate the model")
    global df, model 
    global X_test, Y_test, Y_pred

    Y_pred = model.predict(X_test)

    print("Expected Data : ")
    print(list(Y_test)[:10])

    print("\nPredicted Data : ")
    print([f"{x:.2f}" for x in Y_pred.tolist()[:10]]) 
    print(border)


def CalculateError():
    PrintHeader("Step 7 : Model Metrics")
    global model, Y_test, Y_pred

    print(f"Mean Squared Error (MSE) : {mean_squared_error(Y_test, Y_pred):.2f}")
    print(f"Root Mean Squared Error (RMSE) : {root_mean_squared_error(Y_test, Y_pred):.2f}")
    print(f"R2 Score : {r2_score(Y_test, Y_pred):.2f}")
    print(border)


def AdvertisingLinearRegression(Dataset):
    # Step 1 : Load dataset
    LoadData(Dataset)

    # Step 2 : Clean data 
    CleanData()

    # Step 3 : Seperate Independent and dependent variables
    SeperateData()

    # Step 4 : Split features and labels into training and testing variables
    SplitData()

    # Step 5 : Train the model
    TrainData()

    # Step 6 : Evaluate the model
    TestData()

    # Step 7 : Model Metrics
    CalculateError()


def main():
    AdvertisingLinearRegression("Advertising.csv")

if __name__ == "__main__":
    main()