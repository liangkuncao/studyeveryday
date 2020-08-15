from collections import deque


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.chars = characters
        self.comb_len = combinationLength
        self.queue = deque()
        self.helper('', 0)

    def helper(self, s: str, idx: int):
        if len(s) == self.comb_len:
            self.queue.append(s)
            return
        for i in range(idx, len(self.chars)):
            self.helper(s + self.chars[i], i + 1)

    def next(self) -> str:
        return self.queue.popleft()

    def hasNext(self) -> bool:
        return len(self.queue)

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()