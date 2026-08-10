import pandas as pd
import matplotlib.pyplot as plt

Border = "-" * 50

def printHeader(Title):
    print()
    print(Border)
    print(Title)
    print(Border)


def LoadDataset():
    DataPath = "student_performance_ml.csv"
    df = pd.read_csv(DataPath)
    print("Dataset loaded successfully")
    return df


def DisplayBasicInformation(df):
    printHeader("Basic Information about Dataset")    

    print("First 5 records :")
    print(df.head())

    print("\nLast 5 records :")
    print(df.tail())

    print("\nShape of dataset :", df.shape)

    print("\nList of column names :")
    print(list(df.columns))

    print("\nData types of each column :")
    print(df.dtypes)


def CountPassFail(df):
    printHeader("Pass/Fail Analysis")
    
    totalStudents = len(df)
    print("Total number of students : ", totalStudents)

    PassedStudents = len(df[df["FinalResult"] == 1]) 
    print("Number of passed students : ", PassedStudents)

    FailedStudents = len(df[df["FinalResult"] == 0])
    print("Number of failed students : ", FailedStudents)


def CalculateStatistics(df):
    printHeader("Statistics Analysis using Pandas")

    print("Average StudyHours : ", df["StudyHours"].mean())
    print("Average Attendance : ", df["Attendance"].mean())
    print("Maximum PreviousScore : ", df["PreviousScore"].max())
    print("Minimum SleepHours : ", df["SleepHours"].min())
    

def AnalyzeFinalResult(df):
    printHeader("Final Result Analysis")

    # Count how many times each value (0, 1) appears 
    Result = df["FinalResult"].value_counts()

    print("Distribution of FinalResult : ")
    print(Result)

    # Result is a Series and 1, 0 are labels:
    # 1 -> Pass count
    # 0 -> Fail count
    Pass = Result[1]
    Fail = Result[0] 
    Total = len(df)

    PassPercentage = (Pass / Total) * 100
    FailPercentage = (Fail / Total) * 100

    print(f"Pass Percentage : {PassPercentage:.2f}%")
    print(f"Fail Percentage : {FailPercentage:.2f}%")

    if abs(PassPercentage - FailPercentage) <= 10:
        print("Dataset is balanced.")
        print("Pass and Fail percentages are nearly equal.")
    else:
        print("Dataset is not balanced.")
        print("Pass students are much higher than failed students.")


def AnalyzeStudyHours(df):
    printHeader("Study Hours and Attendance Analysis")

    PassedStudents = df[df["FinalResult"] == 1]
    FailedStudents = df[df["FinalResult"] == 0] 

    PassStudyHours = PassedStudents["StudyHours"].mean()
    FailStudyHours = FailedStudents["StudyHours"].mean()

    print("Average study hours of passed students : ", PassStudyHours)
    print("Average study hours of failed students : ", FailStudyHours)

    PassAttendance = PassedStudents["Attendance"].mean()
    FailAttendance = FailedStudents["Attendance"].mean()

    print("Average attendance of passed students : ", PassAttendance)
    print("Average attendance of failed students : ", FailAttendance)

    print(""" 
Observations :
1. Passed students have higher avg study hours. 
2. Failed students have lower avg study hours.
3. Passed students have higher avg attendance.
4. Failed students have lower avg attendance.
5. Higher Study Hours and Attendace improve the chances of passing.
""")


def PlotStudyHoursHistogram(df):
    printHeader("Study Hours Histogram")

    plt.figure(figsize=(7,5))
    plt.hist(df["StudyHours"])

    plt.title("Histogram of Study Hours Distribution")
    plt.xlabel("Study Hours")
    plt.ylabel("Number of Students")
    
    plt.grid()
    plt.show()
    print("""
Observation:
1. The histogram shows the distribution of Study Hours.
2. The tallest bars represent the study hour range with the most students.
3. Smaller bars represent fewer students in that range.
4. It helps understand how students' Study Hours are distributed.
""")


def PlotScatterPlot(df):
    printHeader("Scatter plot of StudyHours vs Attendance")

    PassedStudents = df[df["FinalResult"] == 1]
    FailedStudents = df[df["FinalResult"] == 0]

    plt.figure(figsize=(7,5))

    plt.scatter(
        PassedStudents["StudyHours"],
        PassedStudents["Attendance"],
        color = "green",
        label = "Pass"
    )

    plt.scatter(
        FailedStudents["StudyHours"],
        FailedStudents["Attendance"],
        color = "red",
        label = "Fail"
    )

    plt.xlabel("Study Hours")
    plt.ylabel("Attendance")
    plt.title("Scatter plot of StudyHours vs Attendance")

    plt.grid()
    plt.legend()
    plt.show()
    print("""
Observation:
1. Green points represent Passed students.
2. Red points represent Failed students.
3. Most passed students have higher Study Hours and Previous Scores.
4. Most failed students have lower Study Hours and Previous Scores.
""")


def PlotAttendanceBoxplot(df):
    printHeader("Attendance Boxplot")

    plt.boxplot(df["Attendance"])
    plt.title("Boxplot of Attendance")
    plt.ylabel("Attendance")
    plt.grid()
    plt.show()
    print("""
Observation:
1. Attendance ranges from about 60 to 96.
2. The median Attendance is around 80.
3. Most students have Attendance between 70 and 89.
4. No outliers are visible in the dataset.
""")


def PlotAssignmentsAndResult(df):
    printHeader("Assignments Completed and Final Result")

    PassedStudents = df[df["FinalResult"] == 1]
    FailedStudents = df[df["FinalResult"] == 0]

    plt.scatter(PassedStudents["AssignmentsCompleted"], PassedStudents["FinalResult"], c="green", label="Pass")
    plt.scatter(FailedStudents["AssignmentsCompleted"], FailedStudents["FinalResult"], c="red", label="Fail")

    plt.title("Assignments Completed and Final Result")
    plt.xlabel("Assignments Completed")
    plt.ylabel("Final Result")

    plt.yticks([0, 1], ["Fail", "Pass"])

    plt.legend()
    plt.show()

    print("""
Observation:
1. Green points represent Passed students.
2. Red points represent Failed students.
3. Students who completed more assignments are mostly in the Pass group.
4. Completing more assignments improves the chances of passing.
""")

def PlotSleepHours(df):
    printHeader("Sleep Hours and Final Result")

    PassedStudents = df[df["FinalResult"] == 1]
    FailedStudents = df[df["FinalResult"] == 0]

    plt.scatter(PassedStudents["SleepHours"], PassedStudents["FinalResult"], c="green", label="Pass")
    plt.scatter(FailedStudents["SleepHours"], FailedStudents["FinalResult"], c="red", label="Fail")

    plt.title("Sleep Hours and Final Result")
    plt.xlabel("Sleep Hours")
    plt.ylabel("Final Result")

    plt.yticks([0, 1], ["Fail", "Pass"])

    plt.legend()
    plt.show()

    print("""
Observation:
1. Green points represent Passed students.
2. Red points represent Failed students.
3. Students with higher Sleep Hours are found in both Pass and Fail groups.
4. Sleeping more alone does not guarantee success.
""")
    

def main():
    printHeader("Student Performance ML Case Study")

    df = LoadDataset()

    DisplayBasicInformation(df)

    CountPassFail(df)

    CalculateStatistics(df)

    AnalyzeFinalResult(df)

    AnalyzeStudyHours(df)

    PlotStudyHoursHistogram(df)

    PlotScatterPlot(df)

    PlotAttendanceBoxplot(df)

    PlotAssignmentsAndResult(df)

    PlotSleepHours(df)

if __name__ == "__main__":
    main()