#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
# https://leetcode-cn.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (68.06%)
# Likes:    1067
# Dislikes: 0
# Total Accepted:    272.4K
# Total Submissions: 391K
# Testcase Example:  '[1,2,3,4,5]'
#
# 反转一个单链表。
# 
# 示例:
# 
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
# 
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
# 
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
def printf(x):
    tmp = []
    while x.next:
        val = self.val
        tmp.append(val)
        self.next = self.next.next
    return tmp

class Solution:
    # 递归做法
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return 
        if head.next == None :
            return head
        
        nextList = self.reverseList(head.next)
        printf(nextList)

        head.next.next = head
        head.next = None
        return nextList   

    # def reverseList(self, head: ListNode) -> ListNode:
    #     if head == None:
    #         return 
    #     if head.next == None:
    #         return head
    #     #[1, 2, 3]
    #     prev = None  # 存上一个
    #     cur = head 
    #     while cur:    # 因为是按照head循环的，一定是把next赋给head，迭代的方法跟递归的类似
    #         nextlist = cur.next
    #         cur.next = prev
    #         prev     = cur
    #         cur      = nextlist
    #     return prev
        
        
# @lc code=end
a = Solution()
s = ListNode(1)
s.next = ListNode(2)
print(a.reverseList(s))

