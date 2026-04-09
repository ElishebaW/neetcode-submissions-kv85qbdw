class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) -1

        while left <= right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
            elif not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -=1
        return True





        """
        strip the string of all whitespaces and non alphaCharacters, but that would be O in time with O in space, because with the stripping it creates an extra string in memory and that would make it more memory intensive.

        Another way is to use a two-pointer technique, which we can use with O time complexity and the space complexity would be one. As we're 
        going through the two pointers to stop from this, how the two-pointer algorithm will work is we start from the beginning of the string and at the end of 
        the string and move towards the middle. At each point, we check if the left is alphanumeric. If it's not, we can continue on. If the right is not alphanumeric, 
        then we continue on to the right.
        Once we have two non-alphanumeric letters, we take a comparison to see if they are the same, and that's time O(N) and space O(1). 
        """




        