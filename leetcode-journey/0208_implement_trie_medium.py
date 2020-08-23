class TrieNode:
    def __init__(self):
        self.child_nodes = {}
        self.is_word_end = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr_node = self.root
        for ch in word:
            node = curr_node.child_nodes.get(ch, TrieNode())
            curr_node.child_nodes[ch] = node
            curr_node = node
        curr_node.is_word_end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr_node = self.root
        for ch in word:
            node = curr_node.child_nodes.get(ch)
            if not node:
                return False
            curr_node = node
        return curr_node.is_word_end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr_node = self.root
        for ch in prefix:
            node = curr_node.child_nodes.get(ch)
            if not node:
                return False
            curr_node = node
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)