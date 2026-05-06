class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool

        T: O (n + m) where n is the ransom note and m is the magazine

        S: O (n+m) where n is where the aschii values of n reside and m is the aschii values m reside in an array
        """
        a_ransom_note = [0] * 26

        for m in magazine:
            a_ransom_note[ord(m) - ord('a')] += 1

        for c in ransomNote:
            a_ransom_note[ord(c) - ord('a')] -= 1
            if a_ransom_note[ord(c) - ord('a')] < 0:
                return False

        return True
        