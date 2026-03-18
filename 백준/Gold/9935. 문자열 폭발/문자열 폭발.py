import sys
input = sys.stdin.readline

ary = input().strip()
boom = input().strip()
l = len(boom)
last_char = boom[-1] # 폭발 문자열의 마지막 글자

stack = []

for i in ary:
    stack.append(i)
    
    # 1. 현재 추가된 문자가 폭발 문자열의 끝과 같고
    # 2. 스택의 길이가 폭발 문자열보다 길거나 같을 때만 검사
    if i == last_char and len(stack) >= l:
        if "".join(stack[-l:]) == boom:
            for _ in range(l):
                stack.pop()

if not stack:
    print("FRULA")
else:
    print("".join(stack))