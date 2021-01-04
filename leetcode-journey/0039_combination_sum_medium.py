from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def back_track(target, start, combination):
            if target < 0:
                return
            elif target == 0:
                res.append(combination)
            else:
                for i in range(start, len(candidates)):
                    back_track(target - candidates[i], i, combination + [candidates[i]])

        back_track(target, 0, [])
        return res

## 20201010
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(curr: int, path: List[int]) -> None:
            if curr == 0:
                res.append(path.copy())
            elif curr < 0:
                return
            for num in candidates:
                if path and num < path[-1]:
                    continue
                path.append(num)
                dfs(curr - num, path)
                path.pop()

        res = []
        candidates.sort()
        dfs(target, [])
        return res