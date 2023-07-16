# Detecting Outliers using IQR technique
# Detecting Outliers using Z-Score technique

"""_
1. Sort
2. Find Q1(25 percentile) and Q3 (75 percentile)
3. Find IQR = Q3 - Q1
4. Find Lower Fence = Q1 - 1.5 * IQR
5. Find Upper Fence = Q3 + 1.5 * IQR
"""

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

dataset = [11,10,12,14,13,15,102,12,14,17,19,107,10,13,12,14,17,19,107,10,13,12,14,12,108,12,11,14,13,15,10,15,12,10,14,13,15,10]


def detect_outliers(data):
    data = sorted(data)
    q1,q3 = np.percentile(data,[25,75])
    iqr = q3 - q1
    lower_fence = q1 - iqr * 1.5
    upper_fence = q3 + iqr * 1.5
    print(lower_fence,upper_fence)

    outliers = []
    for i in data:
        if  i < lower_fence or i > upper_fence:
            outliers.append(i)
    
    return outliers        
print(detect_outliers(dataset))
sns.boxplot(dataset)
plt.show()