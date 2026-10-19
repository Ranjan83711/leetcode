class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        balance = 0
        max_length = 0
        first_seen = {0: -1}

        for i, num in enumerate(nums):
            if num == 1:
                balance += 1
            else:
                balance -= 1

            if balance in first_seen:
                length = i - first_seen[balance]
                max_length = max(max_length, length)
            else:
                first_seen[balance] = i

        return max_length