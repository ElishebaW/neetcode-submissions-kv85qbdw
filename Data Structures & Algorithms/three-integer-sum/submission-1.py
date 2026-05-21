class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        result = []
        
        for i in range(len(sortedNums)):
            if i > 0 and sortedNums[i] == sortedNums[i - 1]:
                continue
            left = i + 1
            right = len(sortedNums) - 1
            
            while left < right:
                sum = sortedNums[left] + sortedNums[i] + sortedNums[right]
                if sum == 0:
                    result.append([sortedNums[i], sortedNums[left], sortedNums[right]])
                    while left < right and sortedNums[left] == sortedNums[left + 1]:
                        left += 1
                    while left < right and sortedNums[right] == sortedNums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    right -= 1
        
        return result
