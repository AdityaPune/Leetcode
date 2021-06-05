class Solution:
    def canJump(self, nums: List[int]) -> bool:
        a = len(nums)-1
        for i in reversed(range(0,len(nums)-1)):
            if i==a:
                continue
            req = a-i
            if nums[i]>=req:
                a = i
        return True if a==0 else False
        