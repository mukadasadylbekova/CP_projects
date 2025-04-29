class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

def solve():
    n, m = map(int, input().split())
    
    uf = UnionFind(n)
    
    for _ in range(m):
        a, b = map(int, input().split())
        uf.union(a-1, b-1)
    
    components = {}
    for i in range(n):
        root = uf.find(i)
        if root not in components:
            components[root] = []
        components[root].append(i + 1)
    
    component_list = list(components.values())
    new_roads = []
    
    for i in range(1, len(component_list)):
        new_roads.append((component_list[0][0], component_list[i][0]))
    
    print(len(new_roads))
    for road in new_roads:
        print(road[0], road[1])

solve()
