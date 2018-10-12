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


if __name__ == "__main__":

    assert unique([1, 2, 1, 3]) == [1, 2, 3], "unique Error!"
    assert unique({5, 1, 3}) == [1, 3, 5], "unique Error!"
    assert unique('adsfasdf') == ['a', 'd', 'f', 's'], "unique Error!"
    print("Asserted unique() function!")

    assert transposeDict({}) == {}, "transposeDict Error!"
    assert transposeDict({1: 'a', 2: 'b'}) == {'a': 1, 'b': 2}, \
        "transposeDict Error!"
    assert transposeDict({1: 1}) == {1: 1}, "transposeDict Error!"
    print("Asserted transposeDict() function!")

    assert mex([1, 2, 3]) == 4, "mex Error!"
    assert mex(['asdf', 123]) == 1, "mex Error!"
    assert mex([0, 0, 1, 0]) == 2, "mex Error!"
    print('Asserted mex() function!')

    assert frequencyDict('') == {}, "frequencyDict Error!"
    assert frequencyDict('abacaba') == {'a': 4, 'b': 2, 'c': 1}, \
        "frequencyDict Error!"
    print("Asserted frequencyDict() function!")


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
