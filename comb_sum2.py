import numpy as np

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def combinationhelper(array, start, curr, final,  needed):
            if needed<0:
                return
            elif needed==0:
                if curr not in final:
                    final.append(curr)
                    return
            for i in range(start, len(array)):
                if i>start and array[i]==array[i-1]:
                    continue
                if array[i]>target:
                    break
                combinationhelper(array, i+1,  curr+[array[i]], final, needed - array[i])
        
        candidates.sort()
        final = []
        combinationhelper(candidates, 0,  [], final, target)
        return final
    