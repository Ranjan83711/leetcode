class Solution:
    def frequencySort(self, s: str) -> str:
        result={}
        for i in s:
            if i not in result:
                result[i]=1
            else:
                result[i]+=1
        freq=list(result.values())
        ans=''
        for count in sorted(result.values(), reverse=True):
            for ch in result:
                if result[ch] == count:
                    ans += ch * count
                    result[ch] = -1
        return ans
        