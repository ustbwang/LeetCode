#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#

# @lc code=start
from typing import List
class Solution:
    
    def findnum(self, nums, start, end):
        count = 0
        for i in nums:
            if  start <= i <= end:
                count += 1
        return count

    def findDuplicate(self, nums: List[int]) -> int:
        start = 1
        end = len(nums)-1

        num = 0
        while start < end:
            middle = (start+end)//2
            # print(middle)
            cc = self.findnum(nums, start, middle)
            if cc <= middle-start+1 :     # 说明在右半部分
                start = middle+1
            else:                # 说明在左半部分
                end = middle

        return start
            

# @lc code=end
# a = Solution()
# print(a.findDuplicate([3,1,3,4,2]))

