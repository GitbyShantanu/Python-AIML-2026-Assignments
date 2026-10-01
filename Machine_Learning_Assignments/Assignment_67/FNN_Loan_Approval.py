import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score


def predict_loan(X, Y, new_applicant):

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42
    )

    scaler = StandardScaler()

    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model = MLPClassifier(
        hidden_layer_sizes=(10, 5),
        max_iter=1000,
        random_state=42
    )

    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    accuracy = accuracy_score(Y_test, Y_pred)

    new_applicant = scaler.transform(new_applicant)
    prediction = model.predict(new_applicant)

    print("Accuracy:", accuracy)

    if prediction[0] == 1:
        print("Prediction: Loan Approved")
    else:
        print("Prediction: Loan Rejected")


def main():

    X = np.array([
        [25000, 600, 200000, 10000, 0],
        [40000, 700, 300000, 8000, 1],
        [60000, 750, 500000, 12000, 1],
        [20000, 550, 150000, 15000, 0],
        [80000, 800, 700000, 10000, 1],
        [35000, 650, 250000, 9000, 1],
        [18000, 500, 100000, 12000, 0],
        [90000, 850, 800000, 15000, 1],
        [30000, 580, 200000, 14000, 0],
        [70000, 780, 600000, 10000, 1]
    ])

    Y = np.array([0, 1, 1, 0, 1, 1, 0, 1, 0, 1])

    new_applicant = np.array([[55000, 720, 400000, 10000, 1]])

    predict_loan(X, Y, new_applicant)


if __name__ == "__main__":
    main()