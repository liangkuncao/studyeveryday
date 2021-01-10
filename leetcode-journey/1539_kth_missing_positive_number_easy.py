class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        length = len(arr)
        missing = arr[-1] - length
        if k > missing:
            return arr[-1] + k - missing
        else:
            cur = 0
            for i in range(1, arr[-1] + 1):
                if i == arr[cur]:
                    cur += 1
                else:
                    k -= 1
                    if k == 0:
                        return i