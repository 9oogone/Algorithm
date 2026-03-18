import sys
input = sys.stdin.readline

ary = input().strip()
boom = input().strip()
lb = len(boom)

stack = []

for i in ary:
    if stack:
        last=stack[-1]
        prev=last[1]
    else:
        prev=0
    
    # 현재 문자의 매칭 카운트 결정
    if i == boom[prev]:
        cnt=prev+1
    elif i == boom[0]:
        cnt=1
    else:
        cnt=0
        
    # stack저장
    stack.append((i,cnt))
    
    # 폭발 조건 확인 
    if cnt == lb:
        for j in range(lb):
            stack.pop()

if not stack:
    print("FRULA")
else:
    ans=[]
    for i in stack:
        ans.append(i[0])
    print("".join(ans))