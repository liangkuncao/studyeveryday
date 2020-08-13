class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        p1, p2 = len(num1) - 1, len(num2) - 1
        res, carry = list(), 0
        while p1 >= 0 or p2 >= 0:
            n1 = num1[p1] if p1 >= 0 else '0'
            n2 = num2[p2] if p2 >= 0 else '0'
            sum_ = ord(n1) - ord('0') + ord(n2) - ord('0') + carry
            res.append(sum_ % 10)
            carry = sum_ // 10
            p1 -= 1
            p2 -= 1
        if carry:
            res.append(carry)
        return ''.join(map(str, res[::-1]))