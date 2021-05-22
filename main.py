from node import *


# test for node.dist() 
print("dist between I<4> I<8> : {}, to D {} {}".format(nodes[3].dist(nodes[7]),nodes[idx(1,15)].dist_to_D(),nodes[3].dist_to_D()))
print("dist between I<1> I<6> : {}".format(nodes[0].dist(nodes[5])))
print("dist between I<1> I<20> : {}".format(nodes[0].dist(nodes[19])))
print("dist between I<1> II<1> : {}".format(nodes[0].dist(nodes[24])))
print("dist between I<1> II<6> : {}".format(nodes[0].dist(nodes[29])))