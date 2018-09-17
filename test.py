
def unique(e):
    #this function returns sorted list of distinct elements of a set 'e'
    e.sort()
    return e

#Test
e = [1,4,22,13,6]
print(unique(e))

def transposeDict(d):
    #this function shall return a transposed dictionary 'd'
    return dict([(value, key) for key, value in d.items()])

#test
d = {'a':'apple','b':'ball','c':'cat','d':'dog'}
print(d)
print(transposeDict(d))

def mex(a):
    #this function returns the minimal positive integer not present in the list a
    a.sort()
    b = a[-1] + 1
    return b

#test

a = [4,7,81,2,3]
print(mex(a))

def frequencyDict(dictionary):
    reference = {}
    for element in dictionary:
        keys = reference.keys()
        if element in keys:
            reference[element] += 1
        else:
            reference[element] = 1
    return reference

#test

dictionary = 'adasdasnoidajsdo'
print(frequencyDict(dictionary))
