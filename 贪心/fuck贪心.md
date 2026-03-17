## 焚诀

贪心算法使用条件就是**局部最优可以推导出全局最优**

感觉还没有什么明显的特征，多做点题再说吧





## 55.跳跃游戏[中等]

### 链接

+ [55. 跳跃游戏 - 力扣（LeetCode）](https://leetcode.cn/problems/jump-game)

### 题目

给你一个非负整数数组 `nums` ，你最初位于数组的 **第一个下标** 。数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标，如果可以，返回 `true` ；否则，返回 `false` 。

### 解法1：动态规划

如果看过 [fuck动态规划.md](..\动态规划\fuck动态规划.md) ，那么这道题可以很容易想出动态规划的解法，就是线性dp，`dp[i]`就表示是否可以到达`nums[i]`。但是如果内层循环写`for j in range(i)`的话会超时。

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[0] = True
        for i in range(n):
            if dp[i]:
                for j in range(i + 1, min(i + nums[i] + 1, n)):
                    dp[j] = True
        return dp[-1]
```

+ 时间复杂度：$O(N^2)$

+ 空间复杂度：$O(N)$

### 解法2：贪心

我觉得贪心暂时没有什么明显的表面特征可以总结，对于这道题，其实可以注意到，在更新dp数组时对于某些可以到达的位置，我们会重复地设置它为True。一个还算自然的想法就是，我们只关心最远可到达的位置就行了，也就是遍历`i`时，如果`i`在之前可达的范围内，并且`i+nums[i]`超过数组范围了，那么显然所有位置都可达；如果`i`是之前可达的最远的位置了，并且`i+nums[i]`无法更新这个最远的位置了，而`i`又不是数组末尾，那么自然无法到达数组末尾了。

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        farthest = 0
        for i in range(n):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
            if farthest >= n - 1:
                return True
        return False
```

+ 时间复杂度：$O(N)$
+ 空间负责度：$O(1)$

## 45.跳跃游戏 II[中等]

### 链接

+ [45. 跳跃游戏 II - 力扣（LeetCode）](https://leetcode.cn/problems/jump-game-ii)

### 题目

给定一个长度为 `n` 的 **0 索引**整数数组 `nums`。初始位置在下标 0。

每个元素 `nums[i]` 表示从索引 `i` 向后跳转的最大长度。换句话说，如果你在索引 `i` 处，你可以跳转到任意 `(i + j)` 处：

- `0 <= j <= nums[i]` 且
- `i + j < n`

返回到达 `n - 1` 的最小跳跃次数。测试用例保证可以到达 `n - 1`。

### 解法1：动态规划

和 [55.跳跃游戏](#55.跳跃游戏[中等]) 题的动规思路如出一辙，而且题目保证一定可达，甚至不用判断可达性了，定义`dp[i]`表示到达`nums[i]`的最小跳跃次数。

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [inf] * n
        dp[0] = 0
        for i in range(n):
            for j in range(i + 1, min(i + nums[i] + 1, n)):
                dp[j] = min(dp[j], dp[i] + 1)
        return dp[-1]
```

+ 时间复杂度：$O(N^2)$

+ 空间复杂度：$O(N)$

### 解法2：贪心

贪心思路和前一题也是一样的，每一跳都要跳得尽可能远。但是假设从位置1出发，更新了最远距离可以到达2,3两个位置，而从2最远可以跳到4，从3最远可以跳到5，如果是在每次更新最远距离时增加步数这就会出问题，虽然2跳得没3远，但是2先跳，就会先累积一次步数。所以有点类似于BFS，对于每一跳可到达的所有候选位置，我们只从这些位置中找出下一跳可以跳的最远的那个去跳。具体代码实现是用`end`去维护上一跳可到达的最远位置。

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        farthest, step, end = 0, 0, 0
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == end:
                step += 1
                end = farthest
        return step
```

+ 时间复杂度：$O(N)$
+ 空间负责度：$O(1)$

## 763.划分字母区间[中等]

### 链接

+ [763. 划分字母区间 - 力扣（LeetCode）](https://leetcode.cn/problems/partition-labels)

### 题目

给你一个字符串 `s` 。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。例如，字符串 `"ababcc"` 能够被分为 `["abab", "cc"]`，但类似 `["aba", "bcc"]` 或 `["ab", "ab", "cc"]` 的划分是非法的。

注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是 `s` 。

返回一个表示每个字符串片段的长度的列表。

### 思路

贪心的思路还是很明显的，由于同一个字母最多出现在一个片段中，那么对于一个字母，第一次出现的位置和最后一次出现的位置肯定在一个片段内。因此要先遍历整个字符串，用哈希表记录每个字母最后一次出现的位置。接下来用贪心的方法划分为尽可能多的片段：

+ 从左往右遍历，维护当前片段的开始下标`start`和结束下标`end`
+ 每遍历一个字母，`end=max(end, last[c])`
+ 如果遍历到`end`的位置，那么当前片段的范围就是`[start, end]`，更新`start=end+1`
+ 重复上述步骤，直到遍历完字符串

### 解法

```python
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = [0] * 26
        for i, c in enumerate(s):
            last[ord(c) - ord('a')] = i
        res = []
        start = end = 0
        for i, c in enumerate(s):
            end = max(end, last[ord(c) - ord('a')])
            if i == end:
                res.append(end - start + 1)
                start = i + 1
        return res
```





