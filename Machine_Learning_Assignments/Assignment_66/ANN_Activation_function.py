import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def relu(x):
    return np.maximum(0, x)


def tanh(x):
    return np.tanh(x)


def main():
    x = np.array([-10, -4, 0, 4, 6, 10]) 
    print("Input : " , x)

    sigmoid_output = sigmoid(x)
    relu_output = relu(x)
    tanh_output = tanh(x)

    plt.plot(x, sigmoid_output, label="Sigmoid")
    plt.plot(x, relu_output, label="ReLU")
    plt.plot(x, tanh_output, label="Tanh")

    plt.xlabel("Input")
    plt.ylabel("Output")
    plt.title("Activation Functions")
    plt.legend()
    plt.grid()

    plt.show()


if __name__ == "__main__":
    main()