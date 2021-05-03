class Solution:
    def maxArea(self, height: List[int]) -> int:

        i, j = 0, len(height)-1
        most = min(height[i], height[j])* (j-i)
        while i<j:            
            h = min(height[i], height[j])
            most = max(most, (j-i) * h)
            while height[i]<=h and i<j:
                i+=1 
            while height[j]<=h and i<j:
                j-=1
                    
        return most