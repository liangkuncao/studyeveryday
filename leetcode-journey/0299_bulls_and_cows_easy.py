class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        N = 10
        A, B = 0, 0
        digits_a, digits_b = [0 for _ in range(N)], [0 for _ in range(N)]
        for i, j in zip(secret, guess):
            if i == j:
                A += 1
            else:
                digits_a[int(i)] += 1
                digits_b[int(j)] += 1
        for i in range(N):
            B += min(digits_a[i], digits_b[i])
        return f'{A}A{B}B'