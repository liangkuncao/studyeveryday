"""
链接：https://www.nowcoder.com/questionTerminal/14c0359fb77a48319f0122ec175c9ada
来源：牛客网

有三种葡萄，每种分别有\mathit a,b,ca,b,c颗。有三个人，第一个人只吃第\text 1,21,2种葡萄，第二个人只吃第\text 2,32,3种葡萄，第三个人只吃第\text 1,31,3种葡萄。
适当安排三个人使得吃完所有的葡萄,并且且三个人中吃的最多的那个人吃得尽量少。
"""


import sys

T = int(sys.stdin.readline().strip())
data = []
for i in range(T):
    line = list(map(int, sys.stdin.readline().strip().split()))
    data.append(line)

res = []
for d in data:
    s = sum(d)
    m = max(d)
    a, b = divmod(s, 3)
    c, d = divmod(m, 2)
    a = a if b == 0 else a + 1
    c = c if d == 0 else c + 1
    res.append(max(a, c))

for i in res:
    print(i)
