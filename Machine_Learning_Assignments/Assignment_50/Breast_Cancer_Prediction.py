import pandas as pd 
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, precision_score, recall_score, f1_score

from sklearn.ensemble import VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier


border = "-" * 70
def printHeader(title):
    border = "=" * 70
    print()
    print(border)
    print(title)
    print(border)


def load_Data():
    printHeader("Step 1 : Load Data") 
    dataset = load_breast_cancer()
    df = pd.DataFrame(data=dataset.data, columns=dataset.feature_names) 
    df["target"] = dataset.target
    print(df.head())
    return df


def EDA(df : pd.DataFrame):
    printHeader("Step 2 : Exploratory Data Analysis")

    print("Shape : ", df.shape)
    print(border)

    print("\nData types : ")
    print(df.dtypes)
    print(border)

    print("\nMissing values : ")
    print(df.isnull().sum())
    print(border)

    print("\nUnique Values : ")
    print(df.nunique())
    print(border)

    print("\nDuplicate Values : ")
    print(df.duplicated().sum())
    print(border)

    print("\nStatistics : ")
    print(df.describe())
    print(border)

    print("\nTarget distribution : ")
    print(df["target"].value_counts())
    print(border)

    print("\nCorrelation matrix : ")
    correlations = df.corr()
    print(correlations["target"].sort_values(ascending=False))
    print(border)

    plt.hist(df["target"], bins=2, color="purple", edgecolor = "black", label="Target") 
    plt.xlabel("Target")
    plt.ylabel("Frequency")
    plt.title("Target Distribution")
    plt.legend() 
    plt.show()


def seperate_Features_target(df):
    printHeader("Step 3 : Seperate Features and Target") 
    X = df.drop("target", axis=1) 
    Y = df["target"]
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
    print("Data scaled successfully")
    return X_train, X_test


def train_model(X_train, Y_train):
    printHeader("Step 6 : Train Model") 
    
    dt = DecisionTreeClassifier()
    lr = LogisticRegression(max_iter=1000)
    knn = KNeighborsClassifier(n_neighbors=5)

    dt.fit(X_train, Y_train)
    lr.fit(X_train, Y_train)
    knn.fit(X_train, Y_train) 

    model = VotingClassifier(
        estimators= [
            ("Decision Tree", dt),
            ("Logistic Regression", lr),
            ("KNN", knn)
        ],
        voting="hard"
    )

    model = model.fit(X_train, Y_train) 
    print("All models trained successfully") 
    return dt, lr, knn, model


def evaluate_model(model, X_test, Y_test, X_train, Y_train):
    printHeader("Step 7 : Evaluate Model")
    Y_pred_train = model.predict(X_train) 
    Y_pred_test = model.predict(X_test) 
    
    training_accuracy = accuracy_score(Y_train, Y_pred_train)
    test_accuracy = accuracy_score(Y_test, Y_pred_test)
    
    print(f"Training Accuracy : {training_accuracy * 100:.2f}%")
    print(f"Test Accuracy : {test_accuracy * 100:.2f}%")
    print(border)
    
    print("Confusion Matrix : ")
    cm = confusion_matrix(Y_test, Y_pred_test)    
    print(cm) 
    print(border)
    
    plt.matshow(cm)
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

    print(f"Precision : {precision_score(Y_test, Y_pred_test):.2f}")
    print(f"Recall : {recall_score(Y_test, Y_pred_test):.2f}")
    print(f"F1 Score : {f1_score(Y_test, Y_pred_test):.2f}")
    print(border)     
    
    print("Classification Report : ")
    print(classification_report(Y_test, Y_pred_test))
    print(border)

    print(f"{model.__class__.__name__} model evaluated successfully") 
    print(border)


def compare_models(models, X_test, Y_test, X_train, Y_train):
    printHeader("Step 8 : Compare Models")
    vote = {} 
    print("Accuracy : ")
    for name, model in models:
        Y_pred = model.predict(X_test) 
        accuracy = accuracy_score(Y_test, Y_pred)  
        print(f"{name} : {accuracy * 100:.2f}%") 
        vote[name] = accuracy   
    print(border)

    best_model = max(vote, key=vote.get)
    print(f"Best Model : {best_model}")
    print(f"Best Accuracy : {vote[best_model] * 100:.2f}%")
    print(border)
    return best_model


def main():
    printHeader("Breast Cancer Prediction")
    df = load_Data() 
    EDA(df) 
    X, Y = seperate_Features_target(df) 
    X_train, X_test, Y_train, Y_test = split_data(X, Y)
    X_train, X_test = scale_data(X_train, X_test)
    dt, lr, knn, model = train_model(X_train, Y_train) 
    
    models = [
        ("Decision Tree", dt),
        ("Logistic Regression", lr),
        ("KNN", knn),
        ("Voting", model)
    ]
    
    evaluate_model(model, X_test, Y_test, X_train, Y_train) 
    best_model = compare_models(models, X_test, Y_test, X_train, Y_train)    

if __name__ == "__main__":
    main()