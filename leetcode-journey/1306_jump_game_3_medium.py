class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque()
        queue.append(start)
        seen = set()
        while queue:
            idx = queue.popleft()
            if idx not in seen:
                seen.add(idx)
                left, right = idx - arr[idx], idx + arr[idx]
                for i in (left, right):
                    if 0 <= i < len(arr):
                        queue.append(i)
                        if arr[left] == 0:
                            return True
        return False