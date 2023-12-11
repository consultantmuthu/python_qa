import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    data = numpy.array(arr, float)
    
    return data[::-1]

if __name__ == '__main__':
    print(arrays([1, 2, -3, 4]))