#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#
# https://leetcode-cn.com/problems/sum-of-left-leaves/description/
#
# algorithms
# Easy (54.04%)
# Likes:    165
# Dislikes: 0
# Total Accepted:    29.1K
# Total Submissions: 52.9K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 计算给定二叉树的所有左叶子之和。
# 
# 示例：
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x, left=None, right=None):
#         self.val = x
#         self.left = left
#         self.right = right

# ⁠     1
# ⁠   /  \
# ⁠  2   3
# ⁠ / \  
# 4  5  
# 
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        result = 0
        if not root:
            return result
        ## 说明是一个数字
        if root.left and not root.left.left and not root.left.right:
            result += root.left.val


        result += self.sumOfLeftLeaves(root.left)
        result += self.sumOfLeftLeaves(root.right)

        return result


# @lc code=end

# a = Solution()
# print(a.sumOfLeftLeaves(TreeNode(1, TreeNode(2, 4, 5), 3)))

