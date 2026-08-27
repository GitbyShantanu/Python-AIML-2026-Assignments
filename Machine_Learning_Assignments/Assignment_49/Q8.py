import numpy as np
import math 
from sklearn.metrics import confusion_matrix


# Display and calculate TP, TN, FP, FN 
def main():
    actual = [1,1,1,1,0,0,0,0]
    predicted = [1,1,0,1,0,1,0,0] 

    print("Confusion matrix: ")
    confusionMatrix = confusion_matrix(actual, predicted)

    print(confusionMatrix)

    TN = confusionMatrix[0][0]
    FP = confusionMatrix[0][1]
    FN = confusionMatrix[1][0]
    TP = confusionMatrix[1][1]

    print("TP :", TP)
    print("TN :", TN)
    print("FP :", FP)
    print("FN :", FN)

if __name__ == "__main__":
    main()