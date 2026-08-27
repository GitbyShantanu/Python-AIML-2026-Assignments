import pandas as pd
from sklearn.linear_model import LinearRegression


def MyLinearRegression(Datapath):
    df = pd.DataFrame(Datapath)
    print(df)
    
    X = df[["Experience"]]
    Y = df["Salary"]

    model = LinearRegression()
    model = model.fit(X, Y)

    X_test = 6
    predicted_salary = model.predict([[X_test]])

    print(f"Predicted Salary for {X_test} years of experience: {predicted_salary[0]:.2f}")
    

def main():
    Experience = [1,2,3,4,5]
    Salary = [20000, 25000, 30000, 35000, 40000]

    Dataset = {
        "Experience" : Experience,
        "Salary" : Salary    
    }

    MyLinearRegression(Dataset)

if __name__ == "__main__":
    main()