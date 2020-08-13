import sys
from typing import List
from typing import Set


def unique_combination(person_index: List[int], res: Set[int]):
    if len(res) == 5:
        idx.append(res)
        return
    elif not person_index:
        return

    unique_combination(person_index[1:], set(res))
    res.add(person_index[0])
    unique_combination(person_index[1:], set(res))


if __name__ == '__main__':
    nums = list(map(int, sys.stdin.readline().split()))
    idx = list()
    unique_combination(list(range(10)), set())
    diff = float('inf')
    for idx1 in idx:
        a, b = 0, 0
        for i in range(10):
            if i in idx1:
                a += nums[i]
            else:
                b += nums[i]
        diff = min(diff, abs(a - b))
    print(diff)









