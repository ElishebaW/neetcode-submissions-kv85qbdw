class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        T: O(n ^ 2)
        S: O ( 1)
        #Union find techiue because it perfectly first into the disjointed graph pattern

        """
        n = len(isConnected)

        parent = [i for i in range(n)]

        def find(node):
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        def union(a,b):
            rootA = find(a)
            rootB = find(b)

            if rootA != rootB:
                parent[rootB] = rootA
        
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    union(i,j)

        provinces = 0

        for i in range(len(parent)):
            if parent[i] == i:
                provinces += 1
        
        return provinces
        