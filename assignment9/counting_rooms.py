# Используем DFS для поиска комнат
def dfs(x, y, n, m, grid, visited):
    # Стек для DFS
    stack = [(x, y)]
    visited[x][y] = True
    
    # Соседние клетки (вверх, вниз, влево, вправо)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while stack:
        cx, cy = stack.pop()
        
        # Проходим по всем соседним клеткам
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            
            # Проверяем, чтобы новая клетка была внутри карты и была полом
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '.' and not visited[nx][ny]:
                visited[nx][ny] = True
                stack.append((nx, ny))

def count_rooms(n, m, grid):
    # Массив для отслеживания посещённых клеток
    visited = [[False] * m for _ in range(n)]
    
    room_count = 0
    
    # Ищем все комнаты
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.' and not visited[i][j]:
                # Нашли новую комнату, начинаем DFS
                dfs(i, j, n, m, grid, visited)
                room_count += 1
    
    return room_count

# Чтение входных данных
n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

# Выводим количество комнат
print(count_rooms(n, m, grid))
