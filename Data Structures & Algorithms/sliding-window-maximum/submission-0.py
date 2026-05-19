class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_holder = []
        queue = deque([])

        for windowEnd in range(len(nums)):
            while queue and nums[queue[-1]] <= nums[windowEnd]:
                queue.pop()
            
            if queue and queue[0] <= windowEnd - k:
                queue.popleft()

            queue.append(windowEnd)

            if queue and windowEnd >= k-1:
                max_holder.append(nums[queue[0]])
            
        return max_holder


        