def unique(e):
    y = list(e)
    # this function returns sorted list of distinct elements of a set 'e'
    y.sort()
    output = []
    for x in y:
        if x not in output:
            output.append(x)
    output
    return output


def transposeDict(d):
    # this function shall return a transposed dictionary 'd'
    return dict([(value, key) for key, value in d.items()])


def mex(a):
    # this function returns the minimal positive integer not
    # present in the list a
    return min(set(range(1, len(a) + 2)).difference(set(a)))


def frequencyDict(dictionary):
    reference = {}
    for element in dictionary:
        keys = reference.keys()
        if element in keys:
            reference[element] += 1
        else:
            reference[element] = 1
    return reference


def main():
    print(unique([1, 2, 1, 3]))
    print(unique({5, 1, 3}))
    print(unique('adsfasdf'))

    print(transposeDict({1: 'a', 2: 'b'}))
    print(transposeDict({1: 1}))
    print(transposeDict({}))

    print(frequencyDict(''))
    print(frequencyDict('abacaba'))

    print(mex([1, 2, 3]))
    print(mex(['asdf', 123]))
    print(mex([0, 0, 1, 0]))


main()
