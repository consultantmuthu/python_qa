import itertools

def count():
    iterator = itertools.count(10, 5)
    for i in iterator:
        print(i)
        if ( i == 100):
            break

def repeat():
    iterator = itertools.repeat('ABC', 3)

    for i in iterator:
        print(i)

def accumalate():
    input = [1,2,3,4,5]
    itetrator = itertools.accumulate(input)

    print(list(itetrator))

def chain():
    data_1 = "ABC"
    data_2 = "DEF"

    iterator = itertools.chain(data_1, data_2)

    print(list(iterator))

def chain_iteratable():
    input = [[10,20],[30,40,50], [60], [70,80]]

    iterator = itertools.chain.from_iterable(input)

    print(list(iterator))

def compress():
    input = [['Python'],['Magic'],[False]]
    selector = [1,True,False]
    iterator = itertools.compress(input, selector)
    #print(list(iterator))
    print(' '.join(list(itertools.chain(next(iterator), next(iterator)))))

def product():
    iterator = itertools.product([1,2,3],[1,2,3])
    for i in iterator:
        print(i[0] * i[1]) 

def permutation():
    iterator = itertools.permutations('Python', 2)
    print(list(iterator))

def combination():
    iterator = itertools.combinations('Python', 2)
    print(list(iterator))

if __name__ == '__main__':
    #count()
    #repeat()
    #accumalate()
    #chain()
    #chain_iteratable()
    #compress()
    #product()
    #permutation()
    combination()
