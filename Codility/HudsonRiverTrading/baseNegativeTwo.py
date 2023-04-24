from collections import deque

def helper(cur, num):
    q = deque()
    q.append((0, 1))
    while True:
        v, adder = q.popleft()
        if v == num:
            return
        q.append((v, adder*2))
        q.append((v + adder, adder*2))


def solution(A: int, B: int) -> int:
    return

if __name__ == '__main__':
    3334

    A = [0,1,1,0,0,1,0,1,1,1,0,1,0,1,1]
    B = [0,0,1,0,0,1,1,1,1,1,0,1]
    C = [0,1,0,1,1,0,0,0,1,0,1,1,1]