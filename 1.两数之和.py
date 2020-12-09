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
        for ind, num in enumerate(nums):
            if target - num in hashmap and ind != hashmap[target - num]:                    
                return [ind, hashmap[target - num]]
        
# @lc code=end
a = Solution()
print(a.twoSum([2,7,11,15], 9))

