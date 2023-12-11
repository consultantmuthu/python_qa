import numpy as np

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    arr = sorted(set(arr))
    print(arr[-2])