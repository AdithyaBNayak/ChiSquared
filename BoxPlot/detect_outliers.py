# Detecting Outliers using Z-Score technique
import numpy as np

dataset = [11,10,12,14,13,15,102,12,14,17,19,107,10,13,12,14,17,19,107,10,13,12,14,12,108,12,11,14,13,15,10,15,12,10,14,13,15,10]


def detect_outliers(data):
    outliers = []
    threshold = 2 # 3rd standard deviation
    mean = np.mean(data)
    std = np.std(data)
    
    print(mean)
    print(std)
    for i in data:
        z_score = (i-mean)/std
        print(f"i = {i}, zScore = {z_score}")
        if np.abs(z_score) > threshold:
            outliers.append(i)
    return outliers

print(detect_outliers(dataset))