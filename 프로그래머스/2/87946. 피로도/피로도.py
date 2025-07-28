def solution(k, dungeons):
    answer = 0
    visited = [0 for _ in range(len(dungeons))]
    
    def game(k,cnt):
        nonlocal answer
        answer = max(answer,cnt)
        
        for i in range(len(dungeons)):
            if not visited[i] and k >= dungeons[i][0]:
                visited[i] = 1
                game(k - dungeons[i][1],cnt+1)
                visited[i] = 0
    
    game(k,0)
    
    return answer