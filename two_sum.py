class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d1 = {}        
        for i in range(len(nums)):  
            want = target - nums[i]
            if nums[i] in d1:
                return [ d1[nums[i]] , i]            
            else:
                d1[want] = i
        print(d1)
            