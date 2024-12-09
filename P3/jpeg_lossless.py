import numpy as np
from huffman import huffman_encode

def get_pixel(img, x, y):
    return img[y][x]

def p1(a):
    return a

def p2(b):
    return b

def p3(c):
    return c

def p4(a, b, c):
    return a + b - c

def p5(a, b, c):
    return a + (b - c) / 2

def p6(a, b, c):
    return b + (a - c) / 2

def p7(a, b):
    return (a + b) / 2

predictors = [
    None,
    p1,
    p2,
    p3,
    p4,
    p5,
    p6,
    p7
]

def predict(img_arr, predictor_num):
    height, width = img_arr.shape
    diffs = np.zeros_like(img_arr, dtype=np.int16)
    
    for y in range(height):
        for x in range(width):
            a = get_pixel(img_arr, x - 1, y)    # pixel to left of x
            b = get_pixel(img_arr, x, y - 1)    # above x
            c = get_pixel(img_arr, x - 1, y - 1)  # diagonal from x
            
            
            if predictor_num == 1:
                prediction = predictors[predictor_num](a)
            elif predictor_num == 2:
                prediction = predictors[predictor_num](b)
            elif predictor_num == 3:
                prediction = predictors[predictor_num](c)
            elif predictor_num == 7:
                prediction = predictors[predictor_num](a, b)
            else:
                prediction = predictors[predictor_num](a, b, c)
            
            x_val = img_arr[y][x]
            difference = x_val - prediction
            diffs[y][x] = difference
            
    return diffs



def test_all_predictors(img_array, predictor_num):
    diffs = predict(img_array, predictor_num)
    diff_list = diffs.flatten().tolist()
    
    huffman_codes, coded_arr = huffman_encode(diff_list)
    return len(coded_arr), coded_arr, huffman_codes




def find_best_predictor(channel_data):
    smallest_size = float('inf')
    best_predictor = 0
    best_encoded = None
    best_codes = None
    
    for predictor_num in range(1, 8):
        compressed_size, coded_arr, huffman_codes = test_all_predictors(channel_data, predictor_num)
        
        if compressed_size < smallest_size:
            smallest_size = compressed_size
            best_predictor = predictor_num
            best_encoded = coded_arr
            best_codes = huffman_codes
            
    return smallest_size, best_predictor, best_encoded, best_codes



def lossless_jpeg_compress(img_data, width, height):
    img_array = np.array(img_data).reshape(height, width, 3)
    
    best_sizes = []
    best_predictors = []
    best_compressed = []
    best_huffman_codess = []
    
    for channel in range(3):
        channel_data = img_array[:, :, channel]
        size, predictor, encoded, codes = find_best_predictor(channel_data)
        
        best_sizes.append(size)
        best_predictors.append(predictor)
        best_compressed.append(encoded)
        best_huffman_codess.append(codes)
    
    return {
        'predictors': best_predictors,
        'compressed_sizes': best_sizes,
        'compressed_data': best_compressed,
        'huffman_codes': best_huffman_codess
    }