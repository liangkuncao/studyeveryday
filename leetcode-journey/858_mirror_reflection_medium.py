class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        from fractions import gcd
        g = gcd(p, q)
        if (p // g) % 2 == 0:
            return 2
        return (q // g) % 2