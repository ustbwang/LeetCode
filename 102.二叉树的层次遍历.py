#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层次遍历
#
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (61.14%)
# Likes:    561
# Dislikes: 0
# Total Accepted:    159K
# Total Submissions: 252.2K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
# 
# 
# 
# 示例：
# 二叉树：[3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 返回其层次遍历结果：
# 
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        layer = [root]
        res = []
        while len(layer):
            this_res = []
            next_l = []
            for n in layer:
                this_res.append(n.val)
                if n.left:
                    next_l.append(n.left)
                if n.right:
                    next_l.append(n.right)
            res.append(this_res)
            layer = next_l
        return res
# @lc code=end
a = Solution()
print(a.levelOrder(TreeNode))

