import itertools
from functools import reduce


def squares(n):
    for it in n:
        yield int(it) ** 2
        
def repeatntimes(elems, n):
    it = itertools.tee(elems, n)
    for i in it:
        yield from i


def evens(x):
    if x % 2:
        x += 1
    while True:
        yield x
        x += 2


def digitsumdiv(n):
    for i in itertools.count(1):
        if not sum(map(int, str(i))) % n:
            yield i


def extractnumbers(n):
    return filter(lambda x: x.isdigit(), n)


def changecase(n):
    return map(lambda x: x.swapcase() if x.isalpha() else x, n)


def productif(elem, cond):
    return reduce(lambda x, y: x * y, map(lambda x: x[0] if x[1] else 1,
                                          zip(elem, cond)), 1)


def main():
    for e in squares([1, 3, 5]):
        print(e)

    for e in repeatntimes([1], 5):
        print(e)

    for e in extractnumbers('12345'):
        print(e)

    print(list(changecase('hello!')))

    print(productif([1, 2, 3], [True, True, True]))
    print(productif(range(5), [False, False, True, False, True]))
    print(productif([], [True, True, True, True]))
    print(productif([100], [False]))
    print(productif(itertools.count(1), [True, True, True, False, True]))
    
    for i in repeatntimes(squares([1, 2, 3]), 2):
    print(i)
        
main()
