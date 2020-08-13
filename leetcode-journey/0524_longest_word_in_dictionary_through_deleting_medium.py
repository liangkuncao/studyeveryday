class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d = sorted(d, key=lambda x: len(x), reverse=True)
        words = list()
        length = 0
        for word in d:
            p1, p2 = len(s) - 1, len(word) - 1
            while p1 >= 0 and p2 >= 0:
                if s[p1] == word[p2]:
                    p2 -= 1
                p1 -= 1
            if p2 < 0:
                if len(word) < length:
                    break
                length = len(word)
                words.append(word)

        return sorted(words)[0] if words else ''