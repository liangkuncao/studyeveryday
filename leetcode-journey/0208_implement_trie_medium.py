class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.word_set = set()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.word_set.add(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return word in self.word_set

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return any(word.startswith(prefix) for word in self.word_set)


t = Trie()
print(t.insert('hello'))
print(t.search('hell'))
print(t.search('helloa'))
print(t.search('hello'))
print(t.startsWith('hell'))
print(t.startsWith('helloa'))
print(t.startsWith('hello'))
