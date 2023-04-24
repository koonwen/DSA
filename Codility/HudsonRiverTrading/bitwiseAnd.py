import random
from functools import reduce
from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def solution(A):
    subsets = powerset(A)
    max_so_far = 0
    for subset in subsets:
        res = reduce(lambda x, y: x & y, subset, ~0)
        if res > 0:
            max_so_far = max(max_so_far, len(subset))
    return max_so_far

from collections import Counter

def newSolution(A):
    c = Counter()
    for num in A:
        binrep = bin(num)[2:][::-1]
        for i, j in enumerate(binrep):
            c[i] += int(j)
    return c.most_common(2)[0][1]

def generate(n = 100000):
    arr = [0]*n
    for i in range(n):
        arr[i] = random.randint(1, 1000000000)
    return arr

if __name__ == '__main__':
    # A = [13, 7, 2, 8, 3]
    A1 = generate(20)
    # print(A1)
    print(solution(A1))
    print(newSolution(A1))
    print(newSolution([0,0,0]))