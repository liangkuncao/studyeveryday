import sys

n = sys.stdin.readline()
nums = list(map(int, sys.stdin.readline().split()))
avg = sum(nums) / len(nums)
count = 0
if avg.is_integer():
    low, high = 0, 0
    while low < len(nums) and high < len(nums):
        if nums[low] >= avg:
            low += 1
            continue
        if nums[high] <= avg:
            high += 1
            continue
        if (nums[low] - avg) % 2 != 0 or (nums[high] - avg) % 2 != 0:
            count = -1
            break
        nums[low] += 2
        nums[high] -= 2
        count += 1
    print(count)
else:
    print(-1)