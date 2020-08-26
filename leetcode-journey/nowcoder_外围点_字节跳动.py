import sys


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


n = int(sys.stdin.readline())
points = list()
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    points.append(Point(x, y))
points.sort(key=lambda point: point.y, reverse=True)
last = points[0]
res = list()
res.append(last)
for point in points[1:]:
    if point.x >= last.x:
        last = point
        res.append(last)
for p in res:
    print(p.x, p.y)