import numpy as np


def getdimension(a):
    return a.ndim


def getdiagonal(a):
    return np.diagonal(a)


def cutarray(a, minvalue, maxvalue):
    return np.clip(a, minvalue, maxvalue)


def getmoments(a):
    return (np.mean(a), np.var(a))


def getdotproduct(a, b):
    return np.dot(a, b)


def checkequal(a, b):
    return a == b


def comparewithnumber(a, bound):
    return a < bound


def matrixproduct(a, b):
    return np.matmul(a, b)


def matrixdet(a):
    return np.linalg.det(a)


def getones(n, k):
    return np.eye(n, k=k)


def main():

    print(getdimension(np.array([1, 2, 3])))
    print(getdimension(np.array([[1], [2], [3]])))
    print(getdimension(np.array([[[[1]]]])))

    print(getdiagonal(np.array([[1, 2], [3, 4]])))

    print(cutarray(np.array([1, 2, 3, 4]), 2, 3))
    print(cutarray(np.array([1, 2, 3, 4]), 2, 3))

    print(getmoments(np.array([2, 1, 9])))

    print(getdotproduct(np.array([1, 2, 3]), np.array([4, 5, 6])))

    print(checkequal(np.array([1, 2, 3]), np.array([1, 5, 3])))

    print(comparewithnumber(np.array([[1, 2], [3, 4]]), 4))

    print(matrixproduct(np.array([[1, 2], [3, 4]]),
                        np.array([[5, 6], [7, 8]])))
    print(matrixproduct(np.array([[1, 2]]), np.array([[3], [4]])))

    print(matrixdet(np.array([[5, 6], [7, 8]])))
    print(matrixdet(np.array([[123]])))

    print(getones(3, 1))
    print(getones(3, 9))

main()
