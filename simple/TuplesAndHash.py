   
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(type(integer_list))
    # List is not hashable as it is mutable
    # (ie) value can change later
    print(abs(hash(tuple(integer_list))))