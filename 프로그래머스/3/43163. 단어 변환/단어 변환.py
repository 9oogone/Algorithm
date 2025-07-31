from collections import deque

def solution(begin, target, words):
    # 최단 변환 과정이니까 아마 bfs같긴 한데
    # 1. 한 번에 한 개의 알파벳만 바꿔서 word에 있는 단어로 만들어야 됨
    # 2. word에 있는 단어로 바꾸는 과정을 겪으며 target에 도달해야 됨
    
    # 3. word에 target이 없으면 볼 필요도 없음
    if target not in words:
        return 0
    visited = [False]*len(words)

    q = deque()
    q.append((begin,0))

    while q:
        standard, cnt = q.popleft()
        # 타겟 도달하면 반환
        if standard == target:
            return cnt
        
        for idx, compare in enumerate(words):
            if not visited[idx]:
                diff = sum(1 for s,c in zip(standard,compare) if s!=c)
                if diff == 1:
                    visited[idx] = True
                    q.append((compare, cnt+1))
                    

                