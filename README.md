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



##### task

存放一个请求的area 、 number 、 需求时间

`task.linkto(dest)`: 建立一条到dest的有向边

`task.get_parent()`: 返回task在图上的前继元

`task.able_to_reach(dest)`: 是否能够在规定时间内到达dest节点



##### create_graph

建立tasks对应的有向图

```python
def create_graph(tasks):
    list.sort(tasks)
    for i in range(0,len(tasks)):
        for j in range (i+1,len(tasks)):
            if tasks[i].able_to_reach(tasks[j]):
                tasks[i].linkto(tasks[j])
```



##### show_graph

打印图中的边(邻接表形式)

对tasks1.txt的结果

```sh
1 --> [2, 6, 3, 7, 4, 8]
5 --> [6, 4]
2 --> [6, 4, 8]
6 --> []
3 --> [4]
7 --> [8]
4 --> []
8 --> []
```



##### fetch_sequence_time

给定一个任务序列，计算按顺序取零件要的时间

从B点出发，终点为D



##### min_fetch_sequence_time

计算一个任务序列取零件的最短时间

```python
''' tasks2.txt
1	I-3	112
2	I-4	130
3	I-20	150
4	I-13	167
'''

tasks = []
with open('tasks2.txt','r') as f:
    Lines = f.readlines()
    for line in Lines:
        tasks.append(map_dataline_to_task(line))

m, per_res = min_fetch_sequence_time(tasks[:4])

# fetch sequence is 3 4 13 20, right
```



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

