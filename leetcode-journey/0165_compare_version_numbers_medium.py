class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = list(map(int, version1.split('.'))), list(map(int, version2.split('.')))
        while v1 or v2:
            digit1, digit2 = v1.pop(0) if v1 else 0, v2.pop(0) if v2 else 0
            if digit1 < digit2:
                return -1
            elif digit1 > digit2:
                return 1
        return 0