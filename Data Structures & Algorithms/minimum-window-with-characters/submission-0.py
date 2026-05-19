class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freq = defaultdict(int)

        for c in t:
            t_freq[c] += 1

        need = len(t_freq)
        have = 0

        window_freq = defaultdict(int)
        windowStart = 0

        result = ""
        result_len = float("inf")
        
        for windowEnd in range(len(s)):
            window_freq[s[windowEnd]] += 1

            if t_freq[s[windowEnd]] == window_freq[s[windowEnd]]:
                have += 1

            while have == need:
                if windowEnd - windowStart + 1 < result_len:
                    result_len = windowEnd - windowStart + 1
                    result = s[windowStart:windowEnd + 1]

                c = s[windowStart]
                window_freq[c] -= 1
                if c in t_freq and window_freq[c] < t_freq[c]:
                    have -= 1
                windowStart += 1

        return result