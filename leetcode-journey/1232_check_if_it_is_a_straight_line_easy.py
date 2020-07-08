class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        first_point, last_point = coordinates[0], coordinates[-1]
        if first_point[0] - last_point[0] == 0:
            coordinates = [[y, x] for x, y in coordinates]
            return self.checkStraightLine(coordinates)
        else:
            slope = (first_point[1] - last_point[1]) / (first_point[0] - last_point[0])
        intercept = first_point[1] - slope * first_point[0]
        for x, y in coordinates:
            if slope * x + intercept != y:
                return False
        return True