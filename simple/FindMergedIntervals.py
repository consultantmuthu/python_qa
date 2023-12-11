
if __name__ == '__main__':
    intervals = [[4, 5], [4, 6], [8, 12], [9, 9]]
    merged = []     
    for interval in intervals:
        #print(merged)         
        if not merged or merged[-1][1] < interval[0]:             
            merged.append(interval)         
        else:             
            merged[-1][1] = max(merged[-1][1], interval[1])
        #print(merged[-1][1])     
    print(merged)