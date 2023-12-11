from operator import itemgetter

if __name__ == '__main__':
    nested_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nested_list.append([name,score])
    nested_list.sort(key=itemgetter(1))
    scores = []
    for list in nested_list:
        scores.append(list[1])
    scores = sorted(set(scores))
    second_score = scores[1]
    names = []    
    for list in nested_list:
        if list[1] == second_score:
            names.append(list[0])
    names = sorted(names)
    print(*names, sep='\n')