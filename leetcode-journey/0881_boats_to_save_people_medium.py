class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        weights = [0] * (limit + 1)
        for w in people:
            weights[w] += 1
        res = 0
        left, right = 1, limit
        while left <= right:
            if weights[left] == 0:
                left += 1
                continue
            if weights[right] == 0:
                right -= 1
                continue
            weights[right] -= 1
            complement = limit - right
            while complement >= left:
                if weights[complement]:
                    weights[complement] -= 1
                    break
                complement -= 1
            res += 1
        return res