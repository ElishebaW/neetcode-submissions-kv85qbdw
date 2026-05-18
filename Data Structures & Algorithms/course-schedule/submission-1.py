class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj_list = defaultdict(list)

        for a, b in prerequisites:
            indegree[a] += 1
            adj_list[b].append(a)

        queue = deque([i for i in range(numCourses) if indegree[i] == 0])

        counter = 0
        while queue:
            course = queue.popleft()

            counter += 1

            for num in adj_list[course]:
                indegree[num] -= 1
                if indegree[num] == 0:
                    queue.append(num)


        return counter == numCourses