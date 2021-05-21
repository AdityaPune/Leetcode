class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if not nums:
            return -1
        
        
        low, high = 0, n-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[low]<=nums[mid]:
                if nums[low]<=target<=nums[mid]:
                    high = mid
                else:
                    low = mid+1
            else:
                if nums[mid]<=target<=nums[high]:
                    low = mid+1
                elif target>=nums[low] or target<=nums[mid]:
                    high = mid
                else:
                    return -1
        
        return -1
    
    