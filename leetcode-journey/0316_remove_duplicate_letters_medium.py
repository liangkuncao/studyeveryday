class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        def get_idx(c: str) -> int:
            return ord(c) - ord('a')

        count = [0] * 26
        used = [False] * 26
        for c in s:
            count[get_idx(c)] += 1
        res = []
        for c in s:
            count[get_idx(c)] -= 1
            if used[get_idx(c)]:
                continue
            while res and c < res[-1] and count[get_idx(res[-1])] > 0:
                used[get_idx(res[-1])] = False
                res.pop()
            res.append(c)
            used[get_idx(c)] = True
        return ''.join(res)

