from collections import deque

def solve():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    
    dist = [-1] * n
    parent = [-1] * n
    queue = deque([0])  # Uolevi's computer is 1, which is index 0
    dist[0] = 0
    
    while queue:
        current = queue.popleft()
        
        for neighbor in graph[current]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[current] + 1
                parent[neighbor] = current
                queue.append(neighbor)
    
    if dist[n-1] == -1:
        print("IMPOSSIBLE")
    else:
        path = []
        current = n - 1
        while current != -1:
            path.append(current + 1)
            current = parent[current]
        
        path.reverse()
        print(len(path))
        print(" ".join(map(str, path)))

solve()
