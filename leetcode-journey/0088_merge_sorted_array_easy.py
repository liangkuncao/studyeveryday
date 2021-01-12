from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m + n - 1
        while n > 0:
            num1 = nums1[m - 1] if m > 0 else float('-inf')
            if num1 < nums2[n - 1]:
                nums1[i] = nums2[n - 1]
                n -= 1
            else:
                nums1[i] = num1
                m -= 1
            i -= 1


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    Solution().merge(nums1, 3, nums2, 3)
    print(nums1)
