from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s):
            return 0
        lastSeen = {}
        longest = 1
        startIdx = 0
        
        for i,char in enumerate(s):
            if char in lastSeen:
                startIdx = max(startIdx, lastSeen[char]+1)
            longest = max(longest, i+1-startIdx)
            lastSeen[char]=i
        return longest
            
            
        
            
        
        