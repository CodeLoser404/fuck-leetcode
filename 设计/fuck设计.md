# 焚诀

设计类题目最常见的是有时间复杂度的限制，而使用单个的数据结构很有可能无法达到，所以通常采用**空间换时间**的思想，使用额外的数据结构辅助实现。下面列出常用数据结构的时间复杂度：

| 数据结构                                   | 查询                | 修改                           |
| ------------------------------------------ | :------------------ | ------------------------------ |
| 数组`vector`                               | $O(1)$              | $O(N)$，尾部插入摊销后为$O(1)$ |
| 链表`list`                                 | $O(N)$              | $O(1)$                         |
| 栈`stack`                                  | $O(1)$（栈顶）      | $O(1)$（栈顶）                 |
| 队列`queue`/`deque`                        | $O(1)$（队头/队尾） | $O(1)$（队头/队尾）            |
| 哈希表`unordered_set`、`unordered_map`     | $O(1)$              | $O(1)$                         |
| 红黑树`set`、`map`、`multiset`、`multimap` | $O(\log N)$         | $O(\log N)$                    |
| 堆`priority_queue`                         | $O(1)$（堆顶）      | $O(\log N)$                    |

# 栈

## 155.最小栈[中等]

### 链接

+ [155. 最小栈 - 力扣（LeetCode）](https://leetcode.cn/problems/min-stack)

### 题目

设计一个支持 `push` ，`pop` ，`top` 操作，并能在**常数时间**内检索到最小元素的栈。

实现 `MinStack` 类:

- `MinStack()` 初始化堆栈对象。
- `void push(int val)` 将元素val推入堆栈。
- `void pop()` 删除堆栈顶部的元素。
- `int top()` 获取堆栈顶部的元素。
- `int getMin()` 获取堆栈中的最小元素。

### 思路

这个题如果第一次做可能不是特别好想，看到最小值可能会想到用小顶堆这样可以$O(1)$查到最小值的数据结构，但是最小栈还需要pop修改元素，那么同时修改小顶堆的时间复杂度就变成$O(\log N)$了，所以这个方法行不通。注意到，这个题本质上是求**前缀最小值**，假设题目有一个数组，遍历这个数组只push然后getMin，那么我们用一个数组就可以维护前缀最小值了。为了支持栈的结构，我们用求前缀最小值的方法维护一个辅助栈。

### 解法

```c++
class MinStack {
    stack<int> x_stack;
    stack<int> min_stack;
public:
    MinStack() {
        min_stack.push(INT_MAX);
    }
    
    void push(int x) {
        x_stack.push(x);
        min_stack.push(min(min_stack.top(), x));
    }
    
    void pop() {
        x_stack.pop();
        min_stack.pop();
    }
    
    int top() {
        return x_stack.top();
    }
    
    int getMin() {
        return min_stack.top();
    }
};
```

### 变形

把栈改成队列（queue），`getMin`返回队列中的最小元素。

可以尝试同样的方法，除了正常的队列外，使用一个辅助队列。不过队列是FIFO的，不能像栈那样直接取min（因为先取min的元素后出栈，所以没问题），这里的方法是使用**单调递增队列（求下一个最小元素）**。其实最小栈这道题也可以把辅助栈改成**单调递减栈**。



# 哈希表

## 146.LRU缓存[中等]

### 链接

+ [146. LRU 缓存 - 力扣（LeetCode）](https://leetcode.cn/problems/lru-cache)

### 题目

请你设计并实现一个满足 [LRU (最近最少使用) 缓存](https://baike.baidu.com/item/LRU) 约束的数据结构。

实现 `LRUCache` 类：

- `LRUCache(int capacity)` 以 **正整数** 作为容量 `capacity` 初始化 LRU 缓存
- `int get(int key)` 如果关键字 `key` 存在于缓存中，则返回关键字的值，否则返回 `-1` 。
- `void put(int key, int value)` 如果关键字 `key` 已经存在，则变更其数据值 `value` ；如果不存在，则向缓存中插入该组 `key-value` 。如果插入操作导致关键字数量超过 `capacity` ，则应该 **逐出** 最久未使用的关键字。

函数 `get` 和 `put` 必须以 `O(1)` 的平均时间复杂度运行。

### 思路

使用**哈希表**可以保证`get`和`put`的时间是$O(1)$，而记录最近使用的key，可以用**链表**，每访问一个key就把它放到链表头来，逐出时就逐出链表尾即可。但从链表找key的时间是$O(N)$，所以我们要用哈希表记录key到链表中节点的映射，而移动这个节点到链表头，需要修改前后节点的指针，所以要用**双向链表**。

### 解法

```python
class DLinkNode:
        def __init__(self, key=0, value=0):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        # 两个虚拟节点
        self.head = DLinkNode()
        self.tail = DLinkNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = dict()
        self.capacity = capacity
        self.size = 0
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.moveToHead(node)
        return node.value       

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = DLinkNode(key, value)
            self.cache[key] = node
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                removed = self.removeTail()
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)

    def addToHead(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)
    
    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node
```





# 树

## 208.实现 Trie（前缀树）[中等]

### 链接

+ [208. 实现 Trie (前缀树) - 力扣（LeetCode）](https://leetcode.cn/problems/implement-trie-prefix-tree)

### 题目

**[Trie](https://baike.baidu.com/item/字典树/9825209?fr=aladdin)**（发音类似 "try"）或者说 **前缀树** 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补全和拼写检查。

请你实现 Trie 类：

- `Trie()` 初始化前缀树对象。
- `void insert(String word)` 向前缀树中插入字符串 `word` 。
- `boolean search(String word)` 如果字符串 `word` 在前缀树中，返回 `true`（即，在检索之前已经插入）；否则，返回 `false` 。
- `boolean startsWith(String prefix)` 如果之前已经插入的字符串 `word` 的前缀之一为 `prefix` ，返回 `true` ；否则，返回 `false` 。

### 思路

**前缀树/字典树**的每个节点包含两部分：

+ 指向子节点的指针数组。对于本题而言，只有26个字母。
+ `isEnd`标识是否是一个`word`的结尾。

`search`就是从根往下找，直到找到`word`的最后一个字符，如果所在节点`isEnd=True`，说明`word`在前缀树中；而`startsWith`不需要看`isEnd`。

### 解法

官解直接把`Trie`当做节点类，也不是不行，但感觉不符合一般树数据结构的写法，所以我还是特意定义了一个节点类。另外`searchPrefix`也可以写成递归形式，但是用`for`直接遍历`prefix`会更简单。

```python
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def searchPrefix(self, prefix: str) -> TrieNode:
        node = self.root
        for c in prefix:
            ch = ord(c) - ord('a')
            if not node.children[ch]:
                return None
            node = node.children[ch]
        return node

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            ch = ord(c) - ord('a')
            if not node.children[ch]:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEnd = True


    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.searchPrefix(prefix)
        return True if node else False	
```













