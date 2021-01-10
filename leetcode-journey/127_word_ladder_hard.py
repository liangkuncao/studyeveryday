class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        def bfs(cur: Set[str], history: Set[str], word_set: Set[str], level: int) -> int:
            if not nxt or not word_set:
                return 0

            nxt = set()
            for word in cur:
                for w in word_set:
                    if w not in history and can_transform(word, w):
                        if w == endWord:
                            return level + 1
                        else:
                            nxt.add(w)
            history = history.union(nxt)
            word_set = word_set.difference(nxt)
            return bfs(nxt, history, word_set, level + 1)

        def can_transform(source: str, target: str) -> bool:
            count = 0
            for i, j in zip(source, target):
                if i != j:
                    count += 1
                if count > 1:
                    return False
            return True

        word_set.discard(beginWord)
        return bfs({beginWord}, {beginWord}, word_set, 1)