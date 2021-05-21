import math
from node import *

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

# test for node.dist() 
print("dist between I<1> I<4> : {}".format(nodes[0].dist(nodes[3])))
print("dist between I<1> I<6> : {}".format(nodes[0].dist(nodes[5])))
print("dist between I<1> I<20> : {}".format(nodes[0].dist(nodes[19])))
print("dist between I<1> II<1> : {}".format(nodes[0].dist(nodes[24])))
print("dist between I<1> II<6> : {}".format(nodes[0].dist(nodes[29])))