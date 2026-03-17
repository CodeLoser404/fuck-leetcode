# 基础搜索算法

## 焚诀

大部分图论题目，DFS和BFS都是可以互相转换的，但各自有使用场景

+ DFS（深度优先搜索）
  + **检测环或连通性**
  + **搜索路径或组合**
+ BFS（广度优先搜索）
  + **最短路径或最少操作步数**
  + **搜索整个图，但希望按“距离起点”的顺序**

一般来说，BFS 的优势在于其**按层扩展**的特点，而在不需要分层信息时，DFS 通常更简洁；相比之下，DFS 天生便适合处理**路径相关**的问题。



## 200.岛屿数量[中等]

### 链接

+ [200. 岛屿数量 - 力扣（LeetCode）](https://leetcode.cn/problems/number-of-islands)

### 题目

给你一个由 `'1'`（陆地）和 `'0'`（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

### 思路

这个题不需要分层信息，所以用DFS写起来更简洁一点，由于可以把已访问过的陆地标记为水，甚至不需要额外的`visited`数组。

### 解法：DFS

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        m = len(grid)
        n = len(grid[0])
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def dfs(x, y):
            grid[x][y] = '0'
            for dx, dy in dir:
                next_x, next_y = x + dx, y + dy
                if 0 <= next_x < m and 0 <= next_y < n and grid[next_x][next_y] == '1':
                    dfs(next_x, next_y)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    res += 1
        return res
```

+ 时间复杂度：$O(MN)$
+ 空间复杂度：$O(MN)$，最坏情况所有节点都是陆地，递归栈开销就是$O(MN)$

## 994.腐烂的橘子[中等]

### 链接

+ [994. 腐烂的橘子 - 力扣（LeetCode）](https://leetcode.cn/problems/rotting-oranges)

### 题目

在给定的 `m x n` 网格 `grid` 中，每个单元格可以有以下三个值之一：

- 值 `0` 代表空单元格；
- 值 `1` 代表新鲜橘子；
- 值 `2` 代表腐烂的橘子。

每分钟，腐烂的橘子 **周围 4 个方向上相邻** 的新鲜橘子都会腐烂。

返回 *直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 `-1`* 。

### 思路

由于腐烂是逐层扩展，所以用BFS。由于可能有多个起始源，所以是多源广度优先搜索，由于上一轮腐烂的橘子到下一轮它的邻居都腐烂了，那么这个橘子在下一轮是不需要再遍历了的，所以可以用BFS。

### 解法：BFS

```python
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        que = collections.deque()
        res = -1
        m = len(grid)
        n = len(grid[0])
        dir = [[0,1], [0,-1], [1,0], [-1,0]]
        
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 1:
                    fresh += 1
                elif val == 2:
                    que.append((i,j))
        
        while que:
            res += 1
            for _ in range(len(queue)):
                x, y = que.popleft()
                for dx, dy in dir:
                    next_x, next_y = x + dx, y + dy
                    if 0 <= next_x < m and 0 <= next_y < n and grid[next_x][next_y] == 1:
                        fresh -= 1
                        grid[next_x][next_y] = 2
                        que.append((next_x, next_y))

        if not fresh and res == -1:
            return 0
            
        return -1 if fresh else res
```

+ 时间复杂度：$O(MN)$
+ 空间复杂度：$O(MN)$



# 拓扑排序

## 焚诀

拓扑排序是对有向无环图（DAG）的节点进行线性排序，使得每条有向边 `u → v` 都满足 `u` 在 `v` 之前。

+ 验证是否有环：有向图含有一个环当且仅当深度优先搜索过程中探测到一条回边。
+ 以下三个在深度优先搜索中出现的看似不同的性质——**无环性**、**可线性化**以及**无回边性**——实际上是一回事。

什么时候我们要联想到使用拓扑排序呢？

+ **任务调度/依赖处理**（前后依赖，先做A再做B）

求拓扑排序一般有两种方法，分为**逆序输出零入度节点（DFS）**和**顺序输出零入度节点（BFS）**。

+ DFS类似于后序遍历，在子节点都处理完后把当前节点加入栈，最后逆序输出整个栈就是拓扑排序
+ BFS按入度为0的节点逐层输出，每处理完一个就把它从图中删掉（更新子节点的入度），直到所有节点都处理完

## 207.课程表[中等]

### 链接

+ [207. 课程表 - 力扣（LeetCode）](https://leetcode.cn/problems/course-schedule)

### 题目

你这个学期必须选修 `numCourses` 门课程，记为 `0` 到 `numCourses - 1` 。

在选修某些课程之前需要一些先修课程。 先修课程按数组 `prerequisites` 给出，其中 `prerequisites[i] = [ai, bi]` ，表示如果要学习课程 `ai` 则 **必须** 先学习课程 `bi` 。

- 例如，先修课程对 `[0, 1]` 表示：想要学习课程 `0` ，你需要先完成课程 `1` 。

请你判断是否可能完成所有课程的学习？如果可以，返回 `true` ；否则，返回 `false` 。

### 思路

**依赖处理**，非常经典的拓扑排序题目，不过由于只需要判断能否线性化，也就是判断是否无环，所以DFS时到没必要维护栈了，因为不需要拓扑排序，只要检测到回边就可以提前结束了。

### 解法1：DFS

DFS 中的节点通常分三种状态：

- `0`：未访问
- `1`：正在访问（在递归栈中）
- `2`：访问完成（已经出栈）

如果一条边

+ 指向 `1` → 回边 → 有环
+ 指向 `0` → 树边 → 继续 DFS
+ 指向 `2` → 前向边/横向边 → 不影响环检测（相当于有一个节点已经访问过了，现在有一条新边指向旧的这个节点，显然这不算环，因为当前节点的父结点不可能是这个节点）

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for to_, from_ in prerequisites:
            graph[from_].append(to_)

        visited = [0] * numCourses
        def dfs(i):
            visited[i] = 1
            for j in graph[i]:
                if visited[j] == 1:
                    return False # 有环
                elif visited[j] == 0:
                    if not dfs(j):
                        return False
            visited[i] = 2
            return True
        
        for i in range(numCourses):
            if not visited[i]:
                if not dfs(i): # dfs为False表示有环
                    return False
        return True
```

### 解法2：BFS

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for to_, from_ in prerequisites:
            graph[from_].append(to_)
            indegree[to_] += 1

        que = collections.deque([i for i in range(numCourses) if indegree[i] == 0])

        visited = 0
        while que:
            visited += 1
            i = que.popleft()
            for j in graph[i]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    que.append(i)

        return visited == numCourses
```















