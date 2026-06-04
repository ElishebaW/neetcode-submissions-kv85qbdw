class Solution:
    def maxProduct(self, nums: List[int]) -> int:  
        max_prod = nums[0]
        min_prod = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            new_max = max(nums[i], nums[i] * max_prod, nums[i] * min_prod)
            new_min = min(nums[i], nums[i] * max_prod, nums[i] * min_prod)
            max_prod = new_max
            min_prod = new_min
            result = max(max_prod, result)

        return result
        