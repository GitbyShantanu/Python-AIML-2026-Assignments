import numpy as np
from tensorflow.keras.layers import Dense

def Flatten(matrix : np.ndarray): 
    return matrix.flatten() # flatten is a method in numpy ndarray class

def FullyConnected(flatten_output):
    dense = Dense(units=1, activation="relu") # dense is a class in tensorflow.keras.layers used to create a fully connected layer

    # Dense needs 2D float input of shape (batch_size, features) => here (1, 4) and float32, but flatten gives 1D int array of shape (4,)
    input_data = flatten_output.reshape(1, 4).astype("float32")  # reshape to (1, 4) and convert to float32. 

    dense(input_data)  # initialize the layer

    weights = np.array([[0.1], [0.2], [0.3], [0.4]]) # weights
    bias = np.array([1.0]) # bias
    
    dense.set_weights([weights, bias]) # set weights and bias

    output = dense(input_data) # forward pass
    return output.numpy()[0][0] # return the output


def ManualCalculation(flatten_output):
    weights = [0.1, 0.2, 0.3, 0.4]
    bias = 1

    return (
        (flatten_output[0] * weights[0]) +
        (flatten_output[1] * weights[1]) +
        (flatten_output[2] * weights[2]) +
        (flatten_output[3] * weights[3]) + 
        bias
    )

def main():
    matrix = np.array([
        [6, 4],
        [8, 6]
    ])

    flatten_output = Flatten(matrix)

    final_output = FullyConnected(flatten_output)

    manual_output = ManualCalculation(flatten_output)

    print("Input Matrix:")
    print(matrix)

    print("\nFlatten Output:")
    print(flatten_output)

    print("\nFully Connected Output:", final_output)
    print("Manual Output:", manual_output)

if __name__ == "__main__":
    main()