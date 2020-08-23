class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        t = 0
        s = (1 + num_people) * num_people // 2
        curr = s
        while curr <= candies:
            t += 1
            curr += t * num_people**2 + s
        res = [0] * num_people
        for i in range(num_people):
            first_turn = i + 1
            last_second_turn = (t-1) * num_people + first_turn
            res[i] = (first_turn + last_second_turn) * t // 2
        candies -= sum(res)
        for i in range(num_people):
            tmp = min(candies, t * num_people + i + 1)
            res[i] += tmp
            candies -= tmp

        return res