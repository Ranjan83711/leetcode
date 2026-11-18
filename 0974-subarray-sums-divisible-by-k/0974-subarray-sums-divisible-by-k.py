class Solution:
    def subarraysDivByK(self, nums, k):
        count = 0
        prefix_sum = 0

        freq = [0] * k
        freq[0] = 1

        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k

            count += freq[remainder]
            freq[remainder] += 1

        return count