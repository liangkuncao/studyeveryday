from typing import List

class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:

        def reverse(nums: List[int], count: int) -> List[int]:
            return nums[:count][::-1] + nums[count:]

        N = len(A)
        res = []
        flg = True
        while True:
            flg = False
            for i in range(N - 2, -1, -1):
                 if A[i] != A[i + 1] - 1:
                    flg = True
                    if i in (N - 2, 0):
                        A = reverse(A, N)
                        res.append(N)
                    else:
                        A = reverse(A, i + 1)
                        res.append(i + 1)
                    break
        return res


print(Solution().pancakeSort([3,2,4,1]))