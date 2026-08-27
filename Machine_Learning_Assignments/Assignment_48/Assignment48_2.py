import numpy as np


def CustomLinearRegression(X, Y):
    x_mean = np.mean(X)
    y_mean = np.mean(Y)

    n = len(X)

    numerator = 0
    denominator = 0

    # Calculate slope m
    for i in range(n):
        numerator = numerator + (X[i] - x_mean) * (Y[i] - y_mean)
        denominator = denominator + ((X[i] - x_mean) ** 2)

    m = numerator / denominator

    # c = Y - m*X
    # c = y_bar - m * x_bar
    c = y_mean - (m * x_mean)

    # Now we have m, X and c    
    print("\nRegression Equation : ")
    print(f"Y = {m} * X + {c}")

    Yp = []
    for i in range(n):
        Yp.append(m * X[i] + c)

    print("\nPredicted Y : ")
    for i in range(n):
        print(f"Yp{i+1} : {Yp[i]}")

    # Residual (Error) is differenc between predicted points vs actual points
    print("\nResidual (Error) : Y - Yp")
    Error = []
    for i in range(n):
        Error.append(Y[i] - Yp[i])
        print(f"RE{i+1} : {Y[i]} - {Yp[i]} = {Error[i]:.1f}")
    print()

    # Mean Squared Error (MSE)
    # MSE = Sum((Y - Yp)^2) / n
    numerator = 0
    denominator = 0

    print("Squares of Residuals (Error) R : ")
    for i in range(n):
        numerator = numerator + (Error[i] ** 2)
        print(f"(RE{i+1}) ^ 2 : {Error[i] ** 2:.2f}")

    MSE = numerator / n
    print("\nMean Squared Error (MSE) = Sum(RE ^ 2) / n")
    print(f"MSE = {numerator:.2f} / {n}")
    print(f"MSE = {MSE}\n")


    # R-Squared R^2 (Rsq)
    # Rsq = 1 - (SS_res / SS_tot)
    
    # Where 
    # SS_res = Sum((Y - Yp) ^ 2) = Sum(MSE)
    # SS_tot = Sum((Y - Y_bar) ^ 2) = Sum((Y - Y_mean)**2)

    print("R-Squared R^2 (Rsq) = 1 - (SS_res / SS_tot)\n")

    print(f"SS_res = Sum((Y - Yp)^2))")
    print(f"SS_res = Sum(MSE)")
    SS_res = 0
    for i in range(n):
        SS_res = SS_res + (Error[i] ** 2)
    print(f"SS_res : {SS_res:.1f}\n")

    print(f"SS_tot = Sum((Y - Y_mean)^2)")    
    SS_tot = 0
    for i in range(n):
        SS_tot = SS_tot + ((Y[i] - y_mean) ** 2)

    print("SS_tot :",SS_tot)

    print(f"\nR-squared = 1 - {SS_res:.1f} / {SS_tot:.1f}")
    Rsq = 1 - (SS_res / SS_tot)
    print(f"R-squared = {Rsq:.2f}")

    print(f"\nModel Explains only {Rsq * 100:.0f}% variance\n")


def main():
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    CustomLinearRegression(X, Y)
    

if __name__ == "__main__":
    main()
