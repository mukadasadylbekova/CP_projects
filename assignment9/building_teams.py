from collections import deque

def solve():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    
    team = [-1] * n  # -1 means unvisited, 1 and 2 represent two teams
    possible = True
    
    def bfs(start):
        queue = deque([start])
        team[start] = 1  # Start by assigning team 1 to the first node
        while queue:
            node = queue.popleft()
            current_team = team[node]
            for neighbor in graph[node]:
                if team[neighbor] == -1:  # If unvisited, assign the opposite team
                    team[neighbor] = 2 if current_team == 1 else 1
                    queue.append(neighbor)
                elif team[neighbor] == current_team:  # If same team as the current node, it's impossible
                    return False
        return True

    for i in range(n):
        if team[i] == -1:  # If this node is unvisited, start a BFS from it
            if not bfs(i):
                possible = False
                break
    
    if possible:
        print(" ".join(map(str, team)))
    else:
        print("IMPOSSIBLE")

solve()
