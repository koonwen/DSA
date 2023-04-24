import random


def count(S):
    return sum(alpha == 'a' for alpha in S)


def solution(S):
    mySet = set()
    p1 = 1
    while (p1 != len(S)-1):
        for p2 in range(p1+1, len(S)):
            fst, snd, thrd = S[0:p1], S[p1:p2], S[p2:len(S)]
            num = count(fst)
            if count(snd) == num and count(thrd) == num:
                mySet.add((S[0:p1], S[p1:p2], S[p2:len(S)]))
        p1 += 1
    return len(mySet)


def newSolution(S):
    first = 1 if S[0] == 'a' else 0
    second = 1 if S[1] == 'a' else 0
    third = sum(1 for i in range(2, len(S)) if S[i] == 'a')
    count = 0
    p1 = 0
    p2 = 1
    while p1 < p2 and second <= third:
        print(first,second, third)
        print("PTRS", p1, p2)
        if first == second and second == third:
            count += 1

        while p2 < len(S)-1 and second < third:
            p2 += 1
            if S[p2] == 'a':
                second += 1
                third -= 1
        else:
            p1 += 1
            if S[p1] == 'a':
                first += 1
                second -= 1
    return count

def generate(n=40000):
    s = ""
    for _ in range(n):
        s += random.choice(['a','b'])
    return s


if __name__ == '__main__':
    S = "babaa"
    S2 = "ababa"
    # S1 = generate(1000)
    # print(S1)
    # print(solution(S1))
    print(newSolution(S2))