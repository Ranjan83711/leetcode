class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ana={}
        for i in strs:
            key=''.join(sorted(i))
            if key not in ana:
                ana[key]=[]
            ana[key].append(i)
        return list(ana.values())


        