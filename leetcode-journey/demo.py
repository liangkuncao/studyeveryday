from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 1
        window = set()
        res = 0
        while left <= right < len(s):
            if s[right] in window:
                window.remove(s[left])
                left += 1
                continue
            window.add(s[right])
            right += 1
            res = max(res, right - left)
        return res


print(Solution().findKthPositive(arr = [2,3,4,7,11], k = 5))