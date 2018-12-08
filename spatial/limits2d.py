class Limits2D:

    def __init__(self, minPoint, maxPoint):
        self.minPoint = minPoint
        self.maxPoint = maxPoint

    def contains(self, point):
        return self.minPoint <= point and self.maxPoint > point
