
def unique(e):
    y = list(e)
    #this function returns sorted list of distinct elements of a set 'e'
    y.sort()
    output = []
    for x in y:
        if x not in output:
            output.append(x)
    print(output)
    return e

def transposeDict(d):
    #this function shall return a transposed dictionary 'd'
    this = print(dict([(value, key) for key, value in d.items()]))
    return this



def mex(a):

    #this function returns the minimal positive integer not present in the list a
    b = print(min(set(range(1, len(a) + 2)).difference(set(a))))
    return b


def frequencyDict(dictionary):
    reference = {}
    for element in dictionary:
        keys = reference.keys()
        if element in keys:
            reference[element] += 1
        else:
            reference[element] = 1
    z = print(reference)
    return z

def main():
    unique([1, 2, 1, 3])
    unique({5, 1, 3})
    unique('adsfasdf')

    transposeDict({1: 'a', 2: 'b'})
    transposeDict({1: 1})
    transposeDict({})

    frequencyDict('')
    frequencyDict('abacaba')

    mex([1, 2, 3])
    mex(['asdf', 123])
    mex([0, 0, 1, 0])


main()
