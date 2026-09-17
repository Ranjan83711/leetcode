class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq={}
        nums=sorted(nums)
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        values=sorted(freq.values(),reverse=True)[:k]
        lst=[]
        for i in values:
            for j in freq:
                if i==freq[j] and j not in lst:
                    lst.append(j)
        return lst
