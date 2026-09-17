class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        group={}
        for i in strs:
            keys=''.join(sorted(i))
            if keys not in group:
                group[keys]=[]
            group[keys].append(i)
        return list(group.values())