class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.is_end = False


class Trie:

    def __init__(self):
        self.root = self.get_node()

    def get_node(self) -> TrieNode:
        return TrieNode()

    def _char_to_index(self, ch: str) -> int:
        return ord(ch) - ord('a')

    def insert(self, word: str):
        cur = self.root
        for i in range(len(word) - 1, -1, -1):
            index = self._char_to_index(word[i])
            if not cur.children[index]:
                cur.children[index] = self.get_node()
            cur = cur.children[index]
        cur.is_end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            index = self._char_to_index(ch)
            if not cur.children[index]:
                return False
            cur = cur.children[index]
        return cur and cur.is_end

    def is_empty(self, items: list) -> bool:
        for item in items:
            if item:
                return False
        return True

    def is_tail(self, word: str) -> bool:
        cur = self.root
        for i in range(len(word) - 1, -1, -1):
            index = self._char_to_index(word[i])
            if cur.children[index].is_end and self.is_empty(cur.children[index].children):
                return True
            cur = cur.children[index]
        return False


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = set(words)
        trie = Trie()
        res = 0
        for word in words:
            trie.insert(word)
        for word in words:
            if trie.is_tail(word):
                res += len(word) + 1
        return res