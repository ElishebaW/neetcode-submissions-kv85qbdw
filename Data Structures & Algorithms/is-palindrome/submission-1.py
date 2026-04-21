class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        T: O(n) = where n is the length of s
        S: O(1) = don't need additional data structures
        """
        left = 0
        right = len(s) - 1

        while left <= right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            else:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1

        return True


        