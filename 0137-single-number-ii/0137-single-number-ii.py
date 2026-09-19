class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for i,j in freq.items():
            if j<3:
                return i
        