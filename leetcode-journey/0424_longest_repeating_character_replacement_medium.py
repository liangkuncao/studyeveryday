class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0

        letter_counts = [0 for _ in range(26)]
        res = 0
        left = right = 0
        most_frequent = 0
        while right < len(s):
            letter = s[right]
            letter_counts[ord(letter) - ord('A')] += 1
            most_frequent = max(letter_counts)
            while right - left + 1 > most_frequent + k:
                letter = s[left]
                letter_counts[ord(letter) - ord('A')] -= 1
                most_frequenct = max(letter_counts)
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res
