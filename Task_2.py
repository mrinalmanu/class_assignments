def listToString(n):
    return str(n)

def shorting(n):
    x = []
    for i in range(len(n)):
        if len(n[i]) <= 10:
            x.append(i)
        else:
            n[i] = n[i][0] + str(len(n[i]) - 2) + n[i][len(n[i]) - 1]
            x.append(n[i])
    return x

def competition(score, k):
    next_round = 0
    for i in range(len(score)):
        if score[i] >= score[k] and score[i] > 0: #score at i greater than or equal to k
            next_round += 1
    return next_round

def goodPairs(a, b):
    pair_list = []
    for i in a:
        for j in b:
            if (i*j)%(i+j) ==0:
                good_pair = (i*i + j*j)
                if good_pair not in pair_list:
                    pair_list.append(good_pair)
    pair_list.sort()
    return pair_list

def makeShell(n):
    shell = []
    for i in range(int(n)):
        shell.append([0] * (i + 1))
    for j in range(int(n-1),0,-1):
        shell.append([0] * j)
    return shell

def addborder(a):
    assert type(a) == list
    up_to_down = a
    right_to_left = max(len(x) for x in up_to_down)
    wrap = ['+'+'-'*right_to_left+'+']
    for x in up_to_down:
        wrap.append('|'+(x+'-'*right_to_left)[:right_to_left]+'|')
    wrap.append('+'+'-'*right_to_left+'+')
    return '\n'.join(wrap)


def main():
    print(listToString([]))
    print(listToString([1, 2, 3]))
    print(listToString([-5]))

    print(shorting(['word', 'localization', 'internationalization',
              'pneumonoultramicroscopicsilicovolcanoconiosis']))

    print(competition([5, 4, 3, 2, 1], 2))
    print(competition([1, 0, 0, 0], 3))
    print(competition([10, 9, 8, 7, 7, 7, 5, 5], 4))

    print(goodPairs([4, 5, 6, 7, 8], [8, 9, 10, 11, 12]))
    print(goodPairs([2], [2]))
    print(goodPairs([7, 8, 9], [5, 3, 2]))

    print(makeShell(1))
    print(makeShell(2))
    print(makeShell(3))

main()
