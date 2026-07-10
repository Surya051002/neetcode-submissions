class Solution:

    def encode(self, strs: List[str]) -> str:
        arr=[]
        res=""
        for i in strs:
            arr.append(len(i))
            res+=str(len(i))+"#"+i

        return res




    def decode(self, s: str) -> List[str]:
        i=0
        print(s)
        ans=[]
        while i < len(s) :
            t=i
            while s[i]!='#':
                i+=1
            temp=int(s[t:i])+1
            ans.append(s[i+1:i+temp])
            i+=temp
        return ans

