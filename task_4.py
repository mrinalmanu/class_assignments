
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

def digitsum(n):
    array = []
    string = str(n)
    for x in string:
        array.append(int(x))
    return sum(array)


