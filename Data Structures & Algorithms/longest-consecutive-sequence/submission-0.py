class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestSeq = 0

        for num in nums:
            if num - 1 not in numSet:
                currSeq = 1
                currNum = num 
                while currNum + 1 in numSet:
                    currSeq += 1
                    currNum += 1
                longestSeq = max(currSeq, longestSeq)
        
        return longestSeq

