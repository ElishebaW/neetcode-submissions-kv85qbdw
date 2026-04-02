class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #2 pointer algp 
        # T: O (n)
        # S: O(n)

        elem = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in elem:
                return [elem[complement], i]

            elem[nums[i]] = i

        return -1

        
      