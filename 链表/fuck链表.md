# 基础操作

链表的很多操作都要涉及多个指针的操作，我觉得比较核心的有：

+ 对于单链表而言，由于每个节点只有指向下一个节点的指针，因此所有的**增删元素都是对当前节点的下一节点进行操作**

## 206.反转链表[简单]*

### 链接

+ [206. 反转链表 - 力扣（LeetCode）](https://leetcode.cn/problems/reverse-linked-list/)
+ [反转链表【基础算法精讲 06】](https://www.bilibili.com/video/BV1sd4y1x7KN)

### 题目

给你单链表的头节点 `head` ，请你反转链表，并返回反转后的链表。

### 思路

反转链表也就是把原本从`pre`指向`cur`的指针反转成从`cur`指向`pre`的指针，很自然地就需要使用双指针（一个巴掌拍不响）,`cur`是我们当前正在处理的节点，（对于第一个节点`pre=NULL`，对于最后一个节点`cur=NULL`），此外我们还需要`nxt`来记录一下下一个`cur`，不然我们把`cur`的next指针反转过来了就没法遍历下一个节点了。

### 解法

```c++
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* pre = NULL, *cur = head;
        while(cur != NULL){
            ListNode *nxt = cur->next;
            cur->next = pre;
            pre = cur;
            cur = nxt;
        }
        return pre;
    }
};
```

## 92.反转链表 II[中等]*

### 链接

+ [92. 反转链表 II - 力扣（LeetCode）](https://leetcode.cn/problems/reverse-linked-list-ii/)
+ [反转链表【基础算法精讲 06】](https://www.bilibili.com/video/BV1sd4y1x7KN)

### 题目

给你单链表的头指针 `head` 和两个整数 `left` 和 `right` ，其中 `left <= right` 。请你反转从位置 `left` 到位置 `right` 的链表节点，返回 **反转后的链表** 。

### 思路

遍历时记录leftPre，leftNode，在left和right之间反转链表，到rightNode时记录rightNext，然后修改leftPre，leftNode，rightNode，rightNext之间的关系即可，即修改leftPre->rightNode, leftNode -> rightNext这两条边。

### 解法

```c++
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        int temp = left;
        ListNode* dummyHead= new ListNode(-1);
        dummyHead->next = head;
        ListNode* pre = dummyHead;
        for(int i = 0; i < left - 1; ++i){ 
            pre = pre->next;
        }
        // 此时pre刚好在left结点前面
        ListNode* leftPre = pre;
        pre = pre->next;
        ListNode* leftNode = pre;
        ListNode* cur = pre->next;
        for(int i = left; i < right; ++i){
            ListNode* next = cur->next;
            cur->next = pre;
            pre = cur;
            cur = next;
        }
        // 此时pre指向right结点
        ListNode* rightNext = cur;
        leftPre->next = pre;
        leftNode->next = rightNext;
        return dummyHead->next;
    }
};
```

## 25.K个一组翻转链表[困难]*

### 链接

+ [25. K 个一组翻转链表 - 力扣（LeetCode）](https://leetcode.cn/problems/reverse-nodes-in-k-group/description/)
+ [反转链表【基础算法精讲 06】](https://www.bilibili.com/video/BV1sd4y1x7KN)

### 题目

给你链表的头节点 `head` ，每 `k` 个节点一组进行翻转，请你返回修改后的链表。

`k` 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 `k` 的整数倍，那么请将最后剩余的节点保持原有顺序。

你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

### 解法

```c++
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        // 统计节点总数
        int n = 0;
        ListNode* tmp = head;
        while(tmp){
            n++;
            tmp = tmp->next;
        }

        ListNode* dummy = new ListNode(-1, head);
        ListNode* leftPre = dummy;
        while(n >= k){
            n -= k;

            ListNode* pre = NULL;
            ListNode* cur = leftPre->next;
            for(int i = 0; i < k; ++i){
                ListNode* tmp = cur->next;
                cur->next = pre;
                pre = cur;
                cur = tmp;
            }
            // 此时cur指向rightNext
            ListNode* leftNode = leftPre->next; // 原本蓝色的第一个节点
            leftNode->next = cur;
            leftPre->next = pre;
            leftPre = leftNode;
        }
        return dummy->next;
    }
};
```

## 237.删除链表中的节点[中等]*

### 链接

+ [237. 删除链表中的节点 - 力扣（LeetCode）](https://leetcode.cn/problems/delete-node-in-a-linked-list/)
+ [删除链表重复节点【基础算法精讲 08】](https://www.bilibili.com/video/BV1VP4y1Q71e)

### 题目

有一个单链表的 `head`，我们想删除它其中的一个节点 `node`。

给你一个需要删除的节点 `node` 。你将 **无法访问** 第一个节点 `head`。

链表的所有值都是 **唯一的**，并且保证给定的节点 `node` 不是链表中的最后一个节点。

删除给定的节点。注意，删除节点并不是指从内存中删除它。这里的意思是：

- 给定节点的值不应该存在于链表中。
- 链表中的节点数应该减少 1。
- `node` 前面的所有值顺序相同。
- `node` 后面的所有值顺序相同。

### 思路

这个题看起来很反直觉，在单链表中删除一个节点，还不让我们知道上一个节点，这根本做不到嘛！但细看题目，**所有节点的值唯一**，**不用从内存中删除**，似乎也暗示着我们只要把给定节点的值给它删掉即可（有点脑筋急转弯了）。题目又说了删除`node`前后所有值顺序不变，那么最简单的方法就是把`node`节点的下一个节点的值覆盖`node`，然后把下一个节点物理删除。

### 解法

```c++
class Solution {
public:
    void deleteNode(ListNode* node) {
        node->val = node->next->val;
        ListNode* nxt = node->next;
        node->next = nxt->next;
        delete nxt;
    }
};
```

## 21.合并两个有序链表[简单]

### 链接

+ [21. 合并两个有序链表 - 力扣（LeetCode）](https://leetcode.cn/problems/merge-two-sorted-lists)

### 题目

将两个升序链表合并为一个新的 **升序** 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

### 解法

```python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode()
        prev = dummyHead
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next
        prev.next = list1 if list1 else list2
        return dummyHead.next
```



# 快慢双指针

## 焚诀

链表中的快慢双指针与数组的双指针区别主要在于：

+ **利用快慢双指针来控制距离**
  + 例如求链表的中间节点，或者倒数第k个元素（一个先移动到第k个位置，然后另一个从头开始与之同步移动，直到第一个指针到达链表末尾，第二个指针即指向倒数第k个元素）

+ **龟兔赛跑算法来判断有没有环**



## 876.链表的中间结点[简单]*

### 链接

+ [876. 链表的中间结点 - 力扣（LeetCode）](https://leetcode.cn/problems/middle-of-the-linked-list/)
+ [环形链表II【基础算法精讲 07】](https://www.bilibili.com/video/BV1KG4y1G7cu)

### 题目

给你单链表的头结点 `head` ，请你找出并返回链表的中间结点。

如果有两个中间结点，则返回第二个中间结点。

### 思路

暴力一点，把所有节点存到一个数组中，最后返回数组中间位置的节点即可，时间复杂度$O(N)$，空间复杂度$O(N)$。

或者遍历两边链表，第一次拿到节点总数`N`，第二次遍历到`N/2`的位置，时间复杂度$O(2N)$，空间复杂度$O(1)$。

中间结点我们可以看做是在链表中**控制距离**（中间结点到头/尾结点的距离为链表长度的一半），因此可以考虑使用快慢指针。快指针每次走两步，慢指针每次走一步，这样当快指针走到末尾时，慢指针刚好在链表中间。

### 解法

```c++
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode* fast = head;
        ListNode* slow = head;
        while(fast != NULL && fast->next != NULL){
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow;
    }
};
```

+ 时间复杂度：$O(N)$
+ 空间复杂度：$O(1)$

上面的代码返回的是中间靠右边的节点，下面的代码返回的是靠左边的节点

```python
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        if(!head) return head;
        ListNode* fast = head;
        ListNode* slow = head;
        while(fast->next != NULL && fast->next->next != NULL){
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow;
    }
};
```

## 141.环形链表[简单]*

### 链接

+ [141. 环形链表 - 力扣（LeetCode）](https://leetcode.cn/problems/linked-list-cycle/)
+ [环形链表II【基础算法精讲 07】](https://www.bilibili.com/video/BV1KG4y1G7cu)

### 题目

给你一个链表的头节点 `head` ，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 `next` 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 `pos` 来表示链表尾连接到链表中的位置（索引从 0 开始）。**注意：`pos` 不作为参数进行传递** 。仅仅是为了标识链表的实际情况。

*如果链表中存在环* ，则返回 `true` 。 否则，返回 `false` 。

### 思路

判断链表是否有环，其实就是看有没有重复元素，符合使用哈希表的特征。不过哈希表需要使用额外$O(N)$的空间，在链表中我们可以使用快慢指针进行优化（龟兔赛跑算法）。同样快指针每次走两步，慢指针每次走一步，如果有环，那么快指针一定能追上慢指针，如果快指针变成`NULL`了，说明没有环。

### 解法

```c++
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode* slow = head, *fast = head;
        while(fast && fast->next){
            slow = slow->next;
            fast = fast->next->next;
            if(fast == slow){
                return true;
            }
        }
        return false;
    }
};
```

+ 时间复杂度：$O(N)$
+ 空间复杂度：$O(1)$

## 142.环形链表 II[中等]*

### 链接

+ [142. 环形链表 II - 力扣（LeetCode）](https://leetcode.cn/problems/linked-list-cycle-ii/)
+ [环形链表II【基础算法精讲 07】](https://www.bilibili.com/video/BV1KG4y1G7cu)

### 题目

给定一个链表的头节点  `head` ，返回链表开始入环的第一个节点。 *如果链表无环，则返回 `null`。*

如果链表中有某个节点，可以通过连续跟踪 `next` 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 `pos` 来表示链表尾连接到链表中的位置（**索引从 0 开始**）。如果 `pos` 是 `-1`，则在该链表中没有环。**注意：`pos` 不作为参数进行传递**，仅仅是为了标识链表的实际情况。

**不允许修改** 链表。

### 思路

经过141题的洗礼后，我们很容易想到这道题也能用快慢指针做。

我们使用两个指针，fast 与 slow。它们起始都位于链表的头部。随后，slow 指针每次向后移动一个位置，而 fast 指针向后移动两个位置。如果链表中存在环，则 fast 指针最终将再次与 slow 指针在环中相遇。

如下图所示，设链表中环外部分的长度为 a。slow 指针进入环后，又走了 b 的距离与 fast 相遇。此时，fast 指针已经走完了环的 n 圈，因此它走过的总距离为 a+n(b+c)+b=a+(n+1)b+nc。

<img src="https://assets.leetcode-cn.com/solution-static/142/142_fig1.png" width="80%">

根据题意，任意时刻，fast 指针走过的距离都为 slow 指针的 2 倍。因此，我们有

a+(n+1)b+nc=2(a+b)⟹a=c+(n−1)(b+c)
有了 a=c+(n−1)(b+c) 的等量关系，我们会发现：从相遇点到入环点的距离加上 n−1 圈的环长，恰好等于从链表头部到入环点的距离。

因此，当发现 slow 与 fast 相遇时，我们再额外使用一个指针 ptr。起始，它指向链表头部；随后，它和 slow 每次向后移动一个位置。最终，它们会在入环点相遇。

### 解法

```c++
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        ListNode* slow = head;
        ListNode* fast = head;
        while(fast != NULL && fast->next != NULL){
            slow = slow->next;
            fast = fast->next->next;
            if(fast == slow){ // 相遇后,slow走c步,head也走c步,二者之间的距离刚好是环长的倍数,所以持续走总会相遇
                while(slow != head){
                    slow = slow->next;
                    head = head->next;
                }
                return slow;
            }
        }
        return NULL;
    }
};
```

+ 时间复杂度：$O(N)$
+ 空间复杂度：$O(1)$

## 143.重排链表[中等]*

给定一个单链表 `L` 的头节点 `head` ，单链表 `L` 表示为：

```
L0 → L1 → … → Ln - 1 → Ln
```

请将其重新排列后变为：

```
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
```

不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

**示例 1：**

![img](https://pic.leetcode-cn.com/1626420311-PkUiGI-image.png)

```
输入：head = [1,2,3,4]
输出：[1,4,2,3]
```

### 思路

这个题还是很tricky的，先把链表从中间分成两半，把后一半的链表全部翻转过来，例如上面的例子就变成了`[1->2->3<-4]`，接下来用两个指针分别从两头交错合并成一个链表即可。（即876题和206题的结合）

### 解法

```c++
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode* fast = head;
        ListNode* slow = head;
        while(fast != NULL && fast->next != NULL){
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow;
    }
    ListNode* reverseList(ListNode* head) {
        ListNode* pre = NULL, *cur = head;
        while(cur != NULL){
            ListNode *nxt = cur->next;
            cur->next = pre;
            pre = cur;
            cur = nxt;
        }
        return pre;
    }
    void reorderList(ListNode* head) {
        ListNode* mid = middleNode(head);
        ListNode* head2 = reverseList(mid);
        while(head2->next) {
            ListNode* nxt = head->next;
            ListNode* nxt2 = head2->next;
            head->next = head2;
            head2->next = nxt;
            head = nxt;
            head2 = nxt2;
        }
    }
};
```

## 19.删除链表的倒数第N个结点[中等]*

###链接

+ [19. 删除链表的倒数第 N 个结点 - 力扣（LeetCode）](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/description/)

+ [删除链表重复节点【基础算法精讲 08】](https://www.bilibili.com/video/BV1VP4y1Q71e)

### 题目

给你一个链表，删除链表的倒数第 `n` 个结点，并且返回链表的头结点。

### 思路

倒数第N个结点属于典型的**控制距离**类型，可以先让快指针移动N步，然后快慢指针同时移动，当快指针到达末尾时，慢指针刚好指向倒数第N个结点。

### 解法

```c++
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* dummyHead = new ListNode(-1, head);
        ListNode* fast = dummyHead, *slow = dummyHead;
        while(n > 0) {
            fast = fast->next;
            n -= 1;
        }
        while(fast->next) {
            fast = fast->next;
            slow = slow->next;
        }
        // 此时slow指向倒数第N+1个结点
        ListNode* tmp = slow->next;
        slow->next = tmp->next;
        delete tmp;
        return dummyHead->next;
    }
};
```



# 递归

## 焚诀

对于链表，我写的绝大部分代码都是递推的，以前也没有想过用递归来处理链表，主要是[234.回文链表](#234.回文链表[简单])这道题启发了我。因此我总结的规律有：

+ **对于单链表，需要倒着处理节点**



## 234.回文链表[简单]

### 链接

+ [234. 回文链表 - 力扣（LeetCode）](https://leetcode.cn/problems/palindrome-linked-list)

### 题目

给你一个单链表的头节点 `head` ，请你判断该链表是否为回文链表。如果是，返回 `true` ；否则，返回 `false` 。

### 思路

这个题是简单题，我们可以用一些暴力的方法做出来，例如遍历链表然后把元素全存到数组里，然后再用双指针判断数组是否回文。对于单链表，我们的常规思路都是用递推的思路顺着链往后处理，想要倒着处理是做不到的。这道题一个很天才的想法在于我们可以使用递归，在“递”的过程是顺着链往后走的，到“归”的时候就是倒着处理了。

假设有一个递归函数dfs，我们沿着链表一直调用就能到达最后一个节点了，那么我们是不是可以拿这个节点和头节点开始比较了，所以额外需要一个指针left指向头节点（还是类似双指针的思路，不过right指针是在“归”的过程中往前走的）。递归到的当前节点就是right指针指向的位置，如果它的值和left指向的值不相等，可以直接返回False，我们期望整个dfs都应该是False的，所以前一个节点如果发现后面的节点返回了False，就继续返回False传播回去。如果二者的值相等，那么left指针就往后走一步，right指针返回True，那么就会递归到前一个节点去，前一个节点看到后面的节点返回True，就知道后面的节点都是匹配的，那么我们就继续比较当前节点即right指针和left指针指的值是否相等。

### 解法

```python
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        left = head
        def dfs(node):
            if node is not None:
                if not dfs(node.next):
                    return False
                nonlocal left
                if node.val != left.val:
                    return False
                # left和right匹配成功,left往后走一步,right在递归回去时相当于往前走一步
                left = left.next
            return True # 空节点返回True从而开始归
        return dfs(head)
```

+ 时间复杂度：$O(N)$
+ 空间复杂度：$O(N)$

虽然这个算法的性能算不得最优，但是思路挺新奇的，值得学习。

## 148.排序链表[中等]

### 链接

+ [148. 排序链表 - 力扣（LeetCode）](https://leetcode.cn/problems/sort-list)

### 题目

给你链表的头结点 `head` ，请将其按 **升序** 排列并返回 **排序后的链表** 。

### 思路

虽然题目没有限制复杂度，但是如果空间复杂度允许$O(N)$，那就是简单题了，直接转成数组做就行了。排序时间为$O(N\log N)$的算法有快排、堆排、归并，在链表中显然只能用归并排序，自顶向下的归并空间复杂度是$O(\log N)$，也就是递归的栈开销。[876.链表的中间结点](#876.链表的中间结点[简单]) 和 [21.合并两个有序链表](#21.合并两个有序链表[简单]) 的结合。

也可以改成自底向上的归并，先计算整个链表的长度，然后按1、2、4...的步长每次切两个链表出来归并，直到步长大于链表长度，空间就是$O(1)$了，感觉也没必要，就是递归变迭代嘛。

### 解法

```python
class Solution:
    def merge(self, left, right):
        dummyHead = ListNode()
        prev = dummyHead
        while left and right:
            if left.val <= right.val:
                prev.next = left
                left = left.next
            else:
                prev.next = right
                right = right.next
            prev = prev.next
        prev.next = left if left else right
        return dummyHead.next
    
    def middleNode(self, head):
       	slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: 
            return head
        mid = self.middleNode(head)
        right = mid.next
        mid.next = None
        left = self.sortList(head)
        right = self.sortList(right)
        return self.merge(left, right)
```

+ 时间复杂度：$O(N\log N)$
+ 空间复杂度：$O(\log N)$，栈开销



















# 哈希表

## 138.随机链表的复制[中等]

### 链接

+ [138. 随机链表的复制 - 力扣（LeetCode）](https://leetcode.cn/problems/copy-list-with-random-pointer)

### 题目

给你一个长度为 `n` 的链表，每个节点包含一个额外增加的随机指针 `random` ，该指针可以指向链表中的任何节点或空节点。

构造这个链表的 **[深拷贝](https://baike.baidu.com/item/深拷贝/22785317?fr=aladdin)**。 深拷贝应该正好由 `n` 个 **全新** 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 `next` 指针和 `random` 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。**复制链表中的指针都不应指向原链表中的节点** 。

例如，如果原链表中有 `X` 和 `Y` 两个节点，其中 `X.random --> Y` 。那么在复制链表中对应的两个节点 `x` 和 `y` ，同样有 `x.random --> y` 。

返回复制链表的头节点。

用一个由 `n` 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 `[val, random_index]` 表示：

- `val`：一个表示 `Node.val` 的整数。
- `random_index`：随机指针指向的节点索引（范围从 `0` 到 `n-1`）；如果不指向任何节点，则为 `null` 。

你的代码 **只** 接受原链表的头节点 `head` 作为传入参数。

**示例 1：**

![img](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/09/e1.png)

```
输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
```

### 思路

在做题目时，不要陷入“过度优化”的陷阱，其实遍历两次和遍历一次都是$O(N)$复杂度，所以有些题目不要执着于一次遍历就能一步到位，尤其是跟哈希表有关的一些题目。往往第一次遍历用来构建哈希表，第二次遍历利用哈希表$O(1)$的查询性能完成收尾工作。这个题还是很明显的，一次遍历肯定做不到，但关键在于如何**在新链表中知道旧链表中random指向的节点对应到新链表中哪个节点**。所以哈希表构建思路就是，在第一次遍历直接拷贝不包括random部分的节点时，记录一个从旧节点到新节点的映射。第二次遍历时再根据这个表，来构建新节点的random指针。

### 解法

```python
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        p = head
        dummyHead = Node(-1)
        q = dummyHead
        dict = defaultdict(list) # old node -> new node
        while p:
            q.next = Node(p.val)
            dict[p] = q.next 
            p = p.next
            q = q.next
        p = head
        q = dummyHead.next
        while p:
            if p.random:
                q.random = dict[p.random]
            p = p.next
            q = q.next
        return dummyHead.next
```

+ 时间复杂度：$O(N)$
+ 空间复杂度：$O(N)$



