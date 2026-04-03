class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # pair (index, height) missed
        max_area = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h: # missed the comparison
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index)) # missed making teh width
                start = index
            stack.append((start, h)) # used push rather than append and didn't push in a pair just start, h

        for i, h in stack: #missed checking the stack, you had heights
            max_area = max(max_area, h * (len(heights) - i)) # missed calculating the width

        return max_area