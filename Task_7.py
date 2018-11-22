import socket
import itertools


def isIPv4(addr):
    # Checking for a valid IP
    try:
        socket.inet_aton(addr)
        True
    except socket.error:
        False


def popcount(n):
    # popping element and counting 1s from it's binary re
    x = bin(n).count("1")
    return x


"""
def pascals(n, r =[]):
    # Printing Pascal's traingle using a generator
    for x in range(n):
        l = len(r)
        r = [1 if i == 0 or i == l else r[i-1]+r[i] for i in range(l+1)]
        yield r
"""


def pascals():
    preceding = (1,)
    for i in itertools.count(1):
        tri_tuple = []
        tri_tuple.append(1)
        for k in range(len(preceding) - 1):
            tri_tuple.append(preceding[k] + preceding[k + 1])
        tri_tuple.append(1)
        yield tuple(preceding)
        preceding = tri_tuple


"""
def fibonacci(count):
    #Fibonacci from lambda
    sequence = []
    any(map(lambda _: sequence.append(sum(sequence[-2:])), range(2, count)))
    return sequence[count]
"""

from functools import reduce


def fibonacci(count):
    # Fibonacci from lambda
    return reduce(lambda x, count: [x[1], x[0] + x[1]], range(count), [0, 1])[0]


def subpalindrome(string):

    def check(word):
        if len(word) == 1:
            return True
        return all(word[i] == word[-1 * (i + 1)] for i in range(len(word) // 2))


    pal = ''
    max = 0
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            if check(string[i:j]):
                if j - i > max:
                    pal = string[i:j]
                    max = j - i
                elif j - i == max:
                    if string[i:j] < pal:
                        pal = string[i:j]

    return pal


def powers(n, m):
    # Return dict with values of i to power i modulo m for every i from 1 to n
    dict = []
    for i in range(n):
        return dict.append(i ^ (i % m))
    return dict

    ######################
    # Remaining programs #
    ######################


def valuesunion(*dicts):
    l = list()
    for i in dicts:
        for j in i.values():
            l.append(j)
    return set(l)


def spiral(n):
    i = 1
    a = [[0 for i in range(n)] for j in range(n)]
    for l in range(n):
        a[0][l] = i
        i += 1
    h1 = 1
    h2 = n - 1
    v1 = 0
    v2 = n - 1
    while i <= (n * n):
        # down
        for l in range(h2 - h1 + 1):
            a[h1 + l][v2] = i
            i += 1
        v2 -= 1

        # left
        for l in range(v2 - v1 + 1):
            a[h2][v2 - l] = i
            i += 1
        h2 -= 1

        # up
        for l in range(h2 - h1 + 1):
            a[h2 - l][v1] = i
            i += 1
        v1 += 1

        # right
        for l in range(v2 - v1 + 1):
            a[h1][v1 + l] = i
            i += 1
        h1 += 1
    return a




def brackets2(n, m):
    # An exceptionally silly brackets2() program
    # n pairs of () and m pairs of [] with a lexicographical order
    string = ''
    string += '()' * n
    string += '[]' * m
    cache = []
    count1 = 0
    count2 = 0
    for i in itertools.permutations(string, 2 * (n + m)):
        result = True
        for j in list(i):
            if j == ')':
                count1 -= 1
                cache.append(')')
                if count1 < 0:
                    result = False
            if j == ']':
                count2 -= 1
                cache.append(']')
                if count2 < 0:
                    result = False
            if j == '(':
                count1 += 1
                cache.append('(')
            if j == '[':
                count2 += 1
                cache.append(']')
        if result is True:
            print(i)
        count1 = 0
        count2 = 0
        return cache

    def logic(item):

        # ( < ) < [ < ]
        p1 = []
        p2 = []
        p3 = []
        p4 = []

        if item == '(':
            p1.append(item)
        elif item == ')':
            p2.append(item)
        elif item == '[':
            p3.append(item)
        elif item == ']':
            p4.append(item)

        p5 = p4 + p1 + p2 + p3

        return p5


    for item in cache:
        matrix = logic(item)

        yield matrix

def brackets22(m, n):
    
    # Another failed attempt at making brackets22()
   
    ell = ()
    if m == 0:
       ell = ("".join(seq) for seq in itertools.product("[]", repeat=n))
    elif n ==0:
        ell = ("".join(seq) for seq in itertools.product("()", repeat=m))
    else:
        ell = ("".join(seq) for seq in itertools.product("()[]", repeat= n and m ))

    return ell


def main():
    print(popcount(0))
    print(popcount(1))
    print(popcount(10))
    print(popcount(1023))

    for i in subpalindrome('abc'):
        print(i)

    print(subpalindrome('aaaa'))
    print(subpalindrome('abaxfgf'))
    print(subpalindrome('abacabad'))

    isIPv4('192.168.0.15')
    isIPv4('255.255.255.255')
    isIPv4('555.555.555.555')
    isIPv4('190+2.168.0.0')
    isIPv4('abacaba')
    isIPv4('')

    print(fibonacci(5))

    print(powers(4, 50))
    print(powers(1, 1))

    print(spiral(4))

    print(valuesunion({1: 2, 4: 8}))

    for i in (brackets2(3, 0)):
        print(i)

    for i in brackets22(2,1):
        for j in i:
            print(j)


main()
