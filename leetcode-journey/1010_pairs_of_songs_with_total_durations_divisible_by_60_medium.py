class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mod_time = [0] * 60
        for t in time:
            mod_time[t % 60] += 1
        res = 0
        res += mod_time[0] * (mod_time[0] - 1) // 2
        res += mod_time[30] * (mod_time[30] - 1) // 2
        res += sum([mod_time[i] * mod_time[60 - i] for i in range(1, 30)])
        return res

