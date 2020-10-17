class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        res = set()
        for i in range(len(s) - 9):
            tmp = s[i:i + 10]
            if tmp in seen:
                res.add(tmp)
            else:
                seen.add(tmp)
        return list(res)