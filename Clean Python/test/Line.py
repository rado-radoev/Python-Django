
import math

class Line:
    
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        #return math.sqrt(math.pow((self.coor2[0] - self.coor1[0]), 2) + math.pow((self.coor2[-1] -self.coor1[-1]), 2))


        x1, y1 = self.coor1
        x2, y2 = self.coor2

        return ( (x2 - x1)**2 + (y2 - y1)**2 ) ** 0.5
    
    def slope(self):
        return (self.coor2[-1] - self.coor1[-1]) / (self.coor2[0] - self.coor1[0])
    