class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        window = set()
        res = 0
        while left <= right < len(s):
            if s[right] in window:
                window.discard(s[left])
                left += 1
                continue
            window.add(s[right])
            right += 1
            res = max(res, right - left)
        return res


print(Solution().lengthOfLongeubstring("bbtablud"))

