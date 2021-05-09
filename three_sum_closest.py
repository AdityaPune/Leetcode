import numpy as np
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:        
        nums.sort()
        closest = nums[0]+nums[1]+nums[2]
        for i in range(0, len(nums)-2):
            left=i+1
            right=len(nums)-1
            while left<right:
                curSum = nums[i]+nums[left]+nums[right]
                if abs(target-curSum)<abs(target-closest): closest = curSum 
                if curSum == target:
                    return curSum
                elif curSum< target:
                    left+=1
                else:
                    right-=1
        return closest
        
        