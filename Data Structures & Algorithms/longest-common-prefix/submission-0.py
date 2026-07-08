class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        temp= min(strs)
        res=""
        for i in range(0,len(temp)):
            for j in range(0,len(strs)):
                if(temp[i]!=strs[j][i]):
                    return res
            res+=temp[i]
        return res
        