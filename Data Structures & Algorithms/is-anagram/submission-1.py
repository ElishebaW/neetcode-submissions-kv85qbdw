class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # one option is to sort and then go through each word to see if
        # they are anagrams of each other T: O(n log n + n + m) S: O(1)
        # another option is to put the words into an array with a hash table at their index and seee if the 
        # index is the same T: O(n + m) S: O(n + m)
        #hash map the same but with hashmap , there are underlying data structures so 

        # if (len(s) != len(t)):
        #     return False

        # countT, countS = {}, {}

        # ## you need multiple dictionies if you declere multiple vars

        # for i in range(len(s)):
        #     countT[t[i]] = countT.get(t[i], 0) + 1
        #     countS[s[i]] = countS.get(s[i], 0) + 1

        # for c in countS:
        #     if countS[c] != countT.get(c, 0):
        #         return False

        # return True



        if (len(s) != len(t)):
            return False

        countT, countS = {}, {}

        ## you need multiple dictionies if you declere multiple vars

        for i in range(len(s)):
            countT[t[i]] = countT.get(t[i], 0) + 1
            countS[s[i]] = countS.get(s[i], 0) + 1

        return countT == countS


       