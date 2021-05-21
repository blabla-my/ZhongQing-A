from node import *

class task :
    def __init__(self, area = 0, number = 0, sequence_number = 0, time = 0):
        self.dest = nodes[idx(area,number)]
        self.number = sequence_number
        self.time = time
        self.childs = list()
        self.parent = []

    def linkto(self, tail):
        self.childs.append(tail)
        tail.parent.append(self)
        
    def get_parent(self):
        return self.parent
    
    def able_to_reach(self,another):
        if self < another :
            delta_time  =  abs(another.time - self.time)
            return self.dest.dist(another.dest) + unmount_delay * speed <= delta_time * speed
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

def map_dataline_to_task(line):
    line = line.split('\t')
    seqnum = int(line[0])
    _area = 0
    if line[1][0] == 'I':
        _area = 1
    elif line[1][0] == 'II':
        _area = 2
    return task(area = _area, number = int((line[1].split('-'))[1]) ,sequence_number=seqnum, time = int(line[2]))

def show_graph(g):
    for t in g:
        print('{} --> {}'.format(t.number,list(map(lambda x: x.number ,t.childs))))

tasks = []
with open('tasks1.txt','r') as f:
    Lines = f.readlines()
    for line in Lines:
        tasks.append(map_dataline_to_task(line))

create_graph(tasks)
show_graph(tasks)