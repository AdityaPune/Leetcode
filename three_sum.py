class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        array = nums
        result = []
        nums.sort()
        for i in range(0,len(nums)-2):
            left = i+1
            right = len(nums)-1
            while left<right:
                if nums[i]>0:
                    break
                curSum = nums[i] + nums[left] + nums[right]
                if curSum==0:
                    if [nums[i], nums[left], nums[right]] not in result:
                        result.append([nums[i], nums[left], nums[right]])
                    left+=1
                    right-=1
                elif curSum<0:
                    left+=1
                elif curSum>0:
                    right-=1

        return result
        