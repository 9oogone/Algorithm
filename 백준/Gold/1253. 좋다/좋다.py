import sys
input=sys.stdin.readline

N=int(input())
ary=list(map(int,input().split()))
ary.sort()
l=len(ary)
good = 0

def search(i):
    left = 0
    right = l-1
    while left < right:
        if left == i:
            left += 1
        elif right == i:
            right -= 1
        else:
            s=ary[left]+ary[right]
            if s == ary[i]:
                return True
            else:
                if s<ary[i]:
                        left += 1
                else:
                    right -= 1
    return False
for target in range(l):
    if search(target):
        good += 1

print(good)