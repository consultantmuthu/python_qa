def print_formatted(number):
    length = len(str(bin(number))) - 2
    print(length)  
    for i in range(1, number+1):
        print(format(i).rjust(length), format(i, '^o').rjust(length), \
            format(i, 'x').upper().rjust(length), \
                format(i, 'b').rjust(length))

if __name__ == '__main__':
    print_formatted(63)