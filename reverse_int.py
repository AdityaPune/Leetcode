class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)
        flag = 0
        if x_str[0]=="-":
            x_str = x_str[1:]
            flag=1
            
        ans_str = [x for x in reversed(x_str)]
        
        ans_str = ''.join(ans_str)
        
        ans = int(ans_str)
        if flag==1:
            ans = -ans
        return ans if -2**31<=ans<=2**31-1 else 0
       
        