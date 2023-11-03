import numpy as np

def arrays(arr):
    # complete this function
    # use numpy.array
    reverse_arr = np.flip(np.array(arr, float))
    return reverse_arr

arr = input().strip().split(' ')
result = arrays(arr)
print(result)