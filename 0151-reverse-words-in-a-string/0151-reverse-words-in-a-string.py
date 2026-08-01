class Solution:
    def reverseWords(self, s: str) -> str:
        a=s.split()
        b=a[::-1]
        result=' '.join(b)
        return result
        