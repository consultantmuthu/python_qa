from operator import itemgetter

def decorator(input_list):
    input_list.sort(key=itemgetter(1))
    for item in input_list:
        if item[2] == 'M':
            print(f"Mr {item[0]}")
        else:
            print(f"Ms {item[0]}")

if __name__ == '__main__':
    input_list = [
        ['Mike Thomson', 20, 'M'], 
        ['Robert Bustle', 32, 'M'], 
        ['Andria Bustle', 30, 'F'], 
    ]
    decorator(input_list)