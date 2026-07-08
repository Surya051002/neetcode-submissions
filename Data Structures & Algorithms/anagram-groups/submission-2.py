class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        n=len(strs)
        for i in range(0,n):
            temp=strs[i]
            temp="".join(sorted(temp))
            if(temp in d):
                d[temp].append(strs[i])
            else:
                d[temp]=[strs[i]]
        ans=[]
        for item in d.items():
            ans.append(item[1])
        return ans

        