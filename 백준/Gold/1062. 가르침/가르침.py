import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,k = map(int,input().split()) # n개의 단어 k만큼의 시간
words = [input().strip() for _ in range(n)]

# 기본적으로 학습해야 하는 글자
# antic
# 문자열 슬라이스도 해도 될 듯? 백트래킹 관점에서

if k<5:
    print(0)
    sys.exit()

# 기본적으로 학습해야 하는 글자 학습해두기
basic = 0
for study in 'antic':
    basic |= (1<< (ord(study)-ord('a')))

# 주어진 단어들의 [4:-4]만 슬라이스해서 비트로 만들어서 저장해두기
wm = []
for word in words:
    mask = 0
    for i in word[4:-4]:
        mask |= (1 <<((ord(i)-ord('a'))))
    wm.append(mask)

ans = 0

def dfs(start,learn_cnt,study):
    global ans
    if learn_cnt == k:
        cnt = 0
        for word in wm:
            if word & ~study == 0:
                cnt += 1
        ans = max(ans,cnt)
        return

    for i in range(start, 26):
        if not (study & (1 << i)):
            dfs(i+1,learn_cnt+1,study | (1 << i))

dfs(0,5,basic)
print(ans)