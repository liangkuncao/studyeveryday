class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split()
        if len(pattern) != len(words):
            return False
        char_to_word, word_set = {}, set()
        for i, ch in enumerate(pattern):
            if ch in char_to_word:
                if char_to_word[ch] != words[i]:
                    return False
            else:
                if words[i] in word_set:
                    return False
                else:
                    char_to_word[ch] = words[i]
                    word_set.add(words[i])
        return True