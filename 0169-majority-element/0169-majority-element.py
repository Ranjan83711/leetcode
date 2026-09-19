class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freq={}
        for i in nums:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        value=max(freq.values())
        for i,j in freq.items():
            if j==value:
                return i


            
        