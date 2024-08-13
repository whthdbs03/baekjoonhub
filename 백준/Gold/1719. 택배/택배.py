import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

import heapq

# 노드200, 경로10000
n, m = map(int, input().split())

# 무한을 의미하는 INF
INF = int(1e9)

# 그래프 초기화
graph = [[] for _ in range(n+1)]

# 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    # a<->b가 c비용
    graph[a].append((b, c))
    graph[b].append((a,c))

def find(target):
    
    if target == ans[target]:
        return target
    #경로 압축 최적화 - 부모노드로 모두 집합!!
    ans[target]=find(ans[target])
    return ans[target]

def dijkstra(ans, start):
    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [INF] * (n+1)
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    ans[start] = start # 자기자신으로 갈때 가장 짧은길 -

    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                ans[i[0]] = now

    for i in range(n): # 자기 부모 타고타고 최종 부모
        if ans[i+1] == start:
            ans[i+1] = i+1
    for i in range(n):        
        ans[i+1] = find(i+1)                
    return ans


ans_gragh = [] # 이따 하나씩 채우자

# 다익스트라 알고리즘을 수행
for k in range(n):
    ans = [[] for _ in range(n+1)] # 자기 최종부모 저장
    '''자기 앞 부모 저장하는 시점. 여기가 가장 짧은 거리임을 확인한 순간.
    '''
    ans_gragh.append(dijkstra(ans, k+1))
    
# 다익스트라 한번 돌면 그 노드에 대해 모든 노드로가기위한 최단거리가 저장됨.
''' 내가 필요한건 걔네들이 맨 처음 간 노드...
그냥 자기 앞 노드 저장. 타고타고 올라가서 한방향트리의 부모노드 찾기마냥...
union-find를 쓰는게 빠를까 나쁠까...

'''
for i in range(n):
    for j in range(n):
        if j == i:
            print('-',end=' ')
        else:
            print(ans_gragh[i][j+1],end=' ')
    print()