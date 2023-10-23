import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        sub_x = self.x - no.x
        sub_y = self.y - no.y
        sub_z = self.z - no.z
        return Points(sub_x, sub_y, sub_z)

    def dot(self, no):
        v_dot = 0
        x_list = [self.x, self.y, self.z]
        y_list = [no.x, no.y, no.z]
        for a, b in zip(x_list, y_list):
            v_dot += a * b
        return v_dot
    
    def cross(self, no):
        v_self = [self.x, self.y, self.z, self.x, self.y]
        v_no = [no.x, no.y, no.z, no.x, no.y]
        v_cross = []
        for i in range(3):
            v_cross.append(v_self[i+1]*v_no[i+2] - v_self[i+2]*v_no[i+1])
        return Points(v_cross[0], v_cross[1], v_cross[2])
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))