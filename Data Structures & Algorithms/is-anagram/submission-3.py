class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
     # hashmap T: O(s + t) S: O(1)

        if len(s) != len(t):
            return False

        countS,countT = {},{}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        
        return countS == countT

     
     # hashtable T: O(s + t) S: O(1)

