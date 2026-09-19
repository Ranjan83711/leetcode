class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[j]<nums[i]:
                    nums[i],nums[j]=nums[j],nums[i]
                # elif nums[i]==nums[j]:
                #     nums[i+1]=nums[j]