class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:


        """
        T: O(n^2)
        S: O(1)


        """
        n = len(edges)
        parent = [ i for i in range(n + 1)]
        result = []

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

        
        for a, b in edges:
            if find(a) == find(b):
                result = [a,b]
            else:
                union(a,b)
        
        return result
        