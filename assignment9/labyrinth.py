from collections import deque


DIRECTIONS = [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]

def bfs(n, m, grid, start, end):
    
    queue = deque([(start[0], start[1], '')])
    visited = set()
    visited.add(start)
    
    while queue:
        x, y, path = queue.popleft()
        
        
        if (x, y) == end:
            return True, len(path), path
        
       
        for dx, dy, move in DIRECTIONS:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited and grid[nx][ny] != '#':
                visited.add((nx, ny))
                queue.append((nx, ny, path + move))
    
    return False, 0, ""

def solve():
    
    n, m = map(int, input().split())
    grid = [input().strip() for _ in range(n)]
    
   
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'A':
                start = (i, j)
            elif grid[i][j] == 'B':
                end = (i, j)
    
    
    found, path_length, path = bfs(n, m, grid, start, end)
    
    if found:
        print("YES")
        print(path_length)
        print(path)
    else:
        print("NO")


solve()

