class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        summ=0
        n=len(arr)
        for i in range(len(arr)):
           for j in range(i,n,2):
            summ+=sum(arr[i:j+1])
        return summ