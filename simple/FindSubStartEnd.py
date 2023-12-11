
def find_substring_start_end(input_string, sub_string):
    start = input_string.find(sub_string)
    if (start == -1):
        return [(-1,-1)]
    else:
        index = []
        while start >= 0:
            index.append((start, start + (len(sub_string) - 1)))
            start = input_string.find(sub_string, (start + 1))
        return index

if __name__ == '__main__':
   data = find_substring_start_end('aaaaaaaaaa', 'aa') 
   print(data)