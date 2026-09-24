class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        sqr=[i**2 for i in nums]
        return sorted(sqr)
        
        