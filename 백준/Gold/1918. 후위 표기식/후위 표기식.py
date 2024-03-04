fx = input() # 중위 표기식 입력
stack = []
postfix = ''

# 연산자 우선순위 정의
priority = {'+': 1, '-': 1, '*': 2, '/': 2}

for tk in fx:
    if tk.isalnum():
        postfix += tk  # 피연산자일 경우 바로 출력
    elif tk == '(':
        stack.append(tk)
    elif tk in '+-*/':
        while stack and priority.get(stack[-1], 0) >= priority[tk]: # 스택의 top이 현재 연산자보다 우선순위가 높으면 pop
            postfix += stack.pop()
        stack.append(tk)
    elif tk == ')':
        while stack and stack[-1] != '(':
            postfix += stack.pop()
        stack.pop()  # '(' 제거

# 남은 연산자들을 모두 출력
while stack:
    postfix += stack.pop()

print(postfix)  # 후위 표기식 출력
