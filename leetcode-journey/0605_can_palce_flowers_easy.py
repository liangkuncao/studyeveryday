class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        N = len(flowerbed)
        i = 0
        while n > 0 and 0 <= i < N:
            prev = flowerbed[i - 1] if i - 1 >= 0 else 0
            post = flowerbed[i + 1] if i + 1 < N else 0
            if flowerbed[i] == 0 and prev == 0 and post == 0:
                flowerbed[i] = 1
                n -= 1
            i += 1
        return False if n else True