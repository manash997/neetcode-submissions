class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_rec = {}
        t_rec = {}
        for val in s:
            if val in s_rec:
                c = s_rec[val]
                c+=1
                s_rec[val] = c
            else:
                s_rec[val] = 1
        for val in t:
            if val in t_rec:
                c = t_rec[val]
                c+=1
                t_rec[val] = c
            else:
                t_rec[val] = 1
        if s_rec == t_rec:
            return True
        else:
            return False
        
        