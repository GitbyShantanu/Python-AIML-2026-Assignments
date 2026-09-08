from sklearn.metrics import confusion_matrix
from sklearn.metrics import brier_score_loss
from numpy import dtype
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

border = "-"*70 
def PrintHeader(title):
    border = "="*70
    print()
    print(border)
    print(title)
    print(border)


def load_data(data_path: str) -> pd.DataFrame:
    df = pd.read_csv(data_path)
    return df


def display_data(df : pd.DataFrame):
    PrintHeader("Data Preview")

    print("First 5 records : ") 
    print(df.head()) 
    print(border) 

    print("Shape of dataset : ", df.shape) 

    print("Columns of dataset : \n", df.columns.to_list()) 
    print(border) 

    print("Missing Values : ")
    print(df.isnull().sum()) 
    print(border) 

    print("Duplicate data : ")
    print(df.duplicated().sum())    


def pre_process_data(df: pd.DataFrame):
    PrintHeader("Data Preprocessing")

    df['OverTime'] = df['OverTime'].map({'Yes': 1, 'No': 0})
    df['Attrition'] = df['Attrition'].map({'Yes': 1, 'No': 0})

    print("After Preprocessing")
    print(df.head())
    return df 


def seperate_features_labels(df):
    PrintHeader("Feature and Label Split")
    X = df.drop("Attrition", axis=1)
    Y = df["Attrition"]

    print("Shape of features : ", X.shape)
    print("Shape of labels : ", Y.shape) 
    print(border) 

    print("Features : \n", X.columns.to_list()) 
    print("Target : \n", Y.name)  

    return X, Y


def SplitData(X, Y):
    PrintHeader("Data Splitting")
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, 
        Y, 
        test_size=0.2, 
        random_state=2 
    )

    print("Shape of X_train : ", X_train.shape)
    print("Shape of X_test : ", X_test.shape)
    print("Shape of Y_train : ", Y_train.shape)
    print("Shape of y_test : ", Y_test.shape)
    
    return X_train, X_test, Y_train, Y_test


def ScaleData(X_train, X_test):
    PrintHeader("Data Scaling")
    
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    print("Data scaled successfully") 
    return X_train, X_test, scaler


def TrainModel(X_train, Y_train):
    PrintHeader("Model Training")

    model = MLPClassifier(
        hidden_layer_sizes=(10,5,3), 
        activation='tanh',
        solver='adam',
        learning_rate_init=0.01,
        max_iter=1000, 
        random_state=42
    )

    model.fit(X_train, Y_train)
    print("MLP Model trained successfully") 
    return model


def EvaluateModel(model, X_train, X_test, Y_train, Y_test): 
    PrintHeader("Model Evaluation") 
    Y_pred_train = model.predict(X_train)   
    Y_pred_test = model.predict(X_test)

    train_accuracy = accuracy_score(Y_train, Y_pred_train) 
    test_accuracy = accuracy_score(Y_test, Y_pred_test)

    print(f"Training Accuracy: {train_accuracy*100:.2f}%")
    print(f"Testing Accuracy: {test_accuracy*100:.2f}%")
    print(f"Number of Iterations: {model.n_iter_}")
    print("Confusion Matrix : \n", confusion_matrix(Y_test, Y_pred_test)) 

    return train_accuracy, test_accuracy


def DisplayLossCurve(model):
    plt.plot(model.loss_curve_, marker="o", color="red", linewidth=2, markersize=10, markerfacecolor="blue")
    plt.xlabel("Iterations")
    plt.ylabel("Loss")
    plt.title("MLP Loss Curve")
    plt.show()


def predict_attrition(emp_data, model : MLPClassifier, scaler : StandardScaler):
    PrintHeader("Predicting for new Data")    
    emp_data['OverTime'] = emp_data['OverTime'].map({'Yes': 1, 'No': 0})
    emp_data = scaler.fit_transform(emp_data)
    
    prediction = model.predict(emp_data)
    print("Prediction for new data : ", prediction)


def CheckFit(train_accuracy, test_accuracy):
    PrintHeader("Model Fitting")
    if train_accuracy > 0.90 and (train_accuracy - test_accuracy) > 0.10:
        print("Model is Overfitting")
    elif train_accuracy < 0.80 and test_accuracy < 0.80:
        print("Model is Underfitting")
    else:
        print("Model is best fitted")


def Employee_Attrition_MLP(data_path):
    PrintHeader("Employee Attrition using MLP Classifier")

    df = load_data(data_path) 
    display_data(df)

    df = pre_process_data(df)
    
    X, Y = seperate_features_labels(df)
    X_train, X_test, Y_train, Y_test = SplitData(X, Y)

    X_train, X_test, scaler = ScaleData(X_train, X_test)

    model = TrainModel(X_train, Y_train)

    train_accuracy, test_accuracy = EvaluateModel(
        model, X_train, X_test, Y_train, Y_test
    )

    DisplayLossCurve(model)

    new_data = pd.DataFrame({
    'Age': [29, 42, 31, 50, 26],
    'MonthlyIncome': [45000, 85000, 52000, 120000, 38000],
    'YearsAtCompany': [2, 10, 4, 15, 1],
    'TotalWorkingYears': [6, 18, 8, 25, 3],
    'DistanceFromHome': [12, 5, 30, 8, 45],
    'JobSatisfaction': [2, 4, 3, 4, 1],
    'WorkLifeBalance': [2, 4, 3, 3, 2],
    'OverTime': ['Yes', 'No', 'Yes', 'No', 'Yes'],
    'NumCompaniesWorked': [4, 2, 5, 1, 3],
    'TrainingTimesLastYear': [2, 5, 3, 4, 1]
    }) 

    predict_attrition(new_data, model, scaler)
    CheckFit(train_accuracy, test_accuracy)


def main():
    Employee_Attrition_MLP("Employee_Attrition.csv")


if __name__ == "__main__":
    main()

