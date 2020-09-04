class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_pos = {c: i for i, c in enumerate(S)}
        start = end = 0
        res = []
        for i, c in enumerate(S):
            end = max(end, last_pos[c])
            if i == end:
                res.append(end - start + 1)
                start = end + 1
        return res