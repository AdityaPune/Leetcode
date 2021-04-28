from itertools import cycle
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        final= []
        
        for i,j in enumerate(cycle([x for x in range(1, numRows+1)]+[x for x in reversed(range(2,numRows))])):
            if i==len(s):
                break
            else:
                final.append([s[i],j])
                
        answer=""
        
        for m in range(1,numRows+1):
            for value in final:
                if value[1]==m:
                    answer+= value[0]
                    
        return answer
            
                
            
            
        
        