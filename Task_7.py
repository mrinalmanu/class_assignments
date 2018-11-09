import socket

def isIPv4(addr):
    #Checking for a valid IP
    try:
        socket.inet_aton(addr)
        print("True")
    except socket.error:
        print("False")

def popcount(n):
    # popping element and counting 1s from it's binary re
    x = bin(n).count("1")
    return x

def pascals(n, r =[]):
    # Printing Pascal's traingle using a generator
    for x in range(n):
        l = len(r)
        r = [1 if i == 0 or i == l else r[i-1]+r[i] for i in range(l+1)]
        yield r

def fibonacci(count):
    #Fibonacci from lambda
    sequence = []
    any(map(lambda _: sequence.append(sum(sequence[-2:])), range(2, count)))
    return sequence[:count]

def subpalindrome(s):
    if not s:
        yield []
        return
        for i in range(len(s), 0, -1):
            sub = s[:i]
            if sub == sub[::-1]:
                for rest in palindromic_substrings(s[i:]):
                    yield [sub] + rest

def powers(n, m):
    #Return dict with values of i to power i modulo m for every i from 1 to n
    dict = []
    for i in range (n):
        return dict.append(i^(i%m))
    return dict

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

    for i in pascals(2):
        print(i)

    print(fibonacci(5))

    print(powers(4, 50))
    print(powers(1, 1))

main()
