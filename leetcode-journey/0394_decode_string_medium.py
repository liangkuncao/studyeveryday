class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_num, cur_str = '', ''
        for c in s:
            if c.isdigit():
                cur_num += c
            elif c == '[':
                stack.append(cur_str)
                stack.append(int(cur_num))
                cur_num = cur_str = ''
            elif c == ']':
                num = stack.pop()
                prev_str = stack.pop()
                cur_str = prev_str + cur_str*num
            else:
                cur_str += c
        return cur_str