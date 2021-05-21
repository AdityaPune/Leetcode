class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        low = 0
        n = len(nums)
        high = n-1        
        while low<=high:
            mid = (low+high)//2
            if nums[mid]==target:
                left = mid-1
                right=mid+1
                while left>=0 and nums[left]==nums[mid]:
                    left-=1
                while right<n and nums[right]==nums[mid]:
                    right+=1
                return [left+1,right-1]    
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
                
        return [-1,-1]
                
        