import numpy as np
import math 


def MSE(Y_True, Y_pred):
    n = len(Y_True)
    total_error = 0 

    for i in range(n):
        error = Y_True[i] - Y_pred[i] 
        sq_err = error ** 2
        total_error = total_error + sq_err

    mse = total_error / n
    return mse


def BCE(Y_true, Y_pred):
    total = 0

    for i in range(len(Y_true)):
        loss = -(Y_true[i] * math.log(Y_pred[i]) +
                (1 - Y_true[i]) * math.log(1 - Y_pred[i]))

        total = total + loss
    return total / len(Y_true)


def main():
    Y_True = np.array([1, 0, 1, 1])
    Y_pred = np.array([0.9, 0.2, 0.8, 0.7])

    mse = MSE(Y_True, Y_pred)
    bce = BCE(Y_True, Y_pred)

    print("Mean Squared Error:", mse)
    print("Binary Cross Entropy:", bce)

    print("MSE is generally used for Regression.")
    print("Binary Cross Entropy is used for Binary Classification.")


if __name__ == "__main__":
    main()