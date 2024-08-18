import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

import heapq
n,m=map(int,input().split()) #노드1에서 n까지최단거리구하기
#di={}
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split()) #a와b를잇는길의비용:c
    '''if a>b:
        x=a
        a=b
        b=x
        #a<b무조건ㅇㅇ
    if not di[(a,b)]: di[(a,b)]=[]
    heapq.heappush(di[(a,b)], c)
    #디렉토리에 ab잇는비용c저장 ㅇㅇ'''
    graph[a].append((b,c))
    graph[b].append((a,c))
    #서로에 대해 길이 저장

INF=int(1e9)
dist=[INF]*(n+1) #여기에 각 노드까지의 최단거리 저장할것임.

def dijkstra(start):
    visit=[]
    q=[]
    heapq.heappush(q,(0, start))
    dist[start]=0

    while q:
        distance, now= heapq.heappop(q)
        #if now in visit: continue
        if distance> dist[now]: continue
        for i in graph[now]:
            cost= distance + i[1]
            if cost< dist[i[0]]:
                dist[i[0]]=cost
                heapq.heappush(q,(cost, i[0]))
        visit.append(now)

dijkstra(1)
print(dist[n])