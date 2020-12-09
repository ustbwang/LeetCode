#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
# https://leetcode-cn.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (35.66%)
# Likes:    646
# Dislikes: 0
# Total Accepted:    63.4K
# Total Submissions: 165.7K
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# 给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。
# 
# 示例：
# 
# 输入: S = "ADOBECODEBANC", T = "ABC"
# 输出: "BANC"
# 
# 说明：
# 
# 
# 如果 S 中不存这样的子串，则返回空字符串 ""。
# 如果 S 中存在这样的子串，我们保证它是唯一的答案。
# 
# 
#

# @lc code=start
class Solution:
    def is_valid(self, s, t):
        _tmp1 = {}
        _tmp2 = {}
        for key in s:
            _tmp1[key] = _tmp1.get(key, 0) + 1
        for key in t:
            _tmp2[key] = _tmp2.get(key, 0) + 1

        for _k, _v in _tmp2.items():
            if _k not in _tmp1 or _tmp1[_k] < _tmp2[_k]:
                return -1
        return 1

    
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        right = 0
        start = 0
        minlen = len(s)
        flag = 0
        tmp = {}
        window = []
        for i in t:
            tmp[i] = 0
        while right < len(s):
            window.append(s[right])
            right += 1

            while self.is_valid(window, t) > 0:
                flag = 1
                if len(window) <= minlen:
                    start = left
                minlen = min(minlen, len(window))
                window.remove(s[left])
                left += 1
                print(start, minlen)

        if not flag:
            return ""
        else:
            return s[start:start+minlen]
        
# @lc code=end

a = Solution()
# print(a.minWindow("ADOBECODEBANC", "ABC"))
print(a.minWindow("cwaefgcf", "cae"))
