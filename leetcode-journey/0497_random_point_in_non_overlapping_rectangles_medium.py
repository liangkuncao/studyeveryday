from typing import List
import random
import bisect


class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.areas = [(rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1) for rect in rects]

    def pick(self) -> List[int]:
        rect = random.choices(self.rects, weights=self.areas)[0]
        return [random.randint(rect[0], rect[2]), random.randint(rect[1], rect[3])]

# Your Solution object will be instantiated and called as such:
obj = Solution([[-2,-2,-1,-1],[1,0,3,0]])
print(obj.pick())