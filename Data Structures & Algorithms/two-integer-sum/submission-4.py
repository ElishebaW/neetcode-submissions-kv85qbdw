class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return []
        
        numsCount = {}

        for i , n in enumerate(nums):
            diff = target - n

            if diff in numsCount:
                return [numsCount[diff], i]

            numsCount[n] = i
       
        return []