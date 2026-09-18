class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        n=sorted(set(nums))
        count=1
        maxx=1
        if len(nums)==0:
            return 0
        for i in range(len(n)-1):
            # if n[i]!=n[i+1]:
            if n[i+1]==n[i]+1:
                count+=1     
            else:
                count=1
            # else:
            #     return 1
            maxx=max(count,maxx)
        return maxx

        