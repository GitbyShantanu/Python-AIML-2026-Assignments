import math

def sigmoid(x):
    return 1/ (1 + math.exp(-x)) 

def main():
    x1 = 2
    x2 = 3

    w1 = 0.4
    w2 = 0.6

    bias = 0.5

    z = (x1 * w1) + (x2 * w2) +bias 

    output = sigmoid(z) 
    print("Output Y : ", output) 

    if output < 0.5:
        print("Output is close to 0") 
    else:
        print("Output is close to 1") 

if __name__ == "__main__":
    main()