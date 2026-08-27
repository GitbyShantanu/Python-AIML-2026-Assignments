import numpy as np

def CustomLinearRegression(X, Y):
        x_mean = np.mean(X)
        y_mean = np.mean(Y)
    
        print("Mean of X : ", x_mean)
        print("Mean of Y : ", y_mean)
    
        n = len(X)
    
        numerator = 0
        denominator = 0
    
        # Y = m*X + c
    
        # Calculate slope m
        for i in range(n):
            numerator = numerator + (X[i] - x_mean) * (Y[i] - y_mean)
            denominator = denominator + ((X[i] - x_mean) ** 2)
    
        m = numerator / denominator
        print("\nSlope (m) : ", m)
    
        # c = Y - m*X
        # c = y_bar - m * x_bar
        c = y_mean - (m * x_mean)
        print("Intercept (c) : ", c)
    
        # Now we have m, X and c
        
        print("\nRegression Equation : ")
        print(f"Y = {m} * X + {c}")
    
        Yp = []
        for i in range(n):
            Yp.append(m * X[i] + c)
    
        # print("\nPredicted Y : ", np.float64(Yp))
    
        x = 6
        print(f"\nPredicted Y for X=6 : {m * x + c :.2f}")
    

def main():
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    CustomLinearRegression(X, Y)
    


if __name__ == "__main__":
    main()
