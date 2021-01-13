class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        def compare(word1: str, word2: str) -> int:
            LESS, EQUAL, GREATER = -1, 0, 1
            for c1, c2 in zip(word1, word2):
                if dic[c1] < dic[c2]:
                    return LESS
                elif dic[c1] > dic[c2]:
                    return GREATER
            else:
                if len(word1) < len(word2):
                    return LESS
                elif len(word1) > len(word2):
                    return GREATER
            return EQUAL

        dic = {c: i for i, c in enumerate(order)}
        for i, word in enumerate(words):
            if i > 0:
                if compare(word, words[i - 1]) == -1:
                    return False
        return True