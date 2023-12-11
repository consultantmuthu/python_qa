def minion_game(string):
    vowel = 'aeiou'.upper()
    strl = len(string)
    print(strl)
    total = 0
    for i in range(strl):
        if string[i] in vowel:
            total = total + (strl - i)
    print(total)
    kevin = sum(strl-i for i in range(strl) if string[i] in vowel)
    print(kevin)
    stuart = strl*(strl + 1)/2 - kevin
    print(stuart)
    if kevin == stuart:
        print ('Draw')
    elif kevin > stuart:
        print ('Kevin %d' % kevin)
    else:
        print ('Stuart %d' % stuart)

if __name__ == '__main__':
    minion_game('APPLE')
