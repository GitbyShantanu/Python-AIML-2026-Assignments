import pandas as pd 

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, precision_score, recall_score, f1_score

import matplotlib.pyplot as plt


border = "-"*70 
def PrintHeader(title):
    border = "="*70 
    print()
    print(border)
    print(title)
    print(border)   


def load_data(data_path):
    PrintHeader("Load Data") 
    df = pd.read_csv(data_path)
    print(f"{data_path} Dataset loaded successfully") 
    return df 


def display_data(df : pd.DataFrame):
    PrintHeader("Display Data") 
    
    print("First 5 records of dataset : ")
    print(df.head()) 
    print(border) 
    
    print("Shape of dataset : ", df.shape) 

    
def EDA(df : pd.DataFrame):
    PrintHeader("Exploratory Data Analysis") 

    print("Data types : ")
    print(df.dtypes) 
    print(border) 

    print("Statistical Summary : ")
    print(df.describe()) 
    print(border) 

    print("Correlation : ")
    print(df.corr(numeric_only=True)) 
    print(border) 

    print("Target Distribution : ")
    print(df["Default"].value_counts())


def clean_data(df : pd.DataFrame):
    PrintHeader("Clean Data")
    print("Missing values : ")
    print(df.isnull().sum()) 
    print(border) 

    print("Duplicate values : ")
    print(df.duplicated().sum()) 
    print(border) 

    df = df.drop_duplicates() 
    df = df.dropna() 
    print("No missing and duplicate values") 
    return df 


def encode_data(df : pd.DataFrame):
    PrintHeader("Encode Data") 
    df["PreviousDefault"] = df["PreviousDefault"].map({"Yes" : 1, "No" : 0}) 
    
    df = pd.get_dummies(df, columns=["HomeOwnership"], dtype=int)
    
    print("Data after encoding : ") 
    print(df.head()) 
    return df 


def seperate_target_features(df : pd.DataFrame):
    PrintHeader("Seperate Target and Features")
    
    X = df.drop("Default", axis=1) 
    Y = df["Default"]  

    print("Features : ", X.columns.tolist()) 
    print("Target : ", Y.name)  

    print("Features shape : ", X.shape) 
    print("Target shape : ", Y.shape)     
    return X, Y


def split_data(X, Y):
    PrintHeader("Split data for Training and Testing") 

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42, stratify=Y) 

    print("Training data shape : ", X_train.shape) 
    print("Testing data shape : ", X_test.shape) 

    print("Training labels shape : ", Y_train.shape) 
    print("Testing labels shape : ", Y_test.shape) 
    print(border) 

    print("Stratified split is used to keep the same proportion of target classes in train and test data.")
    return X_train, X_test, Y_train, Y_test


def scale_data(X_train, X_test):
    PrintHeader("Scale data")  

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)  
    X_test_scaled = scaler.transform(X_test) 

    print("Data after scaling : ") 
    print(X_train_scaled[:5]) 
    return X_train_scaled, X_test_scaled, scaler 


def build_mlp_model():
    PrintHeader("Build Model") 
    
    model = MLPClassifier(
        hidden_layer_sizes=(32, 16),
        activation='relu',
        solver='adam',
        max_iter=1000,
        random_state=42 
    )

    print(f"MLP Model : {model}") 
    return model 


def train_model(model : MLPClassifier, X_train, Y_train):
    PrintHeader("Train Model") 
    model.fit(X_train, Y_train) 
    print("Model trained successfully") 
    return model 


def evaluate_model(model : MLPClassifier, X_test, Y_test, X_train, Y_train):
    PrintHeader("Evaluate Model") 

    Y_pred_train = model.predict(X_train)
    Y_pred_test = model.predict(X_test) 

    train_accuracy = accuracy_score(Y_train, Y_pred_train) 
    test_accuracy = accuracy_score(Y_test, Y_pred_test) 

    print("Training Accuracy : ", train_accuracy) 
    print("Testing Accuracy : ", test_accuracy) 
    print(border) 

    print("Confusion Matrix : ")
    print(confusion_matrix(Y_test, Y_pred_test)) 
    print(border) 

    print("Classification Report : ")
    print(classification_report(Y_test, Y_pred_test)) 
    print(border) 

    print("Precision : ")
    print(precision_score(Y_test, Y_pred_test)) 
    print(border) 

    print("Recall : ")
    print(recall_score(Y_test, Y_pred_test)) 
    print(border) 

    print("F1 Score : ")
    print(f1_score(Y_test, Y_pred_test)) 
    print(border) 

    print("Model fitting : ")
    if train_accuracy > 0.90 and (train_accuracy - test_accuracy) > 0.10:
        print("Model is Overfitted")
    elif train_accuracy < 0.80 and test_accuracy < 0.80:
        print("Model is Underfitted")
    else:
        print("Model is best fitted") 

    return test_accuracy, train_accuracy


def plot_training_loss(model : MLPClassifier):
    plt.plot(model.loss_curve_, marker = "o", markerfacecolor="blue", color="red", linewidth=2, markersize=5) 
    plt.xlabel("Iterations")
    plt.ylabel("Loss")
    plt.title("MLP Training Loss")
    plt.grid(True)
    plt.show()


def predict_for_new_data(model, scaler, data):
    PrintHeader("Test on New Data")

    print("New Data : ") 
    print(data) 
    print(border) 
    
    data["PreviousDefault"] = data["PreviousDefault"].map({"Yes" : 1, "No" : 0}) 
    data = pd.get_dummies(data, columns=["HomeOwnership"], dtype=int)

    data = scaler.transform(data)
    Y_pred = model.predict(data) 

    print("Prediction for new data : ")
    print(Y_pred) 


def experiment_activation_function(X_train, Y_train, X_test, Y_test):
    PrintHeader("Experiment Activation Function")
    
    activations = [
        "identity", 
        "logistic", 
        "tanh", 
        "relu"
    ]

    for fn in activations: 
        model = MLPClassifier(
            hidden_layer_sizes=(32, 16),
            activation=fn,
            solver="adam",
            max_iter=2000,
            random_state=42 
        )
        model.fit(X_train, Y_train) 
        Y_pred = model.predict(X_test) 
        accuracy = accuracy_score(Y_test, Y_pred) 
        print(f"Activation Function : {fn}, Accuracy : {accuracy*100:.2f}%") 


def experiment_hidden_layers(X_train, Y_train, X_test, Y_test):
    PrintHeader("Experiment Hidden Layers")

    hidden_layers = [
        (10,),
        (20, 10),
        (50, 25),
        (100, 50, 25) 
    ]

    for layers in hidden_layers:
        model = MLPClassifier(
            hidden_layer_sizes=layers, 
            activation="relu", 
            solver="adam", 
            max_iter=2000, 
            random_state=42 
        )

        model.fit(X_train, Y_train) 
        Y_pred = model.predict(X_test) 
        accuracy = accuracy_score(Y_test, Y_pred) 
        print(f"Hidden Layers : {layers}, Accuracy : {accuracy*100:.2f}%") 


def experiment_learning_rate(X_train, Y_train, X_test, Y_test):
    PrintHeader("Experiment Learning Rate") 
    learning_rates = [0.001, 0.01, 0.1, 1.0]
    
    for lr in learning_rates:
        model = MLPClassifier(
            hidden_layer_sizes=(32, 16),
            activation="relu",
            solver="adam",
            learning_rate_init=lr,
            max_iter=2000,
            random_state=42
        )
        model.fit(X_train, Y_train)
        Y_pred = model.predict(X_test)
        accuracy = accuracy_score(Y_test, Y_pred)
        print(f"Learning Rate : {lr}, Accuracy : {accuracy*100:.2f}%") 


def Load_Defaulter_MLP(data_path):
    PrintHeader("Loan Defaulter Prediction Using MLP") 
    
    df = load_data(data_path) 
    EDA(df)
    df = clean_data(df) 
    df = encode_data(df) 

    X, Y = seperate_target_features(df) 
    X_train, X_test, Y_train, Y_test = split_data(X, Y) 
    X_train_scaled, X_test_scaled, scaler = scale_data(X_train, X_test) 

    model = build_mlp_model() 
    model = train_model(model, X_train_scaled, Y_train)
    train_accuracy, test_accuracy = evaluate_model(model, X_test_scaled, Y_test, X_train_scaled, Y_train)
    plot_training_loss(model) 

    new_data = pd.DataFrame({
    'Age': [27, 41, 35, 58, 30],
    'Income': [620000, 880000, 540000, 1350000, 410000],
    'LoanAmount': [350000, 550000, 800000, 450000, 950000],
    'CreditScore': [735, 790, 640, 820, 575],
    'EmploymentYears': [4, 12, 6, 22, 3],
    'ExistingLoans': [1, 1, 3, 0, 4],
    'MonthlyDebt': [14000, 18000, 32000, 10000, 42000],
    'LoanTerm': [36, 48, 60, 24, 60],
    'PreviousDefault': ['No', 'No', 'Yes', 'No', 'Yes'],
    'HomeOwnership': ['Rent', 'Mortgage', 'Rent', 'Own', 'Rent']
    })

    predict_for_new_data(model, scaler, new_data)

    experiment_activation_function(X_train_scaled, Y_train, X_test_scaled, Y_test)
    experiment_hidden_layers(X_train_scaled, Y_train, X_test_scaled, Y_test)
    experiment_learning_rate(X_train_scaled, Y_train, X_test_scaled, Y_test)


def main():
    Load_Defaulter_MLP("Loan_Default.csv")


if __name__ == "__main__":
    main()