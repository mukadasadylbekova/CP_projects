import sys
sys.setrecursionlimit(200000)

def solve():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    
    # Reading the edges
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    
    visited = [False] * n  # To keep track of visited nodes
    parent = [-1] * n  # To store the parent of each node in the DFS tree
    
    def dfs(v):
        visited[v] = True
        
        for neighbor in graph[v]:
            if not visited[neighbor]:
                parent[neighbor] = v
                if dfs(neighbor):
                    return True
            elif parent[v] != neighbor:  # Found a cycle
                cycle = []
                cycle.append(neighbor + 1)
                x = v
                while x != neighbor:
                    cycle.append(x + 1)
                    x = parent[x]
                cycle.append(neighbor + 1)
                cycle.reverse()
                print(len(cycle))
                print(" ".join(map(str, cycle)))
                return True
        return False
    
    for i in range(n):
        if not visited[i]:
            if dfs(i):
                return
    
    print("IMPOSSIBLE")

solve()
