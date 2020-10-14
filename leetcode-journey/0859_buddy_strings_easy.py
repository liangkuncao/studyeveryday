class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if A == B:
            if len(set(A)) == len(A):
                return False
            else:
                return True

        str_a, str_b = list(A), list(B)
        for i in range(len(str_a)):
            if str_a[i] != str_b[i]:
                if str_b[i] not in str_a[i + 1:]:
                    return False
                pos = str_a.index(str_b[i], i + 1)
                str_a[i], str_a[pos] = str_a[pos], str_a[i]
                return str_a[i:] == str_b[i:]
        return True

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if A == B:
            if len(set(A)) == len(A):
                return False
            else:
                return True
        diffs = []
        for c1, c2 in zip(A, B):
            if c1 != c2:
                diffs.append((c1, c2))
                if len(diffs) > 2:
                    return False
        if len(diffs) != 2:
            return False
        diffs[0] = (diffs[0][1], diffs[0][0])
        return diffs[0] == diffs[1]
