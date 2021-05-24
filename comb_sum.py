class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def combinationhelper(array, needed, final, curr, s):
            if s==150:
                return
            if needed<0:
                    return                
            elif needed==0:
                final.append(curr)
                s+=1
                
            for i in (range(len(array))):                            
                combinationhelper(array[i:], needed - array[i], final, curr+ [array[i]], s)
            
        final = []
        combinationhelper(candidates, target, final, [], 0)
        
        return final
        
        
        
        
        