from task import *
from car import *

def fitCar(cars):
    #print_cars(cars)
    Min = 999999
    Mc = None
    for c in cars :
        if c.base < Min :
            Min = c.base
            Mc = c
    return Mc

def down_cars_base(cars,d):
    for c in cars:
        c.base -= d

def print_cars(cars):
    print("cars ",end='')
    for c in cars:
        print(c.base,' ')

def show(reply,per_res,car):
    str_reply = ''
    for r in reply:
        str_reply += str(r.number) + '-'
    str_reply = str_reply.strip('-')
    str_per_res = ''
    for r in per_res:
        str_per_res += str(r.number) + '-'
    str_per_res = str_per_res.strip('-')
    print("{}\t\t{}\t\t{}".format(car.number,str_per_res,str_reply))

class instance :
    def __init__(self,tasks,cars,):
        self.graph = task_graph(tasks)
        self.cars = cars
    
    def run(self):
        down = 0
        total = 0
        print("拖车编号\t取件顺序\t配送顺序")
        while self.graph.empty() != True:
            fit_car = fitCar(self.cars)
            if fit_car != None:
                rep,per_res = self.graph.gen_reply(fit_car.base)
                if rep != None and per_res != None:
                    if down != 0:
                        print("------------stall {} seconds.--------------".format(down))
                        total += down
                        down = 0
                    show(rep,per_res,fit_car)
                    fit_car.base += rep[0].dest.dist_to_D() / speed
                    for r in rep:
                        #print(type(self.graph.get_task(r.number)))
                        self.graph.remove(self.graph.get_task(r.number))
                    #self.graph.show()
                else:
                    down_cars_base(cars,1)
                    down += 1
                    #print("down {}".format(down))
                    continue
            else:
                return
        print("totally stall : {} seconds".format(total))

tasks = []
with open('tasks1.txt','r') as f:
    Lines = f.readlines()
    for line in Lines:
        tasks.append(map_dataline_to_task(line))     
cars = [car(1),car(2)]
inst = instance(tasks=tasks,cars = cars)
#inst.graph.show()
inst.run()
                
        