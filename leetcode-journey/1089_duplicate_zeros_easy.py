class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        right = len(arr) - 1
        l, r = 0, len(arr) - 1
        while l < r:
            if arr[l] == 0:
                r -= 1
            l += 1
        left = r
        if l == r and arr[left] == 0:
            arr[right] = 0
            left -= 1
            right -= 1
        while right >= 0:
            if arr[left] == 0:
                arr[right] = 0
                right -= 1
            arr[right] = arr[left]
            left -= 1
            right -= 1