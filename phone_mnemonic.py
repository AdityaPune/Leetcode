dig = {'2': ['a','b','c'], '3': ['d', 'e', 'f'], '4':['g','h','i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p','q','r','s'], '8': ['t','u','v'], '9': ['w','x', 'y','z']}

def helper(idx, digits, curM, final):
    if idx==len(digits):
        final.append("".join(curM))        
    else:
        num = digits[idx]
        letters = dig[num]
        for letter in letters:
            curM[idx]=letter
            helper(idx+1, digits, curM, final)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not len(digits):
            return ""
        final = []
        
        curM = ["0"]*len(digits)
        
        helper(0, digits, curM, final)
        
        return final
        

        