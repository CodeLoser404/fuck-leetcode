# DFS

## 焚诀

+ 二叉树题目在写递归版本代码时，关键在于确定

  + 递归终止条件

  + 单层递归的处理逻辑，是前序遍历、中序遍历还是后序遍历

+ 在二叉树中，如果需要同时检查多个节点的值，要想到使用**双/多指针**。

+ **有些题目在直接使用三种递归方式实现单层递归的处理逻辑比较困难时，要想到在递归时传递更多的信息**（例如引入额外的参数，或者用全局变量）。

## 104.二叉树的最大深度[简单]*

### 链接

+ [104. 二叉树的最大深度 - 力扣（LeetCode）](https://leetcode.cn/problems/maximum-depth-of-binary-tree/description/)
+ [看到递归就晕？带你理解递归的本质！【基础算法精讲 09】](https://www.bilibili.com/video/BV1UD4y1Y769)

### 题目

给定一个二叉树 `root` ，返回其最大深度。

二叉树的 **最大深度** 是指从根节点到最远叶子节点的最长路径上的节点数。

### 思路

我们肯定要先知道左右子树的深度之后，才能知道当前节点的深度，因此使用后序遍历。

### 解法

```c++
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if(root == NULL){
            return 0;
        }
        int left_depth = maxDepth(root->left);
        int right_depth = maxDepth(root->right);
        return max(left_depth, right_depth) + 1;
    }
};
```

## 100.相同的树[简单]*

### 链接

+ [100. 相同的树 - 力扣（LeetCode）](https://leetcode.cn/problems/same-tree/description/)
+ [如何灵活运用递归？【基础算法精讲 10】](https://www.bilibili.com/video/BV18M411z7bb)

### 题目

给你两棵二叉树的根节点 `p` 和 `q` ，编写一个函数来检验这两棵树是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

### 思路

这道题肯定要先比较当前节点的值是否相同，如果相同再检查子树，否则直接返回，因此使用前序遍历。

### 解法

```c++
 */
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if(p == nullptr || q == nullptr){
            return p == q;
        }
        return p->val == q->val && isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};
```

## 101.对称二叉树[简单]*

### 链接

+ [101. 对称二叉树 - 力扣（LeetCode）](https://leetcode.cn/problems/symmetric-tree/description/)
+ [如何灵活运用递归？【基础算法精讲 10】](https://www.bilibili.com/video/BV18M411z7bb)

### 题目

给你一个二叉树的根节点 `root` ， 检查它是否轴对称。

### 思路

与[100题](#100.相同的树[简单])递归思路相同，采用前序遍历。而我们需要同时检查两个节点，即使没做过100题，也要想到使用双指针。轴对称的关键在于，左根节点的左子节点要和右根节点的右子节点相等，左根节点的右子节点要和右根节点的左子节点相等。

### 解法

```c++
class Solution {
public:
   bool isSameTree(TreeNode* p, TreeNode* q) {
        if(p == nullptr || q == nullptr){
            return p == q;
        }
        return p->val == q->val && isSameTree(p->left, q->right) && isSameTree(p->right, q->left);
    }
    
    bool isSymmetric(TreeNode* root) {
        return isSameTree(root->left, root->right);
    }
};
```

## 110.平衡二叉树[简单]*

### 链接

+ [110. 平衡二叉树 - 力扣（LeetCode）](https://leetcode.cn/problems/balanced-binary-tree/)
+ [如何灵活运用递归？【基础算法精讲 10】](https://www.bilibili.com/video/BV18M411z7bb)

### 题目

给定一个二叉树，判断它是否是 平衡二叉树 

> **平衡二叉树** 是指该树所有节点的左右子树的高度相差不超过 1。

### 思路

要求左右子树高度，自然使用后序遍历。这题比较tricky的点在于在正常的求高度的递归逻辑之上，我们返回-1代表不平衡。

### 解法

```c++
class Solution {
public:
    int getHeight(TreeNode* root){
        if(root == nullptr){
            return 0;
        }
        int left_height = getHeight(root->left);
        if(left_height == -1){
            return -1;
        }
        int right_height = getHeight(root->right);
        if(right_height == -1 || abs(left_height - right_height) > 1){
            return -1;
        }
        return max(left_height, right_height) + 1;
    }

    bool isBalanced(TreeNode* root) {
        return getHeight(root) != -1;
    }
};
```

## 199.二叉树的右视图[中等]*

### 链接

+ [199. 二叉树的右视图 - 力扣（LeetCode）](https://leetcode.cn/problems/binary-tree-right-side-view/description/)
+ [如何灵活运用递归？【基础算法精讲 10】](https://www.bilibili.com/video/BV18M411z7bb)

### 题目

给定一个二叉树的 **根节点** `root`，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

### 思路

这题用层序遍历写会很直观。现在考虑如何使用递归来解决，既然想要右视图，不难想到可以先遍历右子树，再遍历左子树，然后期望右边的结果可以遮住左边那些节点。该怎么做呢？**可以记录节点的深度，如果`res`的长度和当前深度相同(这里深度从0开始)，说明当前节点是当前深度所有节点中最右边的节点，直接加入`res`中**，对于左边那些节点，因为最右边的节点已经处理过了，就会被跳过。

### 解法

```c++
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> res;
        std::function<void(TreeNode*, int)> dfs = [&](TreeNode* node, int depth){
            if(node == NULL)
                return;
            if(depth == res.size())
                res.push_back(node->val);
            dfs(node->right, depth + 1);
            dfs(node->left, depth + 1);
        };
        dfs(root, 0);
        return ans;
    }
};
```

## 236.二叉树的最近公共祖先[中等]*

### 链接

+ [236. 二叉树的最近公共祖先 - 力扣（LeetCode）](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/)
+ [二叉树的最近公共祖先【基础算法精讲 12】](https://www.bilibili.com/video/BV1W44y1Z7AR)

### 题目

给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

[百度百科](https://baike.baidu.com/item/最近公共祖先/8918834?fr=aladdin)中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（**一个节点也可以是它自己的祖先**）。”

### 思路

这题的关键就是：如果找到了目标节点就把该节点往上返回，否则把空节点往上返回。如果采用后序遍历，如果看到左右子树均返回了非空节点，那么说明当前节点就是最近公共祖先了。

分类讨论：

+ 若当前节点是空节点，返回空节点
+ 若当前节点是p，返回p
+ 若当前节点是q，返回q
+ 其他：
  + 左右子树都找到：返回当前节点（最终答案）
  + 只有左子树找到：返回递归左子树的结果
  + 只有右子树找到：返回递归右子树的结果
  + 左右子树都没找到：返回空节点

### 解法

```c++
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(root == nullptr || root == p || root == q){
            return root;
        }
        TreeNode* left = lowestCommonAncestor(root->left, p, q);
        TreeNode* right = lowestCommonAncestor(root->right, p, q);
        if(left && right){
            return root;
        }
        if(left){
            return left;
        }
        return right;
    }
};
```

## 114.二叉树展开为链表[中等]

### 链接

+ [114. 二叉树展开为链表 - 力扣（LeetCode）](https://leetcode.cn/problems/flatten-binary-tree-to-linked-list)

### 题目

给你二叉树的根结点 `root` ，请你将它展开为一个单链表：

- 展开后的单链表应该同样使用 `TreeNode` ，其中 `right` 子指针指向链表中下一个结点，而左子指针始终为 `null` 。
- 展开后的单链表应该与二叉树 [**先序遍历**](https://baike.baidu.com/item/先序遍历/6442839?fr=aladdin) 顺序相同。

### 思路

我们相信`flatten(root)`达到的效果就是题目所描述的单链表，那么先调用一下`flatten(root.left)`得到以`root.left`为根向右下角延伸的一条链，接下来我们要用它作为`root.right`（原本的`root.right`保存到`tmp`中），再把这条链最右下角的节点作为`flatten(tmp)`的根。

### 解法

```python
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return
        tmp = root.right
        self.flatten(root.left)
        if root.left is not None:
            root.right = root.left
            root.left = None
            node = root.right
            while node.right: # 找到右边这条链的最右下角的节点
                node = node.right
            node.right = tmp
        self.flatten(tmp)
```

## 437.路径总和 III[中等]

### 链接

+ [437. 路径总和 III - 力扣（LeetCode）](https://leetcode.cn/problems/path-sum-iii)

### 题目

给定一个二叉树的根节点 `root` ，和一个整数 `targetSum` ，求该二叉树里节点值之和等于 `targetSum` 的 **路径** 的数目。

**路径** 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

### 思路

首先对于一个节点，我们想要知道从这个节点出发，有多少条路径和等于`targetSum`，所以据此可以写一个dfs出来。但是二叉树中任何一个节点，都可以作为这个起点，所以我们在外层还要以dfs的形式遍历整棵树。另外注意判断条件一定是`node.val == tsum`而

### 解法1：DFS

```python
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        
        # 以当前节点为起点的路径数量
        def dfs(node, tsum):
            if not node:
                return 0
            count = 1 if node.val == tsum else 0
            count += dfs(node.left, tsum - node.val)
            count += dfs(node.right, tsum - node.val)
            return count
        
        # 当前节点为起点 + 左子树起点 + 右子树起点
        return dfs(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
```

+ 时间复杂度：$O(N^2)$，每个节点都要做一次DFS，每次DFS都是$O(N)$
+ 空间复杂度：$O(N)$，栈开销

### 解法2：前缀和

因为路径方向必须是向下的，我们其实可以把树的分叉看成多条不同的链，那么这个问题就简化为在这些链上去找一个区间和为`targetSum`的数目。看到求区间和，要想到前缀和数组。下面的代码相当于 [560.和为 K 的子数组[中等]](..\数组\fuck数组.md#560.和为 K 的子数组[中等]) 的一次遍历写法的二叉树版本。使用哈希表缓存前缀和，可以避免遍历前缀和数组来两两匹配找区间和。

```python
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        prefix = collections.defaultdict(int)
        prefix[0] = 1

        def dfs(root, curr):
            if not root:
                return 0
            
            ret = 0
            curr += root.val
            ret += prefix[curr - targetSum] # 后 - 前 = targetSum
            prefix[curr] += 1
            ret += dfs(root.left, curr)
            ret += dfs(root.right, curr)
            prefix[curr] -= 1 # 回溯

            return ret

        return dfs(root, 0)
```

+ 时间复杂度：$O(N)$
+ 空间复杂度：$O(N)$







# 二叉搜索树

## 焚诀

二叉搜索树的性质：

+ **中序遍历下，输出的二叉搜索树节点的数值是有序序列。**

## 98.验证二叉搜索树[中等]*

### 链接

+ [98. 验证二叉搜索树 - 力扣（LeetCode）](https://leetcode.cn/problems/validate-binary-search-tree/description/)
+ [验证二叉搜索树【基础算法精讲 11】](https://www.bilibili.com/video/BV14G411P7C1)

### 题目

给你一个二叉树的根节点 `root` ，判断其是否是一个有效的二叉搜索树。

**有效** 二叉搜索树定义如下：

- 节点的左子树只包含 **严格小于** 当前节点的数。
- 节点的右子树只包含 **严格大于** 当前节点的数。
- 所有左子树和右子树自身必须也是二叉搜索树。

> `treeName` 树中的一个节点及其所有子孙节点所构成的树称为 `treeName` 的 **子树**。

### 思路

这道题一个常见的误区就是，仅仅比较`root->left->val < root->val < root->right->val`，这是不够的，因为根据定义，左子树中所有节点的值都要小于当前节点的值，仅判断左儿子是不够的，左孙子就有可能违背定义。

那么怎么保证这一点呢？在直接使用三种递归方式完成单层递归的处理逻辑比较困难时，要想到在递归时传入更多信息。

### 解法1：前序遍历

如果使用前序遍历，在处理当前节点时根节点已经处理过了，那么我们可以传递一个区间`[left, right]`下来，表示当前节点的父结点的取值范围，当前节点自然要满足`left < root->val < right`的约束，然后对于左子树区间就变成了`[left, root->val]`，对于右子树区间就变成了`[root->val, right]`。

```c++
class Solution {
public:
    // 因为题目的值有可能为int的最小值和最大值,所以使用long的最小值和最大值来保证初始区间的正确性
    bool isValidBST(TreeNode* root, long long left = LLONG_MIN, long long right = LLONG_MAX) {
        if (root == nullptr) {
            return true;
        }
        long long x = root->val;
        return left < x && x < right &&
               isValidBST(root->left, left, x) &&
               isValidBST(root->right, x, right);
    }
};
```

### 解法2：中序遍历

如果使用中序遍历，一个naive的思路就是根据BST的性质，在中序遍历时把所有节点的值记录到一个数组中，然后判断这个数组是否是升序的，缺点是空间复杂度为$O(N)$，且需要遍历两次。想要改进的话，不难想到，我们可不可以在遍历的同时就判断是否升序呢？进一步就是比较当前节点是否大于上一个节点。

```c++
class Solution {
public:
    TreeNode* pre = NULL;
    bool isValidBST(TreeNode* root) {
        if(root == nullptr) return true;
        bool left = isValidBST(root->left);
        if(!left){
            return false;
        }
        if(pre && pre->val >= root->val){
            return false;
        }
        pre = root;
        return isValidBST(root->right);
    }
};
```

### 解法3：后序遍历

如果后序遍历，类似于前序遍历，我们需要知道左子树的最大值，和右子树的最小值，保证我们当前节点的值位于二者之间

```c++
class Solution {
    pair<long long, long long> dfs(TreeNode* node) {
        if (node == nullptr) {
            return {LLONG_MAX, LLONG_MIN};
        }
        auto[l_min, l_max] = dfs(node->left);
        auto[r_min, r_max] = dfs(node->right);
        long long x = node->val;
        // 也可以在递归完左子树之后立刻判断，如果发现不是二叉搜索树，就不用递归右子树了
        if (x <= l_max || x >= r_min) {
            return {LLONG_MIN, LLONG_MAX};
        }
        return {min(l_min, x), max(r_max, x)};
    }

public:
    bool isValidBST(TreeNode* root) {
        return dfs(root).second != LLONG_MAX;
    }
};
```

## 235.二叉搜索树的最近公共祖先[中等]*

### 链接

+ [235. 二叉搜索树的最近公共祖先 - 力扣（LeetCode）](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/)
+ [二叉树的最近公共祖先【基础算法精讲 12】](https://www.bilibili.com/video/BV1W44y1Z7AR)

### 题目

给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

[百度百科](https://baike.baidu.com/item/最近公共祖先/8918834?fr=aladdin)中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（**一个节点也可以是它自己的祖先**）。”

### 思路

二叉搜索树也是二叉树，完全可以用[236题](#236.二叉树的最近公共祖先[中等])的代码。但这么做，BST的性质不就白白浪费了嘛！例如我们发现当前节点的值比p和q都大，那么根据BST的性质，p和q必然在左子树中，从而达到了剪枝效果。

分类讨论：

+ 若当前节点是空节点（题目保证一定存在p和q，那么当前节点不可能为空）
+ 若当前节点是p，返回p
+ 若当前节点是q，返回q
+ 若p和q分别在左右子树中，返回当前节点（最终答案）
+ 其他：
  + p和q都在左子树：返回递归左子树的结果
  + p和q都在右子树：返回递归右子树的结果

### 解法

```c++
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        int x = root->val;
        if(p->val < x && q->val < x){
            return lowestCommonAncestor(root->left, p, q);
        }
        if(p->val > x && q->val > x){
            return lowestCommonAncestor(root->right, p, q);
        }
        return root;
    }
};
```









# BFS

面试手搓时可能会考察自己构造二叉树，我第一次面字节时卡这上面卡了半天，我是大蠢猪，贴此代码，以示警戒！

```c++
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

// 二叉树节点定义
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

// 构造二叉树的函数
TreeNode* buildTree(const vector<int*>& arr) {
    if (arr.empty() || arr[0] == nullptr) return nullptr;

    TreeNode* root = new TreeNode(*arr[0]);
    queue<TreeNode*> q;
    q.push(root);

    int i = 1;
    while (!q.empty() && i < arr.size()) {
        TreeNode* node = q.front();
        q.pop();

        // 左孩子
        if (arr[i] != nullptr) {
            node->left = new TreeNode(*arr[i]); // 一定是先在父节点构造子节点
            q.push(node->left);
        }
        i++;

        // 右孩子
        if (i < arr.size() && arr[i] != nullptr) {
            node->right = new TreeNode(*arr[i]);
            q.push(node->right);
        }
        i++;
    }
    return root;
}

// 打印二叉树（层序遍历）
void printTree(TreeNode* root) {
    if (!root) return;
    queue<TreeNode*> q;
    q.push(root);
    while (!q.empty()) {
        int size = q.size();
        for (int i = 0; i < size; i++) {
            TreeNode* node = q.front();
            q.pop();
            if (node) {
                q.push(node->left);
                q.push(node->right);
                cout << node->val << " ";
            }
            else {
                cout << "null ";
            }
        }
        cout << endl;
    }
}

int main() {
    // 用 int* 指针来表示 null
    int a = 1, b = 3;
    vector<int*> arr = {&a, &b, nullptr};

    TreeNode* root = buildTree(arr);
    printTree(root);
    // 1
    // 3 null
}
```



## 102.二叉树的层序遍历[中等]*

### 链接

+ [102. 二叉树的层序遍历 - 力扣（LeetCode）](https://leetcode.cn/problems/binary-tree-level-order-traversal/description/)
+ [二叉树的层序遍历【基础算法精讲 13】](https://www.bilibili.com/video/BV1hG4y1277i)

### 题目

给你二叉树的根节点 `root` ，返回其节点值的 **层序遍历** 。 （即逐层地，从左到右访问所有节点）。

### 解法

```c++
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>>res;
        if(!root) return res; 
        queue<TreeNode*> que;
        que.push(root);
        while(!que.empty()){
            int size = que.size();
            vector<int> tmp;
            for(int i = 0; i < size; ++i){
                TreeNode* node = que.front(); que.pop();
                if(node->left) que.push(node->left);
                if(node->right) que.push(node->right);
                tmp.push_back(node->val);
            }
            res.push_back(tmp);
        }
        return res;
    }
};
```

## 103.二叉树的锯齿形层序遍历[中等]*

### 链接

+ [103. 二叉树的锯齿形层序遍历 - 力扣（LeetCode）](https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/)
+ [二叉树的层序遍历【基础算法精讲 13】](https://www.bilibili.com/video/BV1hG4y1277i)

### 题目

给你二叉树的根节点 `root` ，返回其节点值的 **锯齿形层序遍历** 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

### 思路

也很简单，用一个变量记录当前是奇数层还是偶数层即可。

### 解法

```c++
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> res;
        if(!root) return res;
        queue<TreeNode*> que;
        que.push(root);
        bool even = true;
        while(!que.empty()){
            int size = que.size();
            vector<int> tmp;
            for(int i = 0; i < size; ++i){
                TreeNode* node = que.front(); que.pop();
                if(node->left) que.push(node->left);
                if(node->right) que.push(node->right);
                tmp.push_back(node->val);
            }
            even = !even;
            if(even) reverse(tmp.begin(), tmp.end());
            res.push_back(tmp);
        }
        return res;
    }
};
```

## 513.找树左下角的值[中等]*

### 链接

+ [513. 找树左下角的值 - 力扣（LeetCode）](https://leetcode.cn/problems/find-bottom-left-tree-value/)
+ [二叉树的层序遍历【基础算法精讲 13】](https://www.bilibili.com/video/BV1hG4y1277i)

### 题目

给定一个二叉树的 **根节点** `root`，请找出该二叉树的 **最底层 最左边** 节点的值。

假设二叉树中至少有一个节点。

### 思路

这道题其实就是求左视图，和[199题](#199.二叉树的右视图[中等])如出一辙。如果用层序遍历，也有两种思路，一个是正常的层序遍历，然后返回最后一层的第一个节点；或者层序遍历时每一层从右往左遍历，这样最后一个节点就是答案了，下面给出后一种方法的代码。

### 解法

```c++
class Solution {
public:
    int findBottomLeftValue(TreeNode* root) {
        queue<TreeNode*> que;
        que.push(root);
        TreeNode* node;
        while(!que.empty()){
            node = que.front(); que.pop();
            if(tmp->right) que.push(node->right);
            if(tmp->left) que.push(node->left);
        }
        return node->val;
    }
};
```

## 662.二叉树最大宽度[中等]

### 链接

+ [662. 二叉树最大宽度 - 力扣（LeetCode）](https://leetcode.cn/problems/maximum-width-of-binary-tree)

### 题目

给你一棵二叉树的根节点 `root` ，返回树的 **最大宽度** 。

树的 **最大宽度** 是所有层中最大的 **宽度** 。

每一层的 **宽度** 被定义为该层最左和最右的非空节点（即，两个端点）之间的长度。将这个二叉树视作与满二叉树结构相同，两端点间会出现一些延伸到这一层的 `null` 节点，这些 `null` 节点也计入长度。

题目数据保证答案将会在 **32 位** 带符号整数范围内。

### 思路

第一次碰到这个题时的想法是，BFS然后对于空节点放虚拟节点进去，当成一个满二叉树来遍历，但是怎么避免虚拟节点无限递归下去是个问题，可以遍历队列看是不是都是空节点，若是则break。看个官解，不得不说很妙了，学习一下。这里对有值的节点额外维护它在满二叉树中的索引，直接简化掉了前面的问题。

### 解法

```python
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 1
        arr = [[root, 1]]
        while arr:
            tmp = []
            for node, index in arr:
                if node.left:
                    tmp.append([node.left, index * 2])
                if node.right:
                    tmp.append([node.right, index * 2 + 1])
            res = max(res, arr[-1][1] - arr[0][1] + 1)
            arr = tmp
        return res
```













