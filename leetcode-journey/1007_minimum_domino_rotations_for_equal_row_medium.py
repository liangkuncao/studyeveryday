class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:

        def check(num: int) -> int:
            reta = retb = 0
            for a, b in zip(A, B):
                if a != num and b != num:
                    return -1
                elif a == num and b != num:
                    reta += 1
                elif a != num and b == num:
                    retb += 1
            return min(reta, retb)

        res = check(A[0])
        if res != -1 or A[0] == B[0]:
            return res
        return check(B[0])