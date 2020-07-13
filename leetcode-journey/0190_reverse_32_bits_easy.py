class Solution(object):
    # Pythonic way, easy to understand.
    def reverseBits(self, n):
        output, power = 0, 31
        while n:
            output += (n & 1) << power
            n = n >> 1
            power -= 1
        return output



if __name__ == '__main__':
    input = '00000010100101000001111010011100'
    n = int(input, base=2)
    print(n)
    ret = Solution().reverseBits(n)
    print(f'{ret:032b}')