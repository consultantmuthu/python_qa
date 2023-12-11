
if __name__ == '__main__':
    input_array = [1,2,8,-2,10]

    max_sum = input_array[0]     
    current_sum = input_array[0]     
    for i in range(1, len(input_array)):        
        current_sum = max(input_array[i], current_sum + input_array[i])         
        max_sum = max(max_sum, current_sum)     
    print(max_sum)