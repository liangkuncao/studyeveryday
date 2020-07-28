class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0

        char_counter = {chr(i): 0 for i in range(ord('A'), ord('Z') + 1)}
        left, right, most_freq = 0, 0, 0
        res = 0
        while right < len(s):
            char = s[right]
            char_counter[char] += 1
            most_freq = max(most_freq, char_counter[char])

            while right - left + 1 > most_freq + k:
                char = s[left]
                char_counter[char] -= 1
                most_freq = max(char_counter.values())
                left += 1

            res = max(res, right - left + 1)
            right += 1
        return res


print(Solution().characterReplacement("AABABBA", 1))