class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def edge_squared(p1: List[int], p2: List[int]) -> int:
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

        dis = []
        dis.append(edge_squared(p1, p2))
        dis.append(edge_squared(p1, p3))
        dis.append(edge_squared(p1, p4))
        dis.append(edge_squared(p2, p3))
        dis.append(edge_squared(p2, p4))
        dis.append(edge_squared(p3, p4))
        dis.sort()
        return dis[0] != 0 and dis[0] == dis[1] == dis[2] == dis[3] and dis[4] == dis[5]