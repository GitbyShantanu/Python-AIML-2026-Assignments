from matplotlib import pyplot as plt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

from Assignment_38 import *

Border = "-" * 50

def PrintHeader(title):
    print()
    print(Border)
    print(title)
    print(Border)


def LoadDataset():
    Datapath = "student_performance_ml.csv"
    df = pd.read_csv(Datapath)
    print("Dataset loaded successfully...")
    return df


def DisplayBasicInformation(df):
    PrintHeader("Basic Information about Dataset")

    print("First 5 Records:")
    print(df.head())
    print("\nLast 5 Records:")
    print(df.tail())

    print("\nDataset Shape :", df.shape)

    print("\nColumn Names :")
    print(list(df.columns))

    print("\nData Types :")
    print(df.dtypes)


def PrepareDataset(df):
    PrintHeader("Preparing Dataset")

    # Seperate input features and target variable
    feature_cols = [
        "StudyHours",
        "PreviousScore",
        "Attendance",
        "SleepHours",
        "AssignmentsCompleted"
    ]

    X = df[feature_cols]
    Y = df["FinalResult"]

    print("X shape : ", X.shape)
    print("Y shape : ", Y.shape) 

    return X, Y


def SplitDataset(X, Y): 
    PrintHeader("Splitting Dataset")

    X_train, X_test, Y_train, Y_test= train_test_split(X, Y, test_size=0.2, random_state=42)
    
    print("X_train shape: ", X_train.shape)
    print("X_test shape: ", X_test.shape)

    print("\nY_train shape: ", Y_train.shape)
    print("Y_test shape: ", Y_test.shape)

    return X_train, X_test, Y_train, Y_test


def TrainDecisionTree(X_train, Y_train):
    PrintHeader("Training Decision Tree Classifier")

    Model = DecisionTreeClassifier(random_state=42)
    Model = Model.fit(X_train, Y_train)

    print("Decision Tree Classifier trained successfully...")
    return Model


def PredictTestData(Model, X_test, Y_test):
    PrintHeader("Predicting Test Data...")

    Y_pred = Model.predict(X_test)

    print("Actual values : ")
    print(Y_test)

    print("Predicted values: ")
    print(Y_pred)
    
    print("\nPrediction completed successfully...") 
    return Y_pred


def CalculateAccuracy(Y_test, Y_pred):
    PrintHeader("Calculating Accuracy")

    Accuracy = accuracy_score(Y_test, Y_pred)
    print(f"Accuracy of Decision Tree Classifier: {Accuracy * 100:.2f}%")
    return Accuracy


def DisplayConfusionMatrix(Y_test, y_pred):
    PrintHeader("Confusion Matrix")

    cm = confusion_matrix(Y_test, y_pred)
    print("Confusion Matrix : ")
    print(cm)

    display = ConfusionMatrixDisplay(cm)
    display.plot()
    
    plt.title("Confusion Matrix")
    plt.show()

    print("True Positive  :", cm[1][1])
    print("True Negative  :", cm[0][0])
    print("False Positive :", cm[0][1])
    print("False Negative :", cm[1][0])


def CompareDecisionTrees(X_train, X_test, Y_train, Y_test):
    PrintHeader("Compare Decision Tree Models with Different max_depth Values")

    Model1 = DecisionTreeClassifier(max_depth=1)
    Model1.fit(X_train, Y_train)
    Y_pred1 = Model1.predict(X_test)
    Accuracy1 = accuracy_score(Y_test, Y_pred1)

    Model2 = DecisionTreeClassifier(max_depth=3)
    Model2.fit(X_train, Y_train)
    Y_pred2 = Model2.predict(X_test)
    Accuracy2 = accuracy_score(Y_test, Y_pred2)

    Model3 = DecisionTreeClassifier(max_depth=None)
    Model3.fit(X_train, Y_train)
    Y_pred3 = Model3.predict(X_test)
    Accuracy3 = accuracy_score(Y_test, Y_pred3)

    print(f"Accuracy (max_depth = 1)    : {Accuracy1 * 100} %")
    print(f"Accuracy (max_depth = 3)    : {Accuracy2 * 100} %")
    print(f"Accuracy (max_depth = None) : {Accuracy3 * 100} %")
    print("""
Observation:
1. Different max_depth values produce different accuracies.
2. A very small depth may underfit the dataset.
3. A very large depth may overfit the dataset.
4. Choose the model with the best testing accuracy.
""")


def CompareTrainingTestingAccuracy(Model, X_train, X_test, Y_train, Y_test):
    PrintHeader("Model Accuracy")

    Y_train_pred = Model.predict(X_train)
    Y_test_pred = Model.predict(X_test)

    TrainingAccuracy = accuracy_score(Y_train, Y_train_pred)
    TestingAccuracy = accuracy_score(Y_test, Y_test_pred)

    print(f"Training Accuracy : {TrainingAccuracy * 100:.2f}%")
    print(f"Testing Accuracy  : {TestingAccuracy * 100:.2f}%")

    print("\nObservation:")

    if TrainingAccuracy > TestingAccuracy:
        print("The model may be overfitting.")
    elif TrainingAccuracy < TestingAccuracy:
        print("The model may be underfitting.")
    else:
        print("The model is performing well.")

    return TestingAccuracy


def PredictNewStudent(Model):
    PrintHeader("Predict New Student")


    NewStudent = pd.DataFrame({
        "StudyHours": [6],
        "PreviousScore": [66],
        "Attendance": [85],
        "SleepHours": [7],
        "AssignmentsCompleted": [7]
    })

    Prediction = Model.predict(NewStudent)

    print("Prediction :", Prediction[0])
    if Prediction[0] == 1:
        print("Result : The student will Pass.")
    else:
        print("Result : The student will Fail.")

def DisplayConclusion():
    PrintHeader("Conclusion")

    print(""" 
Conclusion:
1. Decision Tree Classifier is a powerful algorithm for classification tasks.
2. It can handle both numerical and categorical data.
3. The model's performance can be evaluated using accuracy and confusion matrix.
4. Hyperparameter tuning (like max_depth) is crucial for optimal performance.
""")


def main():
    PrintHeader("Student Performance ML Case Study")

    # Step 1 : Load the dataset 
    df = LoadDataset()
    DisplayBasicInformation(df)

    # Step 2 : Data Analysis
    CountPassFail(df)
    CalculateStatistics(df)
    AnalyzeFinalResult(df)
    AnalyzeStudyHours(df)

    # Step 3 : Visualization
    PlotStudyHoursHistogram(df)    
    PlotScatterPlot(df)
    PlotAttendanceBoxplot(df)
    PlotAssignmentsAndResult(df)
    PlotSleepHours(df)

    # Step 4 : Model Training and Evaluation
    X, Y = PrepareDataset(df)
    X_train, X_test, Y_train, Y_test = SplitDataset(X, Y) 
    Model = TrainDecisionTree(X_train, Y_train)
    Y_pred = PredictTestData(Model, X_test, Y_test)
    CalculateAccuracy(Y_test, Y_pred)
    DisplayConfusionMatrix(Y_test, Y_pred)
    CompareTrainingTestingAccuracy(Model, X_train, X_test, Y_train, Y_test)
    CompareDecisionTrees(X_train, X_test, Y_train, Y_test)
    PredictNewStudent(Model)
    DisplayConclusion()


if __name__ == "__main__":
    main()