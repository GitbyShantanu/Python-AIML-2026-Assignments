import numpy as np 
import pandas as pd 

def main():
    dataset = [6,7,8,9,10,11,12]

    print("Variance : ", np.var(dataset))
    print("Standard deviation : ", np.std(dataset))


if __name__ == "__main__":
    main()