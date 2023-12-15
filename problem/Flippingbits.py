#!/bin/python3

def flippingBits(n):
    n = n + 2**32 # convert n to unsigned integer
    bits = str(bin(n))[2:]
    bits = bits.replace('1','2')
    bits = bits.replace('0','1')
    bits = bits.replace('2','0')
    print(int(bits,2))

if __name__ == '__main__':
    flippingBits((2147483647))
    flippingBits(1)
    flippingBits(0)    