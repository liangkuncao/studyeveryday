class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        idx = 0
        amount = 1
        while candies > 0:
            res[idx] += min(amount, candies)
            candies -= amount
            idx = 0 if idx >= num_people - 1 else idx + 1
            amount += 1
        return res