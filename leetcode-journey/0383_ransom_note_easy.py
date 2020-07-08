from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        ransom = defaultdict(int)
        mag = defaultdict(int)
        for c in ransomNote:
            ransom[c] += 1
        for c in magazine:
            mag[c] += 1
        return all(ransom[char] <= mag[char] for char in ransom.keys())


from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        counts = [0] * 26
        letters = 0
        for c in ransomNote:
            index = ord(c) - ord('a')
            if counts[index] == 0:
                letters += 1
            counts[index] += 1
        for c in magazine:
            index = ord(c) - ord('a')
            counts[index] -= 1
            if counts[index] == 0:
                letters -= 1
            if letters == 0:
                break
        return letters == 0