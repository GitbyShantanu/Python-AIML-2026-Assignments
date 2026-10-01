import numpy as np


def ReLU(feature_map):
    return np.maximum(0, feature_map)


def MaxPooling(feature_map):
    #                  3*3            2*2              1
    # Output size = ((Input size - Pool size) / Stride) + 1
               

    pool_size = 2 # 2*2 region
    stride = 1 # 1 step move

    pooled_rows = ((feature_map.shape[0] - pool_size) // stride) + 1  # ((3 - 2) // 1) + 1 = 2
    pooled_cols = ((feature_map.shape[1] - pool_size) // stride) + 1  # ((3 - 2) // 1) + 1 = 2

    pooled = np.zeros((pooled_rows, pooled_cols))

    for i in range(pooled_rows):  # pooled map traversal
        for j in range(pooled_cols):  # pooled map traversal

            region = feature_map[i:i+2, j:j+2] # 2*2 region
            pooled[i, j] = np.max(region) # maximum value in the region

    return pooled


def main():

    feature_map = np.array([
        [3, 3, 3],
        [0, 0, 0],
        [-3, -3, -3],
    ])

    print("Feature Map:")
    print(feature_map)

    relu_output = ReLU(feature_map)

    print("\nReLU Output:")
    print(relu_output)

    pooled_output = MaxPooling(relu_output)

    print("\nMax Pooling Output:")
    print(pooled_output)


if __name__ == "__main__":
    main()