import sys
input = sys.stdin.readline

n = int(input())
moves = []

def hanoi(k, s, m, t):
    if k == 0: 
        return
    hanoi(k-1, s, t, m)
    moves.append(f"{s} {t}")
    hanoi(k-1, m, s, t)

hanoi(n, 1, 2, 3)
print(len(moves))
print("\n".join(moves))