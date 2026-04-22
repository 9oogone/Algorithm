import sys
import heapq

input = sys.stdin.readline

# 델타 (전역)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 다익스트라 (전역)
def dijkstra(n, graph, distance):
    q = []
    # 시작점 (0,0)의 도둑루피 값을 초기 비용으로 설정
    start_cost = graph[0][0]
    distance[0][0] = start_cost
    # 힙큐에는 (누적 비용, x좌표, y좌표) 순으로 삽입
    heapq.heappush(q, (start_cost, 0, 0))

    while q:
        dist, x, y = heapq.heappop(q)

        # 현재 꺼낸 비용이 기록된 비용보다 크다면 이미 처리된 것이므로 무시
        if distance[x][y] < dist:
            continue

        # 상하좌우 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                # 다음 칸까지의 누적 비용 계산
                cost = dist + graph[nx][ny]
                # 기존에 기록된 비용보다 저렴할 경우에만 갱신 후 큐에 삽입
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))
    
    return distance[n-1][n-1]

# 메인 실행부
problem_count = 1
while True:
    line = input().strip()
    if not line:
        break
    n = int(line)
    if n == 0:
        break

    # 동굴 (도둑루피 격자)
    graph = [list(map(int, input().split())) for _ in range(n)]
    # 비용 누적 장부 (무한대로 초기화)
    distance = [[int(1e9)] * n for _ in range(n)]

    result = dijkstra(n, graph, distance)
    
    print(f"Problem {problem_count}: {result}")
    problem_count += 1