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

