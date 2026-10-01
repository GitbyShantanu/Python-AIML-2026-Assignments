import numpy as np 

def Convolution(image, kernel):
    map_len = len(image) - len(kernel) + 1 # 5-3+1=3 => 3x3
    feature_map = np.zeros((map_len, map_len))

    for i in range(map_len):
        for j in range(map_len):
            region = image[i:i+3, j:j+3] 
            result = np.sum(region * kernel) 
            feature_map[i, j] = result 

    return feature_map 

def main():

    image = np.array([
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]) 
    
    print("Image shape : ", image.shape)  
    print("Image : ")
    print(image)

    kernel = np.array([
        [-1, -1, -1],
        [0, 0, 0],
        [1, 1, 1]
    ])

    print("Kernel shape : ", kernel.shape) 
    print("Kernel : ")
    print(kernel) 

    feature_map = Convolution(image, kernel)    
    print("Feature Map : ")
    print(feature_map)

if __name__ == "__main__":
    main()