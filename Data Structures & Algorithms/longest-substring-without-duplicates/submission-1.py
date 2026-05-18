class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        freq = {}
        windowStart = 0

        for i in range(len(s)):
            if s[i] in freq and freq[s[i]] >= windowStart:
                windowStart = freq[s[i]] + 1
            freq[s[i]] = i
            longest = max(longest,i - windowStart + 1)
                
        
        return longest