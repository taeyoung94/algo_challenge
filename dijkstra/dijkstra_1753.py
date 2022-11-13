import sys
from collections import defaultdict
import heapq

def input():
    return sys.stdin.readline().rstrip()

v, e = map(int,input().split())

k = int(input())

INF = sys.maxsize

distance = [INF] * (v+1)

graph = defaultdict(list)

for _ in range(e):
    u, v, w = map(int,input().split())

    graph[u].append((v,w))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) 
    distance[start] = 0        
    while q:
        dist, node = heapq.heappop(q)

        if distance[node] < dist:
            continue
 
        for next in graph[node]:
            cost = distance[node] + next[1]   
            if cost < distance[next[0]]:      
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))


dijkstra(k)

for i in range(1, len(distance)):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])