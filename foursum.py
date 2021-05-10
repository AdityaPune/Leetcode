class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def fourSumHelper(nums, target, N, result, quadruplets):
            if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:
                return        
            if N==2:
                l, r = 0, len(nums)-1
                i, j = 0, len(nums)-1
                while i<j:
                    if (nums[i]+nums[j])==target:
                     
                        quadruplets.append(result+[nums[i], nums[j]])                       
                        i+=1
                        j-=1
                        
                        
                    elif (nums[i]+nums[j])>target:
                        j-=1                
                    else:
                        i+=1
            else:
                for i in range(len(nums)-N+1):
                    if i==0 or (i>0 and nums[i]!=nums[i-1]):
                        fourSumHelper(nums[i+1:], target- nums[i], N-1, result+ [nums[i]], quadruplets)
        
        quadruplets = []
        nums.sort()
        fourSumHelper(nums, target, 4, [], quadruplets)    
        res = []
        [res.append(x) for x in quadruplets if x not in res]                
        return res
            
                
                
        