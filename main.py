from node import *


# test for node.dist() 
print("dist between I<1> I<4> : {}".format(nodes[0].dist(nodes[3])))
print("dist between I<1> I<6> : {}".format(nodes[0].dist(nodes[5])))
print("dist between I<1> I<20> : {}".format(nodes[0].dist(nodes[19])))
print("dist between I<1> II<1> : {}".format(nodes[0].dist(nodes[24])))
print("dist between I<1> II<6> : {}".format(nodes[0].dist(nodes[29])))