from sklearn.metrics import classification_report
import numpy as np
import math 
from sklearn.metrics import confusion_matrix

# Classification report generate
def main():
    actual = [1,1,1,1,0,0,0,0]
    predicted = [1,1,0,1,0,1,0,0] 

    print("Classification Report: \n",classification_report(actual,predicted))

if __name__ == "__main__":
    main()  