class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer = 0
        t_pointer = 0

        # Move through both strings
        while s_pointer < len(s) and t_pointer < len(t):
            # If the characters match, we found the next letter of s in t
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
            
            # Always move the t pointer forward
            t_pointer += 1

        # If we successfully matched all characters in s, s_pointer will equal len(s)
        return s_pointer == len(s)