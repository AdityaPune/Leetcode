class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not len(strs):
            return ""
        prefix = strs[0]
        
        for new in strs[1:]:
            while prefix != new[0:len(prefix)]:
                prefix = prefix[0:len(prefix)-1]
            
        return prefix
        
            
        