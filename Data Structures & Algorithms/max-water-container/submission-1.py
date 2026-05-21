class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = float("-inf")

        while left < right:
            minHeight = min(heights[left], heights[right])
            currMaxArea = minHeight * (right - left)
            maxArea = max(currMaxArea, maxArea)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return maxArea