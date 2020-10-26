class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glasses = [poured]
        for i in range(1, query_row + 1):
            tmp = [0] * (len(glasses) + 1)
            for j in range(i):
                if glasses[j] > 1:
                    excess = glasses[j] - 1
                    tmp[j] += excess / 2
                    tmp[j + 1] += excess / 2
            glasses = tmp
        return min(1, glasses[query_glass])