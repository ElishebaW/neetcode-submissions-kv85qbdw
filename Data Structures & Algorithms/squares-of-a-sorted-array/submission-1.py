class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []

        left, right = 0, len(nums) - 1
        result = [0] * len(nums)
        pos = len(nums) - 1

        while left <= right:
            if (nums[left] ** 2) >= (nums[right] ** 2):
                result[pos] = nums[left] ** 2
                left += 1
            elif (nums[right] ** 2 ) > (nums[left] ** 2):
                result[pos] = nums[right] **2
                right -= 1
            pos -= 1
        
        return result
            
        