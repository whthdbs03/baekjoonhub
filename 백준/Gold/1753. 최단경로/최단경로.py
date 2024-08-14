#재제출
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
import heapq

V,e = map(int, input().split())
k=int(input())
INF= int(1e9) 
graph = [[] * (V+1) for _ in range(V+1)]
distance = [INF] * (V+1)

#간선 정보 입력
for _ in range(e):
    u, v, w = map(int, input().split())
    #u->v일때 w비용
    graph[u].append((v,w))
    
def dijkstra(start):
    q=[]
    #시작노드로 가기위한 최단경로는 0으로 설정, 큐에삽입
    heapq.heappush(q,(0, start))
    distance[start]=0

    while q:
        #가장 최단거리가 짧은 노드에대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        #현재노드가 이미처리된적있는 노드라면 무시
        if distance[now]< dist: continue
        #현재노드와 연결된 다른인접노드들확인
        for i in graph[now]:
            cost= dist+ i[1]
            #현재 노드를 거쳐서, 다른노드로이동하는거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘 수행
dijkstra(k)

#모든 노드로 가기 위한 최단거리 출력
for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
