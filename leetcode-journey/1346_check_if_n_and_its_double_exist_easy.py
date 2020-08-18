class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if arr.count(0) >= 2:
            return True

        int_set = set(arr) - {0}
        for i in arr:
            if i * 2 in int_set:
                return True
        return False