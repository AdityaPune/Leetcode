class Solution:
    def isValid(self, s: str) -> bool:
        d1 = {"(": ")", "[": "]", "{": "}"}
        ls = []
        for char in s:
            if char in d1.values():
                if len(ls) and d1[ls[-1]]==char:
                    ls.pop()
                else:
                    return False
            else:
                ls.append(char)
                
        return ls == []
                    
                    
        