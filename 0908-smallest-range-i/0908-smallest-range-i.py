class Solution:
    def smallestRangeI(self, nums: list[int], k: int) -> int:
        minimum = min(nums)
        maximum = max(nums)

        return max(0, (maximum - k) - (minimum + k))