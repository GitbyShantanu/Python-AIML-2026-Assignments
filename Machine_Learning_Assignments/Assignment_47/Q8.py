import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = None
model = None

def PredictMarks():
    global df, model
    
    Y_pred = model.predict([[6]]) 
    print("Prediction for 6 Study Hours is : ", Y_pred[0], " Marks")
    

def MarvellousLinearRegression():
    global df, model

    # Seperate features and label
    X = df[["StudyHours"]]
    Y = df["Marks"]

    print("X shape : ", X.shape)
    print("Y shape : ", Y.shape)

    # Split data for training and testing
    X_train = X
    Y_train = Y 
    X_test = X[-3:]
    Y_test = Y[-3:]

    model = LinearRegression()
    model.fit(X_train, Y_train)
    Y_pred = model.predict(X_test)

    print("Expected : ", list(Y_test))
    print("Actual : ",Y_pred)

    print("\nCoefficient : ", model.coef_)
    print("intercept : ", model.intercept_)
    

def main():
    data = {
        "StudyHours" : [1,2,3,4,5],
        "Marks" : [50,55,60,65,70]
    }

    global df
    df = pd.DataFrame(data)
    print(df)

    MarvellousLinearRegression()
    PredictMarks()

if __name__ == "__main__":
    main()