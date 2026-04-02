class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''

        res = ""

        for s in strs:
            res += str(len(s)) + '#' + s

        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            first_elem = j +1
            last_elem = j + 1 + length
            res.append(s[first_elem : last_elem])
            i = last_elem

        return res
