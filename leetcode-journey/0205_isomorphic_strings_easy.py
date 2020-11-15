class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t, t2s = {}, {}
        for i, j in zip(s, t):
            if i in s2t:
                if s2t[i] != j:
                    return False
            else:
                if j in t2s:
                    return False
                t2s[j] = i
                s2t[i] = j
        return True
