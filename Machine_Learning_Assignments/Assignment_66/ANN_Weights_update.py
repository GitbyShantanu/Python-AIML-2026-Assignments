def main():
    X = 2
    W = 0.5
    bias = 1
    Y_true = 5
    learning_rate = 0.1

    Y_pred = X * W + bias

    error = Y_true - Y_pred

    W = W + learning_rate * error * X

    print("Y_True:", Y_true)
    print("Y_Pred:", Y_pred)
    print("Error:", error)
    print("Updated Weight:", W)


if __name__ == "__main__":
    main()