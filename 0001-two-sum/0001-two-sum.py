class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen={}
        for i in range(len(nums)):
            remaining=target-nums[i]
            if remaining in seen:
                return [seen[remaining],i]
            else:
                seen[nums[i]]=i