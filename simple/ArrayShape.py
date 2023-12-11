import sys
import numpy as np

array=list(map(int, input().split()))
#print(array)
print(np.reshape(array, (3,3)))