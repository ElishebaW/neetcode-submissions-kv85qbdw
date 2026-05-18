class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        pattern = []

        while x:
            digit = x % 10
            pattern.append(digit)

            x //= 10
        
        left = 0
        right = len(pattern) - 1

        while left < right:
            if pattern[right] != pattern[left]:
                return False
            left += 1
            right -= 1
    
        
        return True
        