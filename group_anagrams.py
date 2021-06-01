class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return[[]]
        
        """
        anagrams =[[strs[0]]]
        flag = False
        for a in range(1, len(strs)):
            flag = False
            c = sorted(strs[a])
            for i,j in enumerate(anagrams):
                if sorted(c)==sorted(j[0]):
                    anagrams[i].append(strs[a])
                    flag = True
                    break
                
            
            if flag:
                continue
            anagrams.append([strs[a]])
            flag = False
            
        return anagrams
        
        """
        
        anagrams = {}
        for s in strs:
            s1 = ''.join(sorted(s))
            if s1 in anagrams.keys():
                anagrams[s1].append(s)
            else:
                anagrams[s1] = [s]
        return [a for a in anagrams.values()]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        