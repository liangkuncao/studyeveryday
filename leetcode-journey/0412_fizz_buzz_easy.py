class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = [str(i) for i in range(n + 1)]
        idx3, idx5 = 3, 5
        while idx3 <= n:
            res[idx3] = 'Fizz'
            idx3 += 3
        while idx5 <= n:
            res[idx5] = 'FizzBuzz' if res[idx5] == 'Fizz' else 'Buzz'
            idx5 += 5
        return res[1:]
