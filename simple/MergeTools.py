def merge_tools(data, k):
    temp = []
    len_temp = 0
    for item in data:
        len_temp += 1
        if item not in temp:
            temp.append(item)
        if len_temp == k:
            print (''.join(temp))
            temp = []
            len_temp = 0

if __name__ == '__main__':
    merge_tools('ABCBBDAFF', 3)