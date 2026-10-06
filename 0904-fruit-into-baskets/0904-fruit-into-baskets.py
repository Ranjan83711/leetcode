class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        left=0
        max_len=0
        freq={}
        for i in range(len(fruits)):
            if fruits[i] not in freq:
                freq[fruits[i]]=1
            else:
                freq[fruits[i]]+=1
            while len(freq)>2:
                left_fruits=fruits[left]
                freq[left_fruits]-=1
                if freq[left_fruits]==0:
                    del freq[left_fruits]
                left+=1
            max_len=max(max_len,i-left+1)
        return max_len
