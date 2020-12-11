class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        k = k % len(code) if k > 0 else -(abs(k) % len(code))
        res = []
        for i in range(len(code)):
            cur = 0
            if k < 0:
                for j in range(-1, k - 1, -1):
                    idx = i + j
                    cur += code[idx]
            elif k > 0:
                for j in range(1, k + 1):
                    idx = i + j if i + j < len(code) else i + j - len(code)
                    cur += code[idx]
            res.append(cur)
        return res
