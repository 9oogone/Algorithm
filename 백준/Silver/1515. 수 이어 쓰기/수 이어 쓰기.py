import sys
input = sys.stdin.readline

s=input().strip()

# 숫자열을 받는다 (s)
# 숫자열의 길이가 필요하다 왜냐면 싹 돌아야 돼서
# n도 필요하다 n은 지워진 숫자나 있어야 할 숫자를 찾는 거임 무조건 1씩 증가 # idx의 수가 가리키는 원본임
#   숫자로 +=1 할 건데 비교는 str으로 바꿔서 해야 함 
# 종료조건은 len(s)-1번째 인덱스를 보고 있고, 거기서 찾았을 때(그럼 넘어가니까)
#   idx==len(s)-1 여기서 n값이 밝혀진다
#   
idx = 0 # s의 몇 번째 인덱스를 볼 건지
n=0 # 찾는 수 (와야 하는 자리 수)
while idx<len(s):
    n+=1
    for i in str(n):
        if s[idx]==i: # 주어진 수랑 찾는 수가 같으면 그리고 마지막 인덱스가 아니면
            idx+=1 #s 인덱스 변경
            # 같지 않으면 그 idx 계속 보는 거임
            
            # 종료조건 # out of range 방지
            if idx == len(s):
                break
print(n)