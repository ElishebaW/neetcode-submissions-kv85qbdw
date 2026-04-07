class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # T: O(n + m ) - where n is the length of s and m is the length of t
        # S: O(1) - since there are only 26 lowercase letters(0(26) -> O(1)
        # The first way I'm thinking about this is to go through an array like the S array and add a value plus one for that ASCII character in the result array. 
        # Then I go through T and I subtract from that ASCII character position one. If everything is zero and there's no ones, then the words are anagrams of each other.
        #  If there are any spaces where there is a one, then they're not anagrams of each other. That means that there wasn't enough characters in T to cancel all S.
        #  It means that there is one extra character in T, or X number of characters extra in T, that make it so that S and T are not anagrams of each other. 
        if len(s) != len(t):
            return False
        res = [0] * 26

        for c in s:
            res[ord('a') - ord(c)] += 1

        for char in t:
            res[ord('a') - ord(char)] -= 1
        
        for num in res:
            if num > 0:
                return False
        
        return True