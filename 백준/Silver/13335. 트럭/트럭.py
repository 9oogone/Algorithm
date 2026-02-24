import sys
input=sys.stdin.readline
from collections import deque

n,w,l = map(int,input().split())
weight=deque(map(int,input().split()))

def simulation():
    bridge=deque([0]*w) # 다리 빈 자리
    time = 0 # 시간 재기
    wm = 0 # 다리 위 트럭들의 현재 총 무게 
    
    # 다리 위의 일
    while weight or wm>0:
        time += 1
        
        left = bridge.popleft()
        wm -= left
    
        # 다리 진입    
        if weight: # 아직 다 못 지나갔으면
            if wm+weight[0]<=l: # 하중 되면
                truck=weight.popleft()
                bridge.append(truck)
                wm += truck
            else: # 하중 안 되면
                bridge.append(0)
    return time
print(simulation())