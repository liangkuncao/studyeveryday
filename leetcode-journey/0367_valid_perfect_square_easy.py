class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low, high = 1, num
        while low <= high:
            mid = (low + high) // 2
            product = mid ** 2
            if product == num:
                return True
            elif product < num:
                low = mid + 1
            else:
                high = mid - 1
        return False