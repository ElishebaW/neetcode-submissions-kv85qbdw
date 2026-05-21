class Solution:
    def validPalindrome(self, s: str) -> bool:
        # tw o pointer
        # if the characters don't match at a certain point
        # increase a counter
        # at the end see if the counter is less than 1
#  "abbda" 1

        def isPalindrome(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return isPalindrome(s, left + 1, right) or isPalindrome(s, left, right - 1)
            left += 1
            right -= 1


        return True