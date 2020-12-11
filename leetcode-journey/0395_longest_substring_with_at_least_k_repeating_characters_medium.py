class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        res = 0
        for i in range(1, len(set(s)) + 1):
            times = [0] * 26
            l = r = ct = dif_ct = 0
            while r < len(s):
                idx = ord(s[r]) - ord('a')
                times[idx] += 1
                if times[idx] == 1:
                    dif_ct += 1
                if times[idx] == k:
                    ct += 1

                while l <= r and dif_ct > i:
                    idx = ord(s[l]) - ord('a')
                    if times[idx] == k:
                        ct -= 1
                    if times[idx] == 1:
                        dif_ct -= 1
                    times[idx] -= 1
                    l += 1

                if ct == dif_ct == i:
                    res = max(res, r - l + 1)

                r += 1
        return res