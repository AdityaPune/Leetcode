class Solution:
    def romanToInt(self, s: str) -> int:
        sym={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        final=sym[s[-1]]        
        for i in reversed(range(0,len(s)-1)):
            if sym[s[i]]<sym[s[i+1]]:
                final -= sym[s[i]]
                continue
            final += sym[s[i]]                
        return final
                       
            