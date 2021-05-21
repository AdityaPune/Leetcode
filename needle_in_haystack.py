class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        a = len(needle)
        for i in range(0,len(haystack)-a+1):
            if haystack[i:i+a]==needle:
                return i
            
        return -1
           
        