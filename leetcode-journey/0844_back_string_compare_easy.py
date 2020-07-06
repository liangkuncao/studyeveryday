import itertools


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:

        def F(string: str) -> str:
            skip = 0
            for c in reversed(string):
                if c == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield c

        return all(x == y for x, y in itertools.zip_longest(F(S), F(T)))