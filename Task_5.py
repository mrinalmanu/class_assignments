def permutations(n, elements=[]):
    def generate(n, elements=[]):
        if len(elements) == n:
            yield tuple(elements)
        else:
            s = set(elements)
            for i in range(1, n + 1):
                if i not in s:
                    yield from generate(n, elements + [i])
    return list(generate(n))


def correctbracketsequences(n):
    def generate(n, elements='', balance=0):
        if len(elements) == 2 * n and balance == 0:
            yield elements
        else:
            for i in ('(', ')'):
                new_elements = elements + i
                new_balance = balance + (1 if i == '(' else -1)
                if len(new_elements) <= 2 * n and new_balance >= 0:
                    yield from generate(n, new_elements, new_balance)
    return list(generate(n))


def combinationswithrepeats(n, k):

    def generate(n, k, elements=[]):
        if len(elements) == k:
            yield tuple(elements)
        else:
            m = max(elements) if len(elements) > 0 else 1
            for i in range(m, n + 1):
                yield from generate(n, k, elements + [i])
    return list(generate(n, k))


def unorderedpartitions(n):
    def generate(n, elements=[]):
        if sum(elements) == n:
            yield tuple(elements)
        else:
            m = elements[-1] if len(elements) > 0 else 1
            for i in range(m, n - m + 2):
                new_elements = elements + [i]
                if sum(new_elements) <= n:
                    yield from generate(n, elements + [i])
    return list(generate(n))


def main():
    print(permutations(1))
    print(permutations(2))
    print(permutations(3))

    print(correctbracketsequences(1))
    print(correctbracketsequences(2))
    print(correctbracketsequences(3))

    print(combinationswithrepeats(1, 1))
    print(combinationswithrepeats(2, 2))
    print(combinationswithrepeats(3, 2))

    print(unorderedpartitions(1))
    print(unorderedpartitions(3))
    print(unorderedpartitions(5))


main()
