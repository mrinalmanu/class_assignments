
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)


# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

def fibonacci(n):
    if n==1 or n==2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

def recurrent(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n % 2 == 0:
        return recurrent(n // 2)
    else:
        return recurrent((n - 1) // 2 + 1) + recurrent((n - 1) // 2)


def ackermann(m, n):
    if m == 0:
        return (n + 1)
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))


def digitsum(n):
    array = []
    string = str(n)
    for x in string:
        array.append(int(x))
    return sum(array)

def reversestring(s):
    return s[::-1]

def perms(n):
    if not n:
        return

    for i in xrange(2**n):
        s = bin(i)[2:]
        s = "0" * (n-len(s)) + s
        yield s

def concatnumbers(n, m):
    array1 = []

    string1 = str(n)
    string2 = str(m)
    for x in string1:
        array1.append(int(x))
    for y in string2:
        array1.append(int(y))
    new = ''.join(map(str, array1))
    return new


def main():
    print(factorial(0))
    print(factorial(2))
    print(factorial(4))

    print(fibonacci(1))
    print(fibonacci(4))
    print(fibonacci(10))

    print(digitsum(0))
    print(digitsum(123))
    print(digitsum(192837465))

    s = ''
    print(reversestring(s))
    s= '1'
    print(reversestring(s))
    s= 'asdf'
    print(reversestring(s))
    s = 'abacaba'
    print(reversestring(s))

    print(ackermann(0, 10))
    print(ackermann(1, 1))
    print(ackermann(2, 2))
    print(ackermann(2, 5))
    print(ackermann(3, 3))

    print(recurrent(2))
    print(recurrent(3))
    print(recurrent(5))
    print(recurrent(7))

    print(concatnumbers(1, 2))
    print(concatnumbers(55, 88))
    print(concatnumbers(123, 789))
    print(concatnumbers(1000, 2))

main()
