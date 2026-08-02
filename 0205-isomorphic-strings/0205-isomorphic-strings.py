class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic={}
        for i,j in zip(s,t):
            if i in dic and dic[i]!=j:
                return False
            else:
                dic[i]=j
        return len(dic.keys())==len(set(s))==len(set(t))
        