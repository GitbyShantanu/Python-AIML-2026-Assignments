import pandas as pd 

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier, AdaBoostClassifier, GradientBoostingClassifier, StackingClassifier, VotingClassifier 
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, f1_score, precision_score, recall_score


border = "-" * 70
def PrintHeader(title):
    border = "=" * 70
    print() 
    print(border)
    print(title)
    print(border)


def load_data(data_path):
    PrintHeader("Step 1 : Loading the dataset")
    df = pd.read_csv(data_path) 
    print("First few records : ")
    print(df.head()) 
    return df 


def EDA(df : pd.DataFrame):
    PrintHeader("Step 2 : EDA")
    print("Dataset shape : ", df.shape) 
    print(border) 

    print("Datatypes : ")
    print(df.dtypes)
    print(border)

    print("Describe statistics : ")
    print(df.describe()) 
    print(border) 
    
    print("Correlation Matrix : ")
    corr_matrix = df.corr()
    print(corr_matrix["Fraud"].sort_values(ascending=False)) 
    print(border) 


def clean_data(df): 
    PrintHeader("Step 4 : Cleaning the data") 
    print("Missing Values : ")
    print(df.isnull().sum()) 
    print(border) 
    
    print("Duplicate Values : ", df.duplicated().sum()) 
    

def seperate_features_target(df):
    PrintHeader("Step 3 : Seperating features and target")
    X = df.drop("Fraud", axis=1) 
    Y = df["Fraud"] 
    print("X shape : ", X.shape) 
    print("Y shape : ", Y.shape) 
    return X, Y 


def split_data(X, Y):
    PrintHeader("Step 5 : Splitting the data")
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, 
        Y, 
        test_size=0.3, 
        random_state=42
    ) 

    print("X_train shape : ", X_train.shape) 
    print("X_test shape : ", X_test.shape) 
    print("Y_train shape : ", Y_train.shape) 
    print("Y_test shape : ", Y_test.shape) 
    return X_train, X_test, Y_train, Y_test 


def build_models(X_train, X_test, Y_train, Y_test):
    PrintHeader("Step 6 : Build Unimodel and Ensemble Models") 
    
    model_dt = DecisionTreeClassifier(random_state=42) 

    model_bagging = BaggingClassifier(
        estimator=DecisionTreeClassifier(random_state=42),  
        n_estimators=10,
        random_state=42 
    )
    
    model_random_forest = RandomForestClassifier(
        n_estimators=10,
        random_state=42 
    )

    model_ada_boost = AdaBoostClassifier(
        n_estimators=10,
        random_state=42,
        learning_rate=1.0 
    )

    model_voting = VotingClassifier(
        estimators= [
            ("dt", model_dt),
            ("random_forest", model_random_forest),
            ("bagging", model_bagging) 
        ],
        voting="hard" 
    ) 

    models = [
        ("Decision Tree", model_dt),
        ("Bagging", model_bagging),
        ("Random Forest", model_random_forest),
        ("AdaBoost", model_ada_boost),
        ("Voting", model_voting) 
    ]

    for name, model in models:
        model.fit(X_train, Y_train) 

    print("All models build and trained successfully")
    return models


def evaluate_models(models, X_train, X_test, Y_train, Y_test):
    PrintHeader("Step 7 : Evaluating Models")

    result = [] 

    for name, model in models:
        Y_pred = model.predict(X_test) 
        accuracy = accuracy_score(Y_test, Y_pred) 
        precision = precision_score(Y_test, Y_pred) 
        recall = recall_score(Y_test, Y_pred) 
        f1 = f1_score(Y_test, Y_pred) 
        cm = confusion_matrix(Y_test, Y_pred) 
        cr = classification_report(Y_test, Y_pred) 
        result.append({
            "Name" : name,
            "Accuracy" : accuracy,
            "Precision" : precision,
            "Recall" : recall,
            "F1_Score" : f1,
            "Confusion Matrix" : cm,
        }) 
    
    for model in result: 
        print(f"Model : {model['Name']}")
        print(f"Accuracy : {model['Accuracy'] * 100:.2f}%") 
        print(f"Precision : {model['Precision']:.2f}") 
        print(f"Recall : {model['Recall']:.2f}") 
        print(f"F1_Score : {model['F1_Score']:.2f}") 
        print(f"Confusion Matrix : \n{model['Confusion Matrix']}") 
        print(border) 
    

def Fraudulent_Transaction_Detection_Ensemble(data_path):
    PrintHeader("Fraudulent Transaction Detection - Ensemble")
    df = load_data(data_path) 
    EDA(df) 
    clean_data(df) 
    X, Y = seperate_features_target(df) 
    X_train, X_test, Y_train, Y_test = split_data(X, Y) 
    models = build_models(X_train, X_test, Y_train, Y_test)
    evaluate_models(models, X_train, X_test, Y_train, Y_test)


def main():
    Fraudulent_Transaction_Detection_Ensemble("Fraudulent_Transaction_Detection.csv")


if __name__ == "__main__":
    main()