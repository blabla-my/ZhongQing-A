from node import *
import itertools
import copy
class task :
    def __init__(self, area = 0, number = 0, sequence_number = 0, time = 0):
        self.dest = nodes[idx(area,number)]
        self.repo = nodes[idx(3,number)]
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
            return self.dest.dist(another.dest)/speed + unmount_delay <= delta_time
        else:
            return False

    def __lt__(self,another):
        return self.time < another.time
    
    def __gt__(self,another):
        return self.time > another.time
    
    def __eq__(self,another):
        return self.time == another.time

class task_graph :
    def __init__(self,tasks):
        self.tasks = copy.deepcopy(tasks)
        list.sort(self.tasks)
        self.entry = list()
        for i in range(0,len(self.tasks)):
            for j in range (i+1,len(self.tasks)):
                if self.tasks[i].able_to_reach(self.tasks[j]):
                    self.tasks[i].linkto(self.tasks[j])

            if len(self.tasks[i].parent) == 0:
                self.entry.append(self.tasks[i])
        list.sort(self.entry)
        edges = []
        for i in range(0,len(self.tasks)):
            for j in range(0,len(self.tasks)):
                if i != j :
                    for pj in self.tasks[j].parent:
                        if pj in self.tasks[i].childs :
                            edges.append((i,j))
                            break
        for pair in edges:
            i , j = pair
            self.tasks[i].childs.remove(self.tasks[j])
            self.tasks[j].parent.remove(self.tasks[i])

    def get_task(self,number):
        for t in self.tasks:
            if number == t.number :
                return t
        return None

    def empty(self):
        return len(self.tasks) == 0
    def show(self):
        for t in self.tasks:
            print('{} --> {}'.format(t.number,list(map(lambda x: x.number ,t.childs))))
        print("entry: {}".format(list(map(lambda x: x.number ,self.entry))))

    def remove(self,_task):
        if _task in self.tasks:
            self.tasks.remove(_task)
        else:
            print("not in graph")
            return
        for next in _task.childs :
            next.parent.remove(_task)
            if len(next.parent) == 0:
                self.entry.append(next)
        for pare in _task.parent :
            pare.childs.remove(_task)
        if _task in self.entry :
            self.entry.remove(_task)
    
    def gen_reply(self,carbase=0):
        Min = 99999999
        reply = None
        for e in self.entry:
            stack = []
            if len(e.childs) == 0:
                Min = min(Min, judge([e]))
                reply = [e]
            else:
                stack = list()
                stack.append([e,0])
                while len(stack) != 0:
                    if stack[-1][1] < len(stack[-1][0].childs):
                        cur = stack[-1][0].childs[stack[-1][1]]
                        if len(cur.childs) == 0:
                            road = list(map(lambda x:x[0],stack))[1:]
                            road.append(cur)
                            for combine_num in range(2,5):
                                feseqs = itertools.combinations(road,combine_num-1)
                                for feseq in feseqs:
                                    jud = judge([e] + list(feseq),carbase)
                                    if jud != None and jud < Min :
                                        Min = jud
                                        reply = copy.copy([e]+list(feseq))
                            stack.pop()
                            if len(stack) == 0:
                                break
                            stack[-1][1] += 1
                        else :
                            stack.append([cur,0])
                    else:
                        stack.pop()
                        if len(stack) == 0:
                            break
                        stack[-1][1] += 1
        return reply
    
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
    

def fetch_sequence_time(feseq):
    assert(len(feseq) <= 4)
    if len(feseq) == 0:
        return None
    res = feseq[0].repo.dist_to_B()/speed + mount_delay
    for i in range(0,len(feseq)-1):
        res += feseq[i].repo.dist(feseq[i+1].repo)/speed + mount_delay
    return res + feseq[-1].repo.dist_to_D()/speed

# cal fetch sequence time
def min_fetch_sequence_time(feseq):
    assert(len(feseq) <= 4)
    per = list(itertools.permutations(feseq,len(feseq)))
    Min = 999999999
    per_res = None
    for p in per:
        tmp = fetch_sequence_time(p)
        if Min > tmp:
            per_res = p
            Min = tmp
    return Min,per_res

def judge(feseq,base=0):
    assert(len(feseq) <= 4)
    mfst, per = min_fetch_sequence_time(feseq)
    TL = mfst + feseq[0].dest.dist_to_D() / speed + base
    
    if TL > feseq[0].time :
        return None
    else:
        return (feseq[0].time-TL)**2 + ( feseq[-1].dest.dist_to_D() / speed + unmount_delay )**2

        
tasks = []
with open('tasks1.txt','r') as f:
    Lines = f.readlines()
    for line in Lines:
        tasks.append(map_dataline_to_task(line))

m, per_res = min_fetch_sequence_time(tasks[:4])

g = task_graph(tasks)
g.show()

while g.empty() != True :
    rep = g.gen_reply()
    if rep != None :
        print("reply : {}".format(list(map(lambda x:x.number, rep))))
        for r in rep:
            g.remove(r)
        g.show()
    
