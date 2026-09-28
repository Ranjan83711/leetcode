class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        word = {}
        left = 0
        max_freq = 0
        result = 0
        for right in range(len(s)):
            ch = s[right]
            if ch in word:
                word[ch] += 1
            else:
                word[ch] = 1
            max_freq = max(max_freq, word[ch])
            while (right - left + 1) - max_freq > k:
                word[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result