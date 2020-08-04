from collections import defaultdict


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        char_dict = defaultdict(int)
        for char in chars:
            char_dict[char] += 1
        for word in words:
            word_dict = defaultdict(int)
            flg = True
            for c in word:
                if c in char_dict:
                    word_dict[c] += 1
                    if word_dict[c] > char_dict[c]:
                        flg = False
                        break
                else:
                    flg = False
                    break
            if flg:
                res += len(word)
        return res
