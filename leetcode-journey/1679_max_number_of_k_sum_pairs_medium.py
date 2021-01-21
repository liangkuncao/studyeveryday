class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums)
        res = 0
        for n, c in cnt.items():
            if k - n in cnt:
                if n == k / 2:
                    res += cnt[n]//2 * 2
                else:
                    res += min(cnt[n], cnt[k - n])
        return res // 2
