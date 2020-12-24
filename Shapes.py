class Point:

    def __init__(self, x, y, label):
        self.x = x
        self.y = y
        self.label = label

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getLabel(self):
        return self.label

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + "), Label:" + str(self.label)


class Line:

    def __init__(self, p1, p2, direction):
        m1 = (p1.getY() - p2.getY()) / (p1.getX() - p2.getX())
        n1 = p1.getY() - m1 * p1.getX()

        self.m = m1
        self.n = n1
        self.d = direction

    def at(self, x):
        return self.m * x + self.n

    def label(self, p):
        # Up is -1, down is 1
        if self.d == 0:
            if p.getY() > self.at(p.getX()):
                return -1
            else:
                return 1
        # Down is -1, up is 1
        else:
            if p.getY() < self.at(p.getX()):
                return -1
            else:
                return 1

    def __str__(self):
        if self.d == 0:
            direction = "Up, -1"
        else:
            direction = "Down, -1"
        return "y = " + str(self.m) + "x + " + str(self.n) + ", direction: " + direction


class VerticalLine:

    def __init__(self, x, direction):
        self.x = x
        self.d = direction

    def getX(self):
        return self.x

    def label(self, p):
        # the left side is -1, and the right is 1
        if self.d == 0:
            if p.getX() < self.x:
                return -1
            else:
                return 1
        # the right side is -1 and the left is 1
        else:
            if p.getX() > self.x:
                return -1
            else:
                return 1

    def __str__(self):
        return "x = " + str(self.x)
