#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#
# https://leetcode-cn.com/problems/rotate-list/description/
#
# algorithms
# Medium (39.95%)
# Likes:    379
# Dislikes: 0
# Total Accepted:    100.8K
# Total Submissions: 248.7K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
# 
# 示例 1:
# 
# 输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL
# 
# 
# 示例 2:
# 
# 输入: 0->1->2->NULL, k = 4
# 输出: 2->0->1->NULL
# 解释:
# 向右旋转 1 步: 2->0->1->NULL
# 向右旋转 2 步: 1->2->0->NULL
# 向右旋转 3 步: 0->1->2->NULL
# 向右旋转 4 步: 2->0->1->NULL
# 
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printf(head):
    res = []
    res.append(head.val)
    while head.next != None:
        head = head.next
        res.append(head.val)
    return res


## 方法一: 变成环的方式
#class Solution:
#    def rotateRight(self, head: ListNode, k: int) -> ListNode:
#        # 4->5->1->2->3->NULL
#        if head == None:
#            return head
#        length = 1
#        tmp = head
#        while tmp.next != None:
#            tmp = tmp.next
#            length = length + 1
#        
#        tmp.next = head  ## 变成环
#        # 此时tmp在最后是5
#        k = k%length
#        newtmp = tmp
#        for i in range(length - k):
#            newtmp = newtmp.next    # 找到3
#
#        head = newtmp.next      # 把4存下来
#        newtmp.next = None
#        return head


## 方法二: 
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # 4->5->1->2->3->NULL
        if head == None:
            return head
        length = 1
        tmp = head
        while tmp.next != None:
            tmp = tmp.next
            length = length + 1

        k = k%length
        for i in range(length - k):
            newtmp = newtmp.next    # 找到3



a = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
b = Solution()
print(printf(a))
print(printf(b.rotateRight(a, 2)))

# @lc code=end

