import sys
input = sys.stdin.readline

N, K = map(int, input().split())
table = list(input().strip())

cnt = 0
for i in range(N):
    if table[i] == 'P':
        # i-K부터 i+K까지 범위 내에서 가장 먼저 발견되는 H를 찾음
        for j in range(max(0, i - K), min(N, i + K + 1)):
            if table[j] == 'H':
                table[j] = 'E' 
                cnt += 1
                break
print(cnt)