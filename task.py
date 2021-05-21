from node import *

class task :
    def __init__(self, area = 0, number = 0, sequence_number = 0, time = 0, childs = []):
        self.dest = nodes[idx(area,number)]
        self.number = sequence_number
        self.time = time
        self.childs = childs
        self.parent = None

    def linkto(self, tail):
        self.childs.append(tail)
        tail.parent.append(self)
        
    def get_parent(self):
        return self.parent
    
    def able_to_reach(self,another):
        if self < another :
            delta_time  =  another.time - self.time
            return self.dest.dist(another) + unmount_delay * speed <= delta_time:
        else:
            return False

    def __lt__(self,another):
        return self.time < another.time
    
    def __gt__(self,another):
        return self.time > another.time
    
    def __eq__(self,another):
        return self.time == another.time

def create_graph(tasks):
    list.sort(tasks)
    for i in range(0,len(tasks)):
        for j in range (i+1,len(tasks)):
            if tasks[i].able_to_reach(tasks[j]):
                tasks[i].linkto(tasks[j])

