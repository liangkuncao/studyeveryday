class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        B = []
        while K > 0:
            K, remainder = divmod(K, 10)
            B.append(remainder)
        B = B[::-1]
        res = []
        carry = 0
        while A or B:
            a = A.pop() if A else 0
            b = B.pop() if B else 0
            total, carry = a + b + carry, 0
            res.append(total % 10)
            carry = total // 10
        if carry:
            res.append(carry)
        return res[::-1]
