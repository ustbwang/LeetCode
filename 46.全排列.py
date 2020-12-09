#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
# https://leetcode-cn.com/problems/permutations/description/
#
# algorithms
# Medium (74.39%)
# Likes:    788
# Dislikes: 0
# Total Accepted:    153.1K
# Total Submissions: 200.3K
# Testcase Example:  '[1,2,3]'
#
# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
# 
# 示例:
# 
# 输入: [1,2,3]
# 输出:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
#

# @lc code=start
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        length = len(nums)
        if len(nums) <=1:
            return [nums]
        
        for i in range(length):
            
            ss = []
            ss.extend([nums[i] for i in range(i)]) 
            ss.extend([nums[i] for i in range(i+1,length)])

            for jj in self.permute(ss):
                tmp1 = []
                tmp1.append(nums[i])
                tmp1.extend(jj)
                res.append(tmp1)

        return res
# @lc code=end

# a = Solution()
# print(a.permute([1,2,3]))

# nums = [1,2,3]
# length = len(nums)
# for i in range(length):
#     tmp = []
#     ss = []
#     ss.extend([nums[i] for i in range(i)]) 
#     ss.extend([nums[i] for i in range(i+1,length)])
#     print(ss)
