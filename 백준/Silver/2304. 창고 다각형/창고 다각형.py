import sys
input = sys.stdin.readline

N = int(input())
d = {}
for _ in range(N):
    x, h = map(int, input().split())
    d[x] = h

sd = sorted(d.items())
n = len(sd)
area = 0

left_idx = 0
base_x, base_h = sd[left_idx]

while True:
    next_idx = left_idx + 1
    while next_idx < n and sd[next_idx][1] < base_h:  
        next_idx += 1

    if next_idx == n:
        pivot_idx = left_idx
        break

    next_x, next_h = sd[next_idx]
    width = next_x - base_x
    area += base_h * width

    left_idx = next_idx
    base_x, base_h = next_x, next_h

right_idx = n - 1
base_x, base_h = sd[right_idx]

while True:
    next_idx = right_idx - 1
    while next_idx >= pivot_idx and sd[next_idx][1] < base_h:  
        next_idx -= 1

    if next_idx < pivot_idx:
        break

    next_x, next_h = sd[next_idx]
    width = base_x - next_x
    area += base_h * width

    right_idx = next_idx
    base_x, base_h = next_x, next_h

area += sd[pivot_idx][1]

print(area)
