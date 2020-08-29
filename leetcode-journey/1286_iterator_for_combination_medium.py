class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.chars = characters
        self.length = combinationLength
        self.curr = (1 << len(self.chars)) - 1

    def next(self) -> str:
        while self.curr and self.count1(self.curr) != self.length:
            self.curr -= 1
        res = []
        idx = 0
        for i in range(len(self.chars) - 1, -1, -1):
            if (self.curr & (1 << i)) >> i:
                res.append(self.chars[idx])
            idx += 1
        self.curr -= 1
        return ''.join(res)

    def hasNext(self) -> bool:
        while self.curr and self.count1(self.curr) != self.length:
            self.curr -= 1
        return self.curr > 0

    def count1(self, n):
        res = 0
        while n:
            res += 1
            n &= n - 1
        return res

# Your CombinationIterator object will be instantiated and called as such:
obj = CombinationIterator('abc', 2)
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())