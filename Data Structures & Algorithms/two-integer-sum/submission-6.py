class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_pos = {}

        for i, num in enumerate(nums):
            complement = target - num

            if num_pos and complement in num_pos:
                return [num_pos[complement], i]
            
            num_pos[num] = i

        return []
        