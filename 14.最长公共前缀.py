#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (36.55%)
# Likes:    994
# Dislikes: 0
# Total Accepted:    245.6K
# Total Submissions: 660.4K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 
# 如果不存在公共前缀，返回空字符串 ""。
# 
# 示例 1:
# 
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 
# 
# 示例 2:
# 
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 
# 
# 说明:
# 
# 所有输入只包含小写字母 a-z 。
# 
#

# @lc code=start
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commonPrefix = ""
        if not strs or len(strs) < 1:
            return commonPrefix
        first = min(strs, key = lambda x:len(x))
        for idx,char in enumerate(first):
            for str in strs:
                if str[idx] != char:
                    return commonPrefix
            commonPrefix += char
        return commonPrefix
        

a = Solution()
print(a.longestCommonPrefix(["flower","flow","flight"]))
# @lc code=end

