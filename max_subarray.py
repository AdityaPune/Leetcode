class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        a = [0 for x in range(len(nums))]
        a[0] = nums[0]        
        for i in range(1,len(nums)):
            a[i] = max(nums[i], nums[i]+a[i-1])
            
        return max(a)
            
        
            
        