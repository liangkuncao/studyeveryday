def is_flower_num(num: int) -> bool:
    n = num
    total = 0
    while n > 0:
        n, remainder = divmod(n, 10)
        total += remainder ** 3
        if total > num:
            return False
    return True if total == num else False


while True:
    m, n = map(int, input().split())
    res = []
    for i in range(m, n + 1):
        if is_flower_num(i):
            res.append(i)
    if not res:
        print('no')
    else:
        print(*res)

