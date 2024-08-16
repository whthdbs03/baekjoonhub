import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

import heapq

n,m,k,x=map(int,input().split()) #도시개수,도로개수,거리,출발
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
#print(graph[1][0])
INF=int(1e9)
dist=[INF]*(n+1)
def dijkstra(start):
    q=[]
    heapq.heappush(q,(0, start))
    dist[start]=0

    while q:
        distance, now= heapq.heappop(q)
        if distance> dist[now]: continue
        for i in graph[now]:
            cost= distance + 1
            if cost< dist[i]:
                dist[i]=cost
                heapq.heappush(q,(cost, i))

dijkstra(x)
ans=0
for i in range(1, n+1):
    if dist[i]==k:
        print(i)
        ans+=1
if ans==0: print(-1)