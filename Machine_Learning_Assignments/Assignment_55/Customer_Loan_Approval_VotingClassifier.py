import pandas as pd 
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, precision_score, recall_score, f1_score

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier


border = "-" * 70
def printHeader(title):
    border = "=" * 70
    print()
    print(border)
    print(title)
    print(border)


def load_Data(data_path):
    printHeader("Step 1 : Load Data") 
    df = pd.read_csv(data_path)
    print("First few records of dataset : ")
    print(df.head())
    return df 


def EDA(df : pd.DataFrame):
    printHeader("Step 2 : EDA") 
    print("Shape of dataset : ", df.shape)
    print(border)
    
    print("Column names : ")
    print(df.columns.to_list())
    print(border)
    
    print("Data Types : ")
    print(df.dtypes) 
    print(border) 
    
    print("Missing values : ")
    print(df.isnull().sum()) 
    print(border)

    print("Distribution of target Variable : ")
    print(df["LoanApproved"].value_counts()) 
    print(border)
   
    print("Correlation Matrix : ")
    corr = df.corr()["LoanApproved"].sort_values() 
    print(corr)
    print(border)

    print("Dataset Overview : ")
    print(df.describe()) 
    print(border)

    print("Duplicate values : ")
    print(df.duplicated().sum()) 
    print(border) 

    plt.figure(figsize=(10, 6))
    plt.bar(corr.index, corr.values)
    plt.title("Correlation Matrix")
    plt.xlabel("Features")
    plt.ylabel("Correlation")
    plt.xticks(rotation=45)
    plt.grid(True)
    # plt.show()

    
def seperate_Features_target(df):
    printHeader("Step 3 : Seperate Features and Target") 
    X = df.drop("LoanApproved", axis=1) 
    Y = df["LoanApproved"]
    print("X shape", X.shape)
    print("Y shape", Y.shape)
    return X , Y


def split_data(X, Y):
    printHeader("Step 4 : Split Data") 
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, 
        Y,
        test_size = 0.2,
        random_state = 42, 
    )
    print("X_train shape", X_train.shape)
    print("X_test shape", X_test.shape)
    print("Y_train shape", Y_train.shape)
    print("Y_test shape", Y_test.shape)
    return X_train, X_test, Y_train, Y_test 


def scale_data(X_train, X_test):
    printHeader("Step 5 : Scale Data") 
    scaler = StandardScaler() 
    X_train = scaler.fit_transform(X_train) 
    X_test = scaler.transform(X_test) 
    print("Features scaled successfully") 
    return X_train, X_test


def train_models(X_train, Y_train):
    base_model_lr = LogisticRegression(max_iter=1000)
    base_model_dt = DecisionTreeClassifier(random_state=42)
    base_model_knn = KNeighborsClassifier(n_neighbors=5) 

    base_model_lr.fit(X_train, Y_train) 
    base_model_dt.fit(X_train, Y_train) 
    base_model_knn.fit(X_train, Y_train) 
    return base_model_dt, base_model_lr, base_model_knn 


def evaluate_individual_model(model_lr, model_dt, model_knn, X_train, X_test, Y_train, Y_test):
    printHeader("Step 6 : Evaluate Individual Model") 
    Y_pred_train_lr = model_lr.predict(X_train) 
    Y_pred_test_lr = model_lr.predict(X_test) 
    
    Y_pred_train_dt = model_dt.predict(X_train) 
    Y_pred_test_dt = model_dt.predict(X_test) 

    Y_pred_train_knn = model_knn.predict(X_train) 
    Y_pred_test_knn = model_knn.predict(X_test) 

    print(f"Training accuracy LR: {accuracy_score(Y_train, Y_pred_train_lr) * 100:.2f}%") 
    print(f"Test accuracy LR: {accuracy_score(Y_test, Y_pred_test_lr) * 100:.2f}%")   
    print(border) 
    
    print(f"Training accuracy DT: {accuracy_score(Y_train, Y_pred_train_dt) * 100:.2f}%") 
    print(f"Test accuracy DT: {accuracy_score(Y_test, Y_pred_test_dt) * 100:.2f}%") 
    print(border)
    
    print(f"Training accuracy KNN: {accuracy_score(Y_train, Y_pred_train_knn) * 100:.2f}%") 
    print(f"Test accuracy KNN: {accuracy_score(Y_test, Y_pred_test_knn) * 100:.2f}%")     


def hard_voting_classifier(model_lr, model_dt, model_knn, X_train, X_test, Y_train, Y_test):
    printHeader("Step 7 : Hard Voting Classifier")
    model = VotingClassifier(
     estimators= [
        ("logistic", model_lr),
        ("decision_tree", model_dt),
        ("knn", model_knn)
     ],  
     voting= "hard"
    )
    
    model.fit(X_train, Y_train) 

    Y_pred_train = model.predict(X_train) 
    Y_pred_test = model.predict(X_test) 

    print(f"Training accuracy : {accuracy_score(Y_train, Y_pred_train) * 100:.2f}%") 
    print(f"Test accuracy : {accuracy_score(Y_test, Y_pred_test) * 100:.2f}%") 
    return model 


def soft_voting_classifier(model_lr, model_dt, model_knn, X_train, X_test, Y_train, Y_test):
    printHeader("Step 7 : Soft Voting Classifier")
    model = VotingClassifier(
     estimators= [
        ("logistic", model_lr),
        ("decision_tree", model_dt),
        ("knn", model_knn)
     ],  
     voting= "soft"
    )
    
    model.fit(X_train, Y_train) 

    Y_pred_train = model.predict(X_train) 
    Y_pred_test = model.predict(X_test) 

    print(f"Training accuracy : {accuracy_score(Y_train, Y_pred_train) * 100:.2f}%") 
    print(f"Test accuracy : {accuracy_score(Y_test, Y_pred_test) * 100:.2f}%") 
    return model 


def compare_all_model_accuracy(models, X_train, X_test, Y_train, Y_test):
    printHeader("Step 8 : Compare All Model Accuracy")
    accuracies = {} 
    
    for name, model in models:
        Y_pred = model.predict(X_test)
        accuracy = accuracy_score(Y_test, Y_pred) * 100 
        accuracies[name] = accuracy

    for name, accuracy in accuracies.items():
        print(f"{name} : {accuracy}")
    print(border) 

    max_accuracy_model = max(accuracies, key=accuracies.get)
    print(f"Best Model : {max_accuracy_model}")
    print(border) 


def main():
    printHeader("Loan Approval Prediction Using Voting Classifier")
    
    df = load_Data("Customer_Loan_Approval.csv")
    EDA(df) 

    X , Y = seperate_Features_target(df)
    X_train, X_test, Y_train, Y_test = split_data(X, Y) 
    X_train, X_test = scale_data(X_train, X_test)  
    
    lr, dt, knn = train_models(X_train, Y_train)
    evaluate_individual_model(lr, dt, knn, X_train, X_test, Y_train, Y_test)
    
    model_hard = hard_voting_classifier(lr, dt, knn, X_train, X_test, Y_train, Y_test)
    model_soft = soft_voting_classifier(lr, dt, knn, X_train, X_test, Y_train, Y_test)

    models = [
        ("Logistic Regression", lr),
        ("Decision Tree", dt),
        ("KNN", knn),
        ("Hard Voting Classifier", model_hard),
        ("Soft Voting Classifier", model_soft)
    ]
    
    compare_all_model_accuracy(models, X_train, X_test, Y_train, Y_test)
    
    
if __name__ == "__main__":
    main()