def count_substring(string, sub_string):
    count = 0
    start_index = 0
    for i in range(len(string)):
        index = string.find(sub_string, start_index)
        if index == -1:
            return count
        else:
            count = count+1
        start_index = index + len(sub_string) - 1
    return count

if __name__ == '__main__':
    count = count_substring('ABCDCDC', 'CDC')
    print("Found {}".format(count))