def fib(n):
    if(n == 0):
       return 0
    elif(n == 1):
        return 1
    else:
        return ((fib(n - 1) + fib(n - 2)))

def fib_for_array(input):
    output = []
    for i in range(len(input)):
        output.append(fib(input[i]))
    return output

if __name__ == '__main__':
    cube = lambda x : x ** 3
    #print(fib(2))
    output = map(cube, [fib(2)])
    print(list(output))
    output = map(cube, fib_for_array([0,1,1,2,3]))
    print(list(output))

