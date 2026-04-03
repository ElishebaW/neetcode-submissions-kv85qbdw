class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p,s] for p,s in zip(position, speed)]
        stack = []

        for p,s in sorted(pairs)[::-1]: #missed negative for reverse
            stack.append((target - p)/ s) # missed parens on target - p, pushing total time of arrival
            if len(stack) >= 2 and stack[-1] <= stack[-2]: # less than or equal rather than greater than , used stack size rather than length, missed checking if the length is equal to 2
                stack.pop()
        
        return len(stack)