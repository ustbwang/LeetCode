#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
#[3,2,4] 6
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for ind, num in enumerate(nums):
            hashmap[num] = ind    

        for i, num in enumerate(nums):      # 去遍历原来的，不遍历字典
            j = hashmap.get(target - num)
            if j is not None and i!=j:
                return [i,j]
        
# @lc code=end
a = Solution()
print(a.twoSum([3,3], 6))

