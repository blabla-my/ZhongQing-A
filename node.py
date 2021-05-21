entry_cloumn_x = [1.5,83,164.5]
ceil = 61.5
floor = 1.5
speed = 5

unmount_delay = 3
mount_delay = 3

class reponode :
    def __init__(self,number,x,y):
        self.number = number 
        self.x = x
        self.y = y
    def dist(self,dest):
        mid = entry_cloumn_x[1]
        if self.y == dest.y:
            return abs(self.x - dest.x)
        else:
            res = abs(self.x - mid)
            res+= abs(dest.x - mid)
            res+= abs(self.y - dest.y)
            return res

class pipenode :
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
            return 1 if raw>0 else 2
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
            if self.number <= 4 :
                res = abs(self.x - entry_cloumn_x[dest.entry_column()])
                res+= abs(dest.x - entry_cloumn_x[dest.entry_column()])
                res+= abs(dest.y - self.y)
            elif dest.number <= 4:
                res = abs(dest.x - entry_cloumn_x[self.entry_column()])
                res+= abs(self.x - entry_cloumn_x[self.entry_column()])
                res+= abs(dest.y - self.y)
            else :
                res = abs( self.x - entry_cloumn_x[self.entry_column()] )
                res+= abs( entry_cloumn_x[self.entry_column()] - entry_cloumn_x[dest.entry_column()] )
                res+= abs( dest.x - entry_cloumn_x[dest.entry_column()] )
                Y1  = abs(self.y-ceil) + abs(dest.y-ceil)
                Y2  = self.y + dest.y
                res+= min(Y1,Y2)
        return res


# read data from data.txt
def map_dataline_to_pipenode(line):
    line = line.split('\t')
    Node = pipenode()
    if line[0] == 'I' : 
        Node.area = 1
    elif line[0] == 'II':
        Node.area = 2
    elif line[0] == 'III':
        Node.area = 3
    Node.number = int(line[1])
    Node.x = float(line[2])
    Node.y = float(line[3])
    return Node


# initialize the nodes of pipeline
nodes = []
with open('data.txt','r') as f :
    data_lines = f.readlines()
    for i in range(1,len(data_lines)):
        nodes.append(map_dataline_to_pipenode(data_lines[i]))


def idx(area,number):
    return (area-1)*24 + number-1