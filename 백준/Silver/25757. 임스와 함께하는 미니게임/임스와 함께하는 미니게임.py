import sys
input=sys.stdin.readline
n,game=input().split()
dict={'Y':1,'F':2,'O':3}
arr=set()
for i in range(int(n)):
    arr.add(input())

print(len(arr)//dict[game])
    