import math


entry_cloumn_x = [1.5,83,164.5]
ceil = 61.5
floor = 1.5
class node :
    def __init__(self,area=0,number = 0, x=0, y=0):
        self.area = area
        self.number = number
        self.x = x
        self.y = y
    
    def entry_column(self):
        raw = ((self.number - 1)>>2) % 2 
        if self.area == 1 :
            return 0 if raw>0 else 1
        elif self.area == 2:
            return 2 if raw>0 else 1
        else:
            return 1

    def dist(self,dest):
        if self.y == dest.y:
            return abs(self.x - dest.x)
        if self.entry_column() == dest.entry_column():
            res = abs( self.x - entry_cloumn_x[self.entry_column()] )
            res+= abs( dest.x - entry_cloumn_x[dest.entry_column()] )
            res+= abs( self.y - dest.y)
        else:
            res = abs( self.x - entry_cloumn_x[self.entry_column()] )
            res+= abs( entry_cloumn_x[self.entry_column()] - entry_cloumn_x[dest.entry_column()] )
            res+= abs( dest.x - entry_cloumn_x[dest.entry_column()] )
            Y1 = abs(self.y-ceil) + abs(dest.y-ceil)
            Y2 = self.y + dest.y
            if Y1 < Y2 :
                res += Y1
            else:
                res += Y2
        return res
