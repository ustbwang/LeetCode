#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (60.34%)
# Likes:    1143
# Dislikes: 0
# Total Accepted:    309.6K
# Total Submissions: 489.5K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
# 
# 
# 示例：
# 
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0, None)
        if l1 == None and l2 == None:
            return
        if l1 == None and l2!= None:
            return l2
        if l2 == None and l1 != None:
            return l1
        if l1.val <= l2.val:
            result.val = l1.val
            result.next = self.mergeTwoLists(l1.next, l2)
        else:
            result.val = l2.val
            result.next = self.mergeTwoLists(l2.next, l1)
        return result

# @lc code=end
# a = Solution()
# l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
# l2 = ListNode(5, ListNode(6, ListNode(7, ListNode(8, None))))

# print(a.mergeTwoLists(l1, l2))

