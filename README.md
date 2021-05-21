### 中青杯A题



##### pipenode

流水线上的节点

`pipenode.dist(dest)`: 计算一个节点到dest节点的最短路程

```python
nodeX = pipenode(area = 1, number = 1, x = 1.5, y = 61.5)
nodeY = pipenode(area = 2, number = 6, x = 113, y = 51.5)

distance = nodeX.dist(nodeY)
print(distance)
# dist between I<1> II<6> : 111.5
```



##### reponode

仓库节点

`reponode.dist(dest)`: 计算一个节点到dest节点的最短路程



#### testcase

```python
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
```

result

```shell
dist between I<1> I<4> : 60.0
dist between I<1> I<6> : 50.0  
dist between I<1> I<20> : 123.0
dist between I<1> II<1> : 81.5 
dist between I<1> II<6> : 111.5
```

