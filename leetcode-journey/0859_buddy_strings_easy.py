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
