from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3 or arr[0] >= arr[1] or arr[-2] <= arr[-1]:
            return False

        for i, v in enumerate(arr):
            if v > arr[i + 1]:
                summit = i
                break
            elif arr[i] == arr[i + 1]:
                return False
        for i, v in enumerate(arr[summit:]):
            if v <= arr[i + 1]:
                return False
        return True


print(Solution().validMountainArray([0,3,2,1]))