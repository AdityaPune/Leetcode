def getPal(s, leftIdx, rightIdx):
    while leftIdx>=0 and rightIdx<len(s):
        if s[leftIdx] != s[rightIdx]:
            break        
        leftIdx -= 1
        rightIdx +=1
    return [leftIdx+1, rightIdx]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest=[0, 1]
        
        for i in range(1,len(s)):
            odd = getPal(s, i-1, i+1)
            even = getPal(s, i-1,i)
            newLong = max(odd, even, key= lambda x: x[1]-x[0])
            
            longest = max(longest, newLong, key= lambda x: x[1]-x[0])          
        
        
        return s[longest[0]:longest[1]]