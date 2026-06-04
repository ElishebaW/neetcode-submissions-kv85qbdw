class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_pair = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if target_pair and complement in target_pair and target_pair[complement] != i:
                return [target_pair[complement], i]
            
            target_pair[nums[i]] = i
        
        return []

        