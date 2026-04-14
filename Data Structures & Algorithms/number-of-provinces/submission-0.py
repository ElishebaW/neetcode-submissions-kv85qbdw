from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        provinces = 0

        for i in range (len(isConnected)):
            if i not in visited:
                provinces += 1
                queue = deque([i])
                visited.add(i)
                while queue:
                    city = queue.popleft()

                    for j in range(len(isConnected[city])):
                        if isConnected[city][j] == 1 and j != city and j not in visited:
                            visited.add(j)
                            queue.append(j)
                   

        return provinces
        