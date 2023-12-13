
if __name__ == '__main__':
    seq = ['soup', 'egg', 'salad', 'curry', 'sambar']

    print(list(map(lambda x : x[0] == 's', seq)))

    print(list(filter(lambda x : x[0] == 's', seq)))