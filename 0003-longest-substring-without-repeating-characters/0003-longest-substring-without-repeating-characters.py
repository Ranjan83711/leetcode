class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        max_len=float('-inf')
        seen=set()
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[i])
            max_len=max(max_len,i-left+1)
        if max_len==float('-inf'):
            return 0
        return max_len
        

        