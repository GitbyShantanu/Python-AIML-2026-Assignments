from sklearn.model_selection import train_test_split
from CustomKNNClassifier import KNNClassifier
import pandas as pd

border = "-"*60

def main():
    border = "-" * 60

    Data = [
        {"StudyHours" : 2, "Attendance" : 60, "Result" : "Fail"},
        {"StudyHours" : 5, "Attendance" : 80, "Result" : "Pass"},
        {"StudyHours" : 6, "Attendance" : 85, "Result" : "Pass"},
        {"StudyHours" : 1, "Attendance" : 50, "Result" : "Fail"}
    ]

    df = pd.DataFrame(Data)
    print(border)
    print("Dataset : ")
    print(border)
    print(df)
    print(border)


    X_train = df.drop(columns=['Result'])
    Y_train = df['Result']

    stdHrs = int(input("Enter Study Hours : "))
    Attd = int(input("Enter Attendance : "))
    print(border)
    new_point = {"StudyHours" : stdHrs, "Attendance" : Attd}

    model = KNNClassifier(n_neighbors=3)
    model = model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test=new_point)
    print("Predicted Result : ", Y_pred)
    print(border)

    
if __name__ == "__main__":
    main()