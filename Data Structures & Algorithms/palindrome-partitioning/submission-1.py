class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans=[]
        def create(i,j,s,temp):
            nonlocal ans
         
            if j>len(s):
                if len("".join(temp))==len(s) and temp not in ans:
                    ans.append(list(temp))
                return 
            # print(temp,s[i:j],i,j)
            create(i,j+1,s,temp)
            val=s[i:j]
            # print("val",val[-1::-1])
            if val==val[-1::-1] and val!="":
                temp.append(val)
                create(j,j+1,s,temp)
                temp.pop()
            
        create(0,0,s,[])
        return ans

              
