from matplotlib import pyplot as plt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn.tree import plot_tree


Border = "-" * 50

df = None
X = None
Y = None

X_train = None
X_test = None
Y_train = None
Y_test = None

Y_pred = None

Model = DecisionTreeClassifier()
Accuracy = 0


def PrintHeader(title):
    print()
    print(Border)
    print(title)
    print(Border)


def LoadDataset():
    global df

    Datapath = "student_performance_ml.csv"
    df = pd.read_csv(Datapath)

    print("Dataset loaded successfully...")


def PrepareDataset():
    global X, Y

    PrintHeader("Preparing Dataset")

    # Separate input features and target variable
    FeatureCols = [
        "StudyHours",
        "PreviousScore",
        "Attendance",
        "SleepHours",
        "AssignmentsCompleted"
    ]

    X = df[FeatureCols]
    Y = df["FinalResult"]

    print("X shape : ", X.shape)
    print("Y shape : ", Y.shape)


def SplitDataset():
    global X_train, X_test, Y_train, Y_test

    PrintHeader("Splitting Dataset")

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )

    print("X_train shape: ", X_train.shape)
    print("X_test shape: ", X_test.shape)

    print("\nY_train shape: ", Y_train.shape)
    print("Y_test shape: ", Y_test.shape)


def TrainDecisionTree():
    PrintHeader("Training Decision Tree Classifier")

    Model.fit(X_train, Y_train)
    print("Decision Tree Classifier trained successfully...")


def PredictTestData():
    global Y_pred

    PrintHeader("Predicting Test Data...")

    Y_pred = Model.predict(X_test)

    print("Actual values : ")
    print(Y_test)

    print("Predicted values: ")
    print(Y_pred)

    print("\nPrediction completed successfully...")


def CalculateAccuracy():
    global Accuracy
    
    PrintHeader("Calculating Accuracy")

    Accuracy = accuracy_score(Y_test, Y_pred)
    print(f"Accuracy of Decision Tree Classifier: {Accuracy * 100:.2f}%")


def DisplayConfusionMatrix():
    PrintHeader("Confusion Matrix")

    cm = confusion_matrix(Y_test, Y_pred)
    print("Confusion Matrix : ")
    print(cm)

    print("True Positive  :", cm[1][1])
    print("True Negative  :", cm[0][0])
    print("False Positive :", cm[0][1])
    print("False Negative :", cm[1][0])


def DisplayFeatureImportance():
    PrintHeader("Feature Importance")

    Importance = Model.feature_importances_

    print("Feature Importance : ")
    print(f"StudyHours           : {Importance[0]:.2f}")
    print(f"PreviousScore        : {Importance[1]:.2f}")
    print(f"Attendance           : {Importance[2]:.2f}")
    print(f"SleepHours           : {Importance[3]:.2f}")
    print(f"AssignmentsCompleted : {Importance[4]:.2f}")

    print("Most important feature is : ", X.columns[Importance.argmax()])
    print("Least important feature is : ", X.columns[Importance.argmin()])


def RemoveSleepHours():
    global X
    global X_train, X_test, Y_train, Y_test
    global Y_pred
    global Model

    PrintHeader("Removing SleepHours")

    X_without_sleep = X
    X_without_sleep = X_without_sleep.drop(columns=["SleepHours"], axis=1) #axis: 0=rows, 1=cols

    X_train, X_test, Y_train, Y_test = train_test_split(
        X_without_sleep, 
        Y, 
        test_size=0.2, 
        random_state=42
    )

    Model = Model.fit(X_train, Y_train)
    Y_pred = Model.predict(X_test)
    NewAccuracy = accuracy_score(Y_test, Y_pred)

    print("New Features after removing SleepHours : ")
    print(list(X_without_sleep.columns))

    print(f"\nAccuracy before removing SleepHours : {Accuracy * 100:.2f}%")
    print(f"Accuracy after removing SleepHours : {NewAccuracy * 100:.2f}%")

    if NewAccuracy > Accuracy:
        print("Accuracy improved.")
    elif NewAccuracy < Accuracy:
        print("Accuracy decreased.")
    else:
        print("Accuracy remains the same.")


def TrainWithTwoFeatures():
    global X
    global X_train, X_test, Y_train, Y_test
    global Y_pred
    global Model
    global df 

    PrintHeader("Training with Two Features StudyHours and Attendance")

    X_two_features = df[["StudyHours", "Attendance"]]
    # print(X_two_features.head())

    X_train, X_test, Y_train, Y_test = train_test_split(
        X_two_features,
        Y,
        test_size=0.2,
        random_state=42
    )

    Model = Model.fit(X_train, Y_train)
    Y_pred = Model.predict(X_test)
    NewAccuracy = accuracy_score(Y_test, Y_pred)

    print(f"Accuracy with full dataset : {Accuracy * 100:.2f}%")
    print(f"Accuracy with only StudyHours and Attendance: {NewAccuracy * 100:.2f}%")

    if NewAccuracy > Accuracy:
        print("Model is performing better with two features.")
    elif NewAccuracy < Accuracy:
        print("Model is performing worse with two features.")
    else:
        print("Model is performing equally with two features.")


def CreateNewDataframe():
    global df
    global Model

    PrintHeader("Creating New Full Dataframe of 5 students")

    NewData = {
        "StudyHours": [2.5, 4.0, 5.5, 7.0, 8.5],
        "Attendance": [62, 72, 81, 90, 96]
    }

    NewStudents = pd.DataFrame(NewData)

    new_pred = Model.predict(NewStudents)
    NewStudents["FinalResult"] = new_pred

    print("Predictions for new students : ")
    print(NewStudents)
    print("(Note: 0 = Fail, 1 = Pass)")

def ManualAccuracyCalculation():
    global Y_test, Y_pred, Accuracy

    PrintHeader("Manual Accuracy Calculation")

    cm = confusion_matrix(Y_test, Y_pred)

    TP = cm[1][1]
    TN = cm[0][0]
    FP = cm[0][1]
    FN = cm[1][0]

    Total = TP + TN + FP + FN
    Correct = TP + TN
    manual_accuracy = Correct / Total

    print(f"True Positive  : {TP}")
    print(f"True Negative  : {TN}")
    print(f"False Positive : {FP}")
    print(f"False Negative : {FN}")

    print(f"\nTotal Samples  : {Total}")
    print(f"Correct Predictions : {Correct}")

    print(f"\nManual Accuracy : {manual_accuracy * 100:.2f}%")
    print(f"Sklearn Accuracy : {Accuracy * 100:.2f}%")

    if manual_accuracy == Accuracy:
        print("Manual accuracy matches sklearn accuracy.")
    else:
        print("Manual accuracy does not match sklearn accuracy.")


def DisplayMisMatchedPredictions():
    global Y_test, Y_pred
    PrintHeader("Miss-Classified Students")

    cnt = 0
    actual = list(Y_test)
    predicted = list(Y_pred)

    for i in range(len(actual)):
        if actual[i] != predicted[i]:
            print(f"Student {i+1}: Actual = {actual[i]}, Predicted = {predicted[i]}")
            cnt += 1

    print(f"\nTotal Miss-Classified Students : {cnt}")


def CompareRandomStates():
    PrintHeader("Comparing Random States")
    global X, Y

    states = [0, 10, 42]

    for state in states:
        X_train, X_test, Y_train, Y_test = train_test_split(
            X,
            Y,
            test_size=0.2,
            random_state=state
        )

        Model = DecisionTreeClassifier()
        Model = Model.fit(X_train, Y_train)
        Y_pred = Model.predict(X_test)
        accuracy = accuracy_score(Y_test, Y_pred)

        print(f"Random State: {state}, Accuracy: {accuracy * 100:.2f}%")
    print()


def DecisionTreeVisualization():
    PrintHeader("Decision Tree Visualization")

    plot_tree(Model, feature_names=X.columns, class_names=["Fail", "Pass"], filled=True)

    plt.title("Decision Tree Visualization")
    plt.show()

    Root = Model.tree_.feature[0]
    print("Root Feature :", X.columns[Root])
    print("Reason : It gives the best split.")    


def CreateColumnPerformanceIndex():
    global df
    global Y

    PrintHeader("Creating Performance Index Column")

    df["PerformanceIndex"] = (df["StudyHours"] * 2) + df["Attendance"]

    print("\nPerformance Index column created successfully.")
    print(df.head())

    FeatureCols = [
        "StudyHours",
        "PreviousScore",
        "Attendance",
        "SleepHours",
        "AssignmentsCompleted",
        "PerformanceIndex"
    ]

    X_new = df[FeatureCols]

    X_train, X_test, Y_train, Y_test = train_test_split(X_new, Y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier()

    model = model.fit(X_train, Y_train) 
    Y_pred = model.predict(X_test)
    accuracy = accuracy_score(Y_test, Y_pred)
    print(f"Accuracy with PerformanceIndex column: {accuracy * 100:.2f}%")


def TrainModelWithMaxDepth(max_depth):
    global X, Y

    PrintHeader(f"Training Decision Tree with max_depth={max_depth}")

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier(max_depth=max_depth)
    model = model.fit(X_train, Y_train)
    Y_pred = model.predict(X_test)
    accuracy = accuracy_score(Y_test, Y_pred)

    print(f"Accuracy with max_depth={max_depth}: {accuracy * 100:.2f}%\n")
    print("_" * 50)

def main():
    PrintHeader("Student Performance ML Case Study")

    LoadDataset()
    PrepareDataset()
    SplitDataset()
    TrainDecisionTree()
    PredictTestData()
    CalculateAccuracy()
    DisplayConfusionMatrix()

    # Assignment 40 questions
    DisplayFeatureImportance()
    RemoveSleepHours()
    TrainWithTwoFeatures()
    CreateNewDataframe()
    ManualAccuracyCalculation()
    DisplayMisMatchedPredictions()
    CompareRandomStates()
    DecisionTreeVisualization()
    CreateColumnPerformanceIndex()
    TrainModelWithMaxDepth(max_depth=None)


if __name__ == "__main__":
    main()