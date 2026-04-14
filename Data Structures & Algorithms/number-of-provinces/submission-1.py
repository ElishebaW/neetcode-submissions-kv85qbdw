class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [i for i in range(n)]
        provinces = 0
        def find(node):
            while parent[node] != node:
                node = parent[node]
            
            return node
            
        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            if rootA != rootB:
                parent[rootB] = rootA

        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1 and i != j:
                    union(i, j)

        for i in range(len(isConnected)):
            if parent[i] == i:
                provinces += 1

        return provinces

        